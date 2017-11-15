# Python class symbolic objects and things
from sympy import *
from ..premise.premise import *
from ..verbs.verbs import *

def make_anchor_point(name):
      binding = find_anchor_point(name)
      if binding=='person':
            return person(name)
      elif binding=='animal':
            return animal(name)
      elif binding=='plant':
            return plant(name)
      elif binding=='object':
            return object(name)
      elif binding=='place':
            return place(name)
      else: return confusion(name)

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

class verb:
      def __init__(self, subject, name):
            self.name = name
            self.subject = subject
            self.type = find_verb_type(name)
            self.premises = []
            self.setInitialPremises()
      def setInitialPremises(self):
            # This may need some special case
            #self.premises.append(Premise(self.subject, self.type, True))
            return
# TODO make anchorpoint interface with all of the definitions it should have
# Move all of these to separate files

class person:
      def __init__(self, name, habitat=[], eats=[]):
            self.name = name
            self.habitat = habitat
            self.eats = eats
      def writeSummary(self):
            print(self.name + " is a person that lives in " + \
                        this.habitat + \
                        " and eats " + this.eats)
class animal:
      def __init__(self, name, habitat=[], eats=[]):
            self.name = name
            self.habitat = habitat
            self.eats = eats # (fish, plankton, 
            self.moves = True
            self.movesType = "on ground", "swim", "run"
            self.premises = []
            self.setInitialPremises()
      def setPremises(self):
            self.habitat = search_relation(self.name, 'AtLocation')
            self.eats = search_relation(self.name, 'Desires')
            
            # TODO - Need to put in a check for empty
            for place in self.habitat:
                  # make a new premise
                  # append to premises
                  new_premise = Premise(self.name, 'AtLocation', place)
                  # append to premises
                  self.premises.append(new_premise)
                  #self.premises.append((self.name, 'AtLocation', place))
            for food in self.eats:
                  new_premise = Premise(self.name, 'eats', food)
                  self.premises.append(new_premise)
                  #self.premises.append((self.name, 'eats', food))
      def setInitialPremises(self):
            # Changed these to premise objects as well
            self.premises.append(Premise(self.name, 'IsA', 'animal'))
            self.premises.append(Premise(self.name, 'action', True))
      def getPremises(self):
            return self.premises
      def writeSummary(self):
            print(self.name + " is an animal that lives in " + \
                        self.habitat[0] + \
                        " and eats " + self.eats[0])
                       
class plant:
      def __init__(self, name, location=[]):
            self.name = name
            self.location = location
      def writeSummary(self):
            print(self.name + " is a plant found  in " + \
                        self.location)
      def exportRelations(self):
            return self.relations

class object:
      def __init__(self, name, location=[]):
            self.name = name
            self.location = location
            self.premises = []
            self.setInitialPremises()
      def setPremises(self):
            self.location = search_relation(self.name, 'AtLocation')
            for place in self.location:
                  self.premises.append(Premise(self.name, 'AtLocation', place))
      def setInitialPremises(self):
            self.premises.append(Premise(self.name, 'IsA', 'object'))
            self.premises.append(Premise(self.name, 'action', False))
      def getPremises(self):
            return self.premises
      def writeSummary(self):
            print(self.name + " is an object  found  in " + \
                        self.location)
      def exportRelations(self):
            return self.relations

class place:
      def __init__(self, name, location=[]):
            self.name = name
            self.location = location
            self.premises = []
            self.setInitialPremises()
      def setPremises(self):
            self.location = search_relation(self.name, 'AtLocation')
            for place in self.location:
                  self.premises.append(Premise(self.name, 'AtLocation', place))
      def setInitialPremises(self):
            self.premises.append(Premise(self.name, 'IsA', 'place'))
            self.premises.append(Premise(self.name, 'action', False))
      def getPremises(self):
            return self.premises
      def writeSummary(self):
            print(self.name + " is a place in " + \
                        self.location)
      def exportRelations(self):
            return self.relations

class confusion:
      def __init__(self, name, location=[]):
            self.name = name
            self.location = location
      def writeSummary(self):
            print(self.name + " alters perception in  " + \
                        self.location)
      def exportRelations(self):
            return self.relations

                       
      	  
