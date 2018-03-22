from .anchors import *

# Super class
# PP  - (picture producer) A physical object
#     - Actions must be animate PP, or a natural force TODO CONSTRAINT
# ACT - one of the eleven primitive actions
# LOC - Location
# T   - Time
# AA  - (Action aider) Modifications of features of an ACT
#     - E.g. speed factor in propel
# PA  - attributes of an object, of the form STATE(VALUE)
#     - e.g. COLOR(red)

class ACT:
    def __init__(self, subject, verb, object, context=None, phrases=None, verbose=False):
        self.support = []
        self.violations = []
        self.props = [] # Propositions that NEED to be printed

        # check if name here
        self.subject = self.clean_name(subject)
        self.verb = verb
        self.object = self.clean_name(object)
        #self.subject_phrase = subject_phrase
        self.context = context
        self.phrases = phrases
        self.world = None
        if 'preposition' in phrases:
            print("setting the prepositions")
            self.pp = phrases['preposition']
        else:
            self.pp = None
        self.verbose = verbose # default is false
        self.light = None # Special case for the vehicle, may want to change
    
    # if give a name, it returns a person anchor
    def clean_name(self, subject):
        if subject == None:
            return None
        if subject.istitle():
            self.support.append("Capitalized names are assumed to belong to people.")
            return 'person'
        return subject      

    def constaints_violated(self):
        if violated:
            return self.constraints

    def add_subject_support(self, subject, anchor_point, action):
        self.support.append("A(n) %s is a(n) %s that can %s on their own." % (subject, anchor_point, action))
    
    def add_subject_violation(self, subject, action):
        self.violations.append("A(n) %s can not %s on their own." % (subject, action))

    def add_object_support(self, object, anchor_point, action):
        self.support.append("A(n) %s is a(n) %s that can be %sed." % (object, anchor_point, action))
 
    def add_object_violation(self, object, action):
        self.violations.append("A(n) %s can not be %sed." % (object, action))

    def print_summary(self, consistent=False):
        if self.check_constraints():
            print("\n")
            print("This perception is reasonable")
            print("=============================================")
            for element in self.support:
                print(element)
            print("So it is reasonable for", self.summary())
        else:
            print("\n")
            print("This perception is unreasonable")
            print("=============================================")
            for element in self.violations:
                print(element)
            print("So it is unreasonable for", self.summary())

    def summary_info(self):
        return {
            'reasonable': len(self.violations) == 0,
            'caption_summary': self.summary(),
            'support': self.support,
            'violations': self.violations
        }

    def summary(self):
        if 'object' in self.phrases:
            summary = "%s to %s %s" %\
                (self.phrases['noun'].lower(), self.verb, self.phrases['object'][0])
            print(self.phrases)
            print(self.verb)
            print(self.phrases)
        else:
            summary = "%s to %s" %(self.phrases['noun'].lower(), self.verb)
        if self.props:
            for element in self.props:
                summary += " %s" %element
        return summary

    # TODO, may want to fill this in
    def setLight(self):
        return False

# 2 state changes for physical and abstract transfers
# PRTRANS -  To change the location of a physical object
# ATRANS - To change an abstract relationship of a physical object
class StateChange(ACT):
    def constaints_violated(self):
        if violated:
            return self.constraints

# 2 mental acts
# MTRANS - to transfer information mentally
# MBUILD - to create or combine thoughts
class MentalAct(ACT):
    def constaints_violated(self):
        if violated:
            return self.constraints

# Instrument for other ACT
# To produce a sound
class Speak(ACT):
    def can_speak(self, subject):
        if has_IsA_edge(subject, 'animal', self.verbose) and not subject == 'plant':
            self.support.append("A(n) %s is an animal and animals can communicate" % subject)
        else: return False

    def check_constraints(self):
        if self.can_speak(self.subject):
            return True
        else:
            violation = "A %s is an object or thing that does not have the ability to produce sounds" %(self.subject)
            self.violations.append(violation)
            return False

# Instrument for other ACT
# To direct a sense organ or focus an organ towards a stimulus
class Attend(ACT):
    def constaints_violated(self):
        if violated:
            return self.constraints

# A person object or thing changes physical position or localion
# JM - The object must be a physical object, thing, substance of person
#    - The actor must be "animate" object of thing capable of making other
#      objects move
#    - The direction case hsould represent a direction in reference to a 
#      physical object
class PTrans(StateChange):
    def constraints(self):
        return None

    def summary(self):
        return self.subject.join("changes physical position or location")
        print(self.subject, "changes physical position or location")

# To change an abstract relationship of a physical object
class ATrans(StateChange):
    def constraints(self):
        return None

    def summary(self):
        return self.subject.join("changes abstraction relationship of a physical object")
        print(self.subject, "changes physical position or location")

# # Another specific vehicle type primitive
# class Wait(Move):
#     def check_constraints(self):
#         consistent = False
#         if self.pp:
#             for context in self.pp:
#                 if 'green light' in context:
#                     self.light = 'green'
#                     self.violations.append("A green light means go, which is inconsistent with waiting.")
#                     consistent = False
#                 elif 'red light' in context:
#                     self.light = 'red'
#                     self.support.append("A red light means stop.")
#                     consistent = True
#                 elif 'yellow light' in context:
#                     self.light = 'yellow'
#                     self.support.append("A yellow light means 'stop if safe'.  So waiting is reasonable")
#                     consistent = True
#                 if 'pedestrian' in context:
#                     if self.light is 'green':
#                         self.support.append("Although green means go, green also means yields to pedestiran in the road.")
#                     self.support.append("Since there is a pedestrian in the road, waiting is reasonable.")
#                     consistent = True
#         print("consistent is", consistent)
#         return consistent 

#     def check_subject_constraints(self):
#         return False

# # Another specific vehicle type primitive
# class Yield(Move):
#     def check_constraints(self):
#         return False

#     def check_subject_constraints(self):
#         return False


# TODO change MOVE to be itself or body, and use PROPEL instead ("a man moves a hurricane", should be propel)
# Some examples that work
# A classy plant crossed the street

# TODO need to fix the object problem
# A penguin flying across the sky - is reasonable, should be unreasonable
