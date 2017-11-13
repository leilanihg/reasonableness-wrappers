import argparse
import requests
import sys
import anchors
import itertools
import logging
import operator
from conflicts import *
from nltk.stem.wordnet import WordNetLemmatizer
from premise import *
from search import *

limit = 3
query_prefix = 'http://api.conceptnet.io/c/en/'
debug

class LocalMonitor:
    """A simple monitor class that stores premises, and checks for 
    inconsistencies"""
    def __init__(self, subject, verb, object, premises=[]):
        self.input = "%s %s %s" % (subject, verb, object) # TODO this may be changed
        self.subject = subject
        self.subject_anchor = anchors.make_anchor_point(subject) 
        self.verb = verb
        self.verb_anchor = anchors.verb(subject, WordNetLemmatizer().lemmatize(verb,'v')) 
        self.object = object
        self.object_anchor = anchors.make_anchor_point(object) 
        self.premises = premises
        self.conflicts = None
        self.state = State.REASONABLE

        self.subject_anchor.setPremises()
        self.object_anchor.setPremises()
        self.addPremises(self.subject_anchor.getPremises())
        self.addPremises(self.verb_anchor.premises)
        self.addPremises(self.object_anchor.getPremises())

        print(debug)
        if debug:
            print("DEBUG MODE")
        logging.debug('Printing Anchor Points')
        logging.debug('')

    def addPremises(self, new_premises):
        for premise in new_premises:
            self.premises.append(premise)
    
    def pp_premise(self):
        for premise in self.premises:
            print(premise.print_summary())

    def print_header(self):
        print("The input statement: %s" % (self.input))
        print("Parsed as : (%s, %s, %s)" % (self.subject, self.verb_anchor.name, self.object))
        print("\nThis perception is %s)" % (self.state.name))
        print("   Using data from ConceptNet 5")

    def detectConflicts(self):
        # Conflicts in relations
        splits = split_premises(self.premises)
        self.conflicts = relation_conflict(splits)
        if self.conflicts:
            self.state = State.UNREASONABLE
        self.explain()

    def removeConflict(self, premise):
        self.premises.remove(premise)

    def explain(self):
        self.print_header()
        if self.conflicts:
            for rel in self.conflicts:
                [rel1, rel2] = rel
                print(rel1.print_summary(),"is not close to",rel2.print_summary())
        else: 
            print("REASONABLE TO DO")# Print summary if reasonable

# Finds the specific anchor point or type of a specific word
def find_anchor_point(word):
    concepts = ['animal', 'object', 'place', 'plant']
    for concept in concepts:
        #relation = isA(word, concept)
        if(has_IsA_edge(word, concept)):
            return concept
    for concept in concepts:    
        if(find_IsA_path(word, concept)):
            return concept
    return 'confusion'

# Moving - is there an edge between action and move
# Linking - perhaps an exact check
# Helping - to be is linking and helping
# Possession - perhaps an exact check
# Communication - connection to talk/speak or listen/hear
def find_verb_type(verb):
    types = ['action', 'linking', 'helping', 'passive', 'possession', 
             'communication']
    action_verbs = ['move', 'action']
    if(is_linking_verb(verb)):
        return 'linking'
    elif(is_helping_verb(verb)):
        return 'helping'
    elif(is_possession_verb(verb)):
        return 'possession'
    elif(is_communication_verb(verb)):
        return 'communication'
    elif(is_action_verb(verb)):
        return 'action'
    else: return 'preposition'

# Checks if a verb is a type of action
def is_action_verb(verb):
    if(has_any_edge(verb, 'move')):
        return True
    elif(has_any_edge(verb, 'action')):
        return True
    else: return False

# A linking verb connects a subject to predicate without expressing an action
# Relating to the five sense (to look, to feel, to smell, to sound, to taste
# Taken from grammar-monster.com
#http://www.grammar-monster.com/glossary/linking_verbs.htm
def is_linking_verb(verb):
    toBe = ['is', 'am', 'are','was' 'were', 'be', 'being', 'been']
    toAppear = ['appears', 'appear', 'appeared', 'appearing']
    toBecome = ['becomes', 'become', 'became', 'becoming']
    toFeel = ['feels', 'feel', 'felt', 'feeling']
    toLook = ['looks', 'look', 'looked', 'looking']
    toSeem = ['seems', 'seem', 'seemed', 'seeming']
    toSmell = ['smells', 'smell', 'smelled', 'smelling']
    toSound = ['sounds', 'sound', 'sounded', 'sounding']
    toTaste = ['tastes', 'taste', 'tasted', 'tasting']

    linkingVerbs = []
    linkingVerbs = toBe + toAppear + toBecome + toFeel + toLook + toSeem + \
        toSmell + toSound + toTaste
    if verb in linkingVerbs:
        return True
    else: return False

