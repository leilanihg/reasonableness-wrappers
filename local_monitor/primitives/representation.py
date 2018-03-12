import argparse
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

def pos(strs):
    sentence = stringBuilder(strs)
    #get_tree(sentence) # FOR TESTING
    text = word_tokenize(sentence)
    tags = nltk.pos_tag(text)

# We may want a different grammar here
def get_tree(words):
    grammar = nltk.data.load('grammars/large_grammars/atis.cfg')
    parser = nltk.ChartParser(grammar)
    sent = words.split()
    for tree in parser.parse(sent):
        print(tree)

def get_atis_tree(words):
    grammar = nltk.data.load('grammars/large_grammars/atis.cfg')
    parser = nltk.ChartParser(grammar)
    for tree in parser.parse(words):
        print(tree)

def make_string_grammar(words):
    tags =nltk.pos_tag(words)
    print(tags)
    base = """
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
NP -> DT N | DT N PP
V -> VBZ | VBP | VBN | VBG | VBD | VB"""
    for (word, tag) in tags:
        base += "\n"
        base += tag
        base += " -> '"
        base += word
        base += "'"
    print(base)
    groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'the'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")
    grammar = nltk.CFG.fromstring(base)
    parser = nltk.ChartParser(groucho_grammar)
    for tree in parser.parse(tags):
        print(tree)

# This is exactly what is used
def parse_with_regex(words):
    tags = nltk.pos_tag(words)#check_tags(nltk.pos_tag(words))
    log.debug(tags)
    #grammar = "NP: {<DT>?<JJ>*<NN>}"
    parser = nltk.RegexpParser('''
    NP: {<DT|PRP$>? <JJ>* <NN|NNP|PRP>*} # NP
    P: {<IN|TO>}           # Preposition
    V: {<V.*>}          # Verb
    PP: {<P> <NP>}      # PP -> P NP
    Adv: {<RB|RBR|RBS>} # Adverbs
    VP: {<V V*> <NP|PP>*}  # VP -> V (NP|PP)*
    ''')
    result = parser.parse(tags)
    result.draw()
    #log.debug(result.draw())
    return result

def check_tags(tags):
    new_tags = []
    for (word, tag) in tags:
        if is_communication_verb(word):
            print("is it here")
            if not tag.startswith('V'):
                tag = 'VB'
        new_tags.append((word, tag))
    return new_tags

# Will also need to get "REAL" Noun as NN/Etc....
def get_noun_phrase(tree):
    phrase = ''
    for subtree in tree.subtrees(filter = filter_noun):
        for (name, label) in subtree:
            if label.startswith('N') or label.startswith('PRP'):
                noun = name
            phrase += name
            phrase += ' '
        # Assume it's the first noun
        return (noun, phrase.strip())

#
def get_verbs(tree, verbose=False):
    phrases = {}
    context = []
    verb_object = None
    for subtree in tree.subtrees(filter = filter_verb):
        for item in subtree:
            if item.label() == 'V':
                phrase = ''
                for (verb, label) in item.leaves():
                    phrase += verb
                    phrase += ' '
                if 'verb' in phrases:
                    phrases['verb'].append(phrase.strip())
                else:
                    phrases['verb'] = [phrase.strip()]
                # logic is that the last verb is the base
                #if not base_verb:
                base_verb = WordNetLemmatizer().lemmatize(phrases['verb'][-1], 'v')
            elif item.label() == 'NP':
                phrase = ''
                for (obj, label) in item.leaves():
                    if label.startswith('N'):
                        verb_object = obj
                    phrase += obj
                    phrase += ' '
                if 'object' in phrase:
                    phrases['object'].append(phrase.strip())
                else:
                    phrases['object'] = [phrase.strip()]
            elif item.label() == 'PP':
                phrase = ''
                for (prep, label) in item.leaves():
                    if label.startswith('N'):
                        context.append(prep)
                    phrase += prep
                    phrase += ' '
                if 'preposition' in phrases:
                    phrases['preposition'].append(phrase.strip())
                else:
                    phrases['preposition'] = [phrase.strip()]
    if context:
        if verbose:
            print("  Context is %s" % phrases)
    return (base_verb, verb_object, context, phrases)

def filter_noun(tree):
    return tree.label() == 'NP'

def filter_verb(tree):
    return tree.label() == 'VP'

# First is the noun phrase
# Second is verb phrase?
# Third is the object (phrase)
def translate_from_simple_parse(tree, tagged_text):
    for item in tree:
        print("next")

        print(item)

def test_again(tokens):
    tag_dict = defaultdict(list)

    # Tag
    tagged_sent = nltk.pos_tag(tokens)

    # Put tags and words into the dictionary
    for word, tag in tagged_sent:
        if tag not in tag_dict:
            tag_dict[tag].append(word)
        elif word not in tag_dict.get(tag):
            tag_dict[tag].append(word)

# Printing to screen
    for tag, words in tag_dict.items():
        print(tag, "->")
        first_word = True
        for word in words:
            if first_word:
                print("\"" + word + "\"")
                first_word = False
            else:
                print("| \"" + word + "\"")
        print('')

# TODO - Need verbose
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sentence', nargs='+',
                    help='Sentence')
    parser.add_argument("-d", "--debug", action='store_true',
                        help='print debug messages to stderr')
    parser.add_argument("-v", "--verbose", action='store_true',
                        help='This is the same as debug right now')
    args = parser.parse_args()


    if args.debug:
        log.basicConfig(format="%(levelname)s: %(message)s",
                        level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")
    if args.verbose:
        print("INFO: Verbose OUTPUT\n")

    tree = parse_with_regex(args.sentence)
    (noun, noun_phrase) = get_noun_phrase(tree)
    (verb, object, context, phrase_dict) = get_verbs(tree, args.verbose)
    phrase_dict['noun'] = noun_phrase
    #long_context = phrase_dict['preposition'] 

    # get verb type
    act = get_verb_type(verb, noun, object, context, phrase_dict, args.verbose)
    consistent = act.check_constraints()
    act.print_summary(consistent)
if __name__ == "__main__":
    main()
