from enum import Enum
from sympy import *

# Builds a relationship dictionary from a txt file
# TODO - may want to use this in the future
def build_relation_dictionary():
    relationList = []
    with open('relations.txt', 'r') as f:
        for line in f:
            elements = ""
            return relationList

def getRelationEnum(rel_string):
    for relation in Relation:
        if rel_string == relation.name:
            return relation
        elif rel_string.lower() == relation.name.lower():
            return relation

# As found in ConceptNet
# Relations in ConceptNet5
# Found here: https://github.com/commonsense/conceptnet5/wiki/Relations
# TODO - May want to build this as a textfile 
# TODO - May want to make this a dictionary
class Relation(Enum):
    RelatedTo = "has/have some positive relationship to "
    ExternalURL = "points to a URL outside of ConceptNet"
    FormOf = "is/are an inflected form of "
    IsA = "is/are a subtype(s) or specific instance(s) of "
    PartOf = "is/are part of "
    HasA = " " # NEED TO FLIP
    UsedFor = " is/are used for "
    CapableOf = " can typically do for " 
    AtLocation = ", which is typically found in location:"
    Causes = " cause(s) " 
    
    # Verb actions - I created 
    Eats = " eats "
    Moves = " moves "
    Action = " action "

    # These don't seem super relevant to us
    HasSubevent = symbols('HasSubevent')
    HasFirstSubevent = symbols('HasFirstSubevent')
    HasLastSubevent = symbols('HasLastSubevent')
    HasPrerequisite = symbols('HasPrerequisite')
    HasProperty = symbols('HasProperty')
    MotivatedByGoal = symbols('MotivatedByGoal')
    ObstructedBy = symbols('ObstructedBy')
    Desires = symbols('Desires')
    CreatedBy = symbols('CreatedBy')
    Synonym = symbols('Synonym')
    Antonym = symbols('Antonym')
    DerivedFrom = symbols('DerivedFrom')
    SymbolOf = symbols('SymbolOf')
    DefinedAs = symbols('DefinedAs')
    Entails = symbols('Entails')
    MannerOf = symbols('MannerOf')
    LocatedNear = symbols('LocatedNear')

class State(Enum):
    REASONABLE = "reasonable"
    UNREASONABLE = "unreasonable"
    DONT_CARE = "don't care"

def main():
    for relation in Relation:
        print(relation)
        print(relation.value)