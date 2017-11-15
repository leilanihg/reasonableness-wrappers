import argparse
import requests
import sys
import itertools
import logging
import operator
from .anchor import anchors
from .conceptnet.search import *
from .conflict.conflicts import *
# from nltk.stem.wordnet import WordNetLemmatizer
from .premise.premise import *
from .verbs.verbs import *

limit = 3
debug = False

class LocalMonitor:
    """A simple monitor class that stores premises, and checks for 
    inconsistencies"""
    def __init__(self, subject, verb, object, premises=[]):
        self.input = "%s %s %s" % (subject, verb, object) # TODO this may be changed
        self.subject = subject
        self.subject_anchor = anchors.make_anchor_point(subject) 
        self.verb = verb
        self.verb_anchor = anchors.verb(subject, verb) #WordNetLemmatizer().lemmatize(verb,'v')) 
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