# progressive and perfect aspects
# Performing specific takss
# No actions
def is_helping_verb(verb):
    toBe = ['is', 'am', 'are','was' 'were', 'be', 'being', 'been']
    conditionals = ['could', 'should', 'would', 'can', 'shall', 'will', 
                    'may', 'might', 'must']
    toHave = ['have', 'has', 'had']
    toDo = ['do', 'does', 'did']
    helpingVerbs = []
    helpingVerbs = toBe + conditionals + toHave + toDo
    if verb in helpingVerbs:
        return True
    else: return False

# A verb showing ownership
def is_possession_verb(verb):
    toHave = ['have', 'has', 'had', 'having']
    toGet = ['get', 'gets', 'getting', 'got']
    toTake = ['take', 'takes', 'took', 'taking']
    toGive = ['give', 'gives', 'gave', 'giving']
    toNeed = ['need', 'needs', 'needed', 'needing']
    toKeep = ['keep', 'keeps', 'kept', 'keeping']
    toProvide = ['provide', 'provides', 'provided', 'providing']
    toPay = ['pay', 'pays', 'paid', 'paying']
    toBuy = ['buy', 'buys', 'bought', 'buying']
    toSend = ['send', 'sends', 'sent', 'sending']
    
    toBelong = ['belong', 'belongs', 'belonged', 'belonging']
    toPossess = ['possess', 'possesses', 'possessed', 'possessing']
    toHold = ['hold', 'holds', 'held', 'holding']
    possessionVerbs = []
    possessionVerbs = toHave + toGet + toTake + toGive + toNeed + \
        toKeep + toProvide + toPay + toBuy + toSend + toBelong + \
        toPossess + toHold
    if verb in possessionVerbs:
        return True
    else: return False

# TODO - scream yell, argue 
def is_communication_verb(word):
    toTalk = ['talk', 'talks', 'talked', 'talking']
    verb = WordNetLemmatizer().lemmatize(word,'v')
    return has_any_edge(verb, 'communicate')        

def containsConcept(concept, list):
    for item in list:
        if concept in item[0]:
            return item[0]
    return False

# Checks if there is any correlation (just an edge)
def has_any_edge(word, concept):
    word_text = word.replace(" ", "_").lower()
    obj = requests.get('http://api.conceptnet.io/query?node=/c/en/'+word_text+\
                           '&other=/c/en/'+concept).json()
    edges = obj['edges']
    if(edges):
        return True
    else: return False

# First check if there is a direct connection via an IsA relation
def has_IsA_edge(word, concept):
    word_text = word.replace(" ", "_").lower()

    obj = requests.get(query_prefix+word_text+'?rel=/r/IsA&limit=1000').json()
    edges = obj['edges']
    for edge in edges:
        start = edge['start']['label'].lower()
        end = edge['end']['label'].lower()

        if(search_equals(word, start) and isA_equals(concept, end.lower())):# == concept.lower()):
            return True
    return False

# Phrases don't always count
def isA_equals(concept, phrase):
    if concept in phrase:
        return True
    else: return False

# TODO - something strange about the query request
# So hard-coded in a check for the relation
def search_relation(word, relation):
    concepts = []
    word_text = word.replace(" ", "_").lower()
    obj = requests.get(query_prefix+word_text+'?rel=/r/'+relation+
                       '&limit=1000').json()
    edges = obj['edges']
    for edge in edges:
        if edge['rel']['label'] == relation:
            end = edge['end']['label'].lower()
            concepts.append(end)
    return concepts

# Explains whether the triple is reasonable or not
def explain(triple):
    [subject, verb, object] = triple
    monitor = LocalMonitor(subject, verb, object)
    monitor.detectConflicts()

# May need a more detailed interface
# TODO - Need verbose 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('triple', nargs='+',
                    help='subject verb object triple separated by whitespace')
    parser.add_argument("-d", "--debug", action='store_true', 
                        help='print debug messages to stderr')
#    parser.add_argument("-v", "--verbose", help="increase output verbosity",
#                    action="store_true")
    
    args = parser.parse_args()
    #debug = args.verbose
    debug = args.debug
    print(debug)
#    if args.verbose:
#        logging.basicConfig(level=logging.DEBUG) # This does things for request

    #logging.debug('Only shown in debug mode')    
    explain(args.triple)

if __name__ == "__main__":
    main()
