
import requests
import sys
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

from flask import Flask, request, json, render_template
app = Flask(__name__)

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
    act.check_constraints()

    return app.make_response(json.jsonify(act.summary_info()))
