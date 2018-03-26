
import requests
import sys
import os
import itertools
import logging as log # Suggestion from stackoverflow
import operator
from .primitives import *
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
from nltk.stem.wordnet import WordNetLemmatizer
#from conceptnet.search import *
from .search import *
from .verbs import *
from .representation import *

import io
log_data = io.StringIO()
log.basicConfig(stream=log_data, format="%(levelname)s: %(message)s",
                level=log.DEBUG)

from flask import Flask, request, json, render_template
app = Flask(__name__)

from werkzeug.utils import secure_filename

import subprocess

RUN_INFERENCE = "/REPLACE/WITH/im2txt/bazel-bin/im2txt/run_inference"
CHECKPOINT = "/REPLACE/WITH/im2txt/model.ckpt-20000"
WORD_COUNTS = "/REPLACE/WITH/im2txt/word_counts.txt"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/1/evaluate", methods=['POST'])
def evaluate():
    req_data = request.get_json(silent=True)
    if not req_data:
        r = app.make_response(json.jsonify({'error': "no request specified"}))
        r.status_code = 400
        return r
    if 'caption' not in req_data:
        r = app.make_response(json.jsonify({'error': "no caption specified"}))
        r.status_code = 400
        return r

    tree = parse_with_regex(req_data['caption'].split(' '))
    (noun, noun_phrase) = get_noun_phrase(tree)
    (verb, object, context, phrase_dict) = get_verbs(tree)
    phrase_dict['noun'] = noun_phrase

    # get verb type
    act = get_verb_type(verb, noun, object, context, phrase_dict, False)
    consistent = act.check_constraints()

    resp = act.summary_info()
    resp['reasonable'] = resp['reasonable'] or consistent
    resp['log_data'] = log_data.getvalue()

    return app.make_response(json.jsonify(resp))

@app.route("/api/1/caption", methods=['POST'])
def caption():
    if 'file' not in request.files:
        r = app.make_response(json.jsonify({'error': "no file provided"}))
        r.status_code = 400
        return r

    the_file = request.files['file']
    if the_file.filename == '':
        r = app.make_response(json.jsonify({'error': "no file provided"}))
        r.status_code = 400
        return r

    fn = secure_filename(the_file.filename)
    path = os.path.join("/tmp/", fn)
    the_file.save(path)

    caption_info = subprocess.check_output([RUN_INFERENCE, \
    "--checkpoint_path={0}".format(CHECKPOINT), \
    "--vocab_file={0}".format(WORD_COUNTS), \
    "--input_files={0}".format(path)])

    caption_info = caption_info.decode().split('\n')

    caption = caption_info[1].split(')')[1].split('(')[0].strip()

    return app.make_response(json.jsonify({'caption': caption}))
