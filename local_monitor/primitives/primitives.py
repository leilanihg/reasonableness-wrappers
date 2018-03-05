from .search import *

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
        self.subject = subject
        self.verb = verb
        self.object = object
        #self.subject_phrase = subject_phrase
        self.context = context
        self.phrases = phrases
        self.support = []
        if 'pp' in phrases:
            self.pp = phrases['pp']
        self.violations = []
        self.props = [] # Propositions that NEED to be printed
        self.verbose = verbose # default is false
    def constaints_violated(self):
        if violated:
            return self.constraints

    # Added for the new primitives
    def is_animate(self, subject, action='move'):
        if has_IsA_edge(subject, 'vehicle', self.verbose):
            self.support.append("A(n) %s is a vehicle that can %s on their own." % (subject, action))
            return True
        elif has_IsA_edge(subject, 'animal', self.verbose):
            self.support.append("A(n) %s is an animal and animals can %s on their own." % (subject, action))
            return True
        elif has_IsA_edge(subject, 'person', self.verbose):#and not has_IsA_edge(subject, 'plant', self.verbose)
            self.support.append("A(n) %s is a person that can %s on their own." % (subject, action))
            return True
        elif subject.istitle():
            self.support.append("Capitalized names are assumed to belong to people.")
            self.support.append("So, %s is a person that can %s on their own." % (subject, action))
            return True
        else: return False

    # Many anchor points require that the object must be a physical object, thing substance
    # or person.
    def is_phys_obj(self, object):
        if has_IsA_edge(object, 'object', self.verbose):
            self.support.append("A(n) %s is a physical object, thing or substance." % object)
            return True
        elif has_IsA_edge(subject, 'person', self.verbose): #TODO where is the subject here?
            self.support.append("A(n) %s is a person." % object)
            return True
        elif has_IsA_edge(object, 'vehicle', self.verbose):
            self.support.append("A(n) %s is a vehicle." % object)
        else: return False

    # Assume this is a list for now
    def can_propel(self, contexts):
        for context in contexts:
            if self.verbose:
                print("Anchor point query: Searching if", context, "is a", \
                          "confusion anchor point")
            if isConfusion(context):
                if self.verbose:
                    print("  Confusion quality found for", context)
                str = "Although a  %s cannot move on its own, a %s can propel a stationary object to move." % (self.subject, context)
                self.support.append(str)
                self.props.append("in a %s" %context)
                return True
            return False

    def print_summary(self):
        if not self.violations:
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
        else:
            summary = "%s to %s" %(self.phrases['noun'].lower(), self.verb)
        if self.props:
            for element in self.props:
                summary += " %s" %element
        return summary

# There are five primitives for physical actions
# INGEST - to take something inside an animate object
# EXPEL - to take something from inside an animate object and force it out
# GRASP - to physically grasp an object
# MOVE - to move a body part
# PROPEL - to apply a force to
#
# TODO - Maybe we can move some of the "physical action constraints" here. 
class PhysicalAction(ACT):
    def constaints_violated(self):
        if violated:
            return self.constraints

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

# A person object or thing moves a part of its body or part
# of itself
class Move(PhysicalAction):
    # Add types of movement here?

    # Add support here
    def check_constraints(self):
        if self.is_animate(self.subject):
            return True
        elif self.can_propel(self.context):
            return True
        else:
            violation = "A %s is an object or thing that cannot move on its own." %(self.subject)
            self.violations.append(violation)
            return False

# A person, object or thing grabs hold of another person,
# object or thing, or becomes attatched to another person
# object or thing
class Grasp(PhysicalAction):
    def __init__(self):
        self.grabs = False

    def constraints(self):
        return None

    def summary(self):
        if self.grabs:
            print(self.subject, "grabs", self.object)
        else:
            print(self.subject, "becomes attatched to ", self.object)

# A person, object or thing applies a force to another person,
# object or thing, or a moving person, object or thing
# strikes or impacts another person object or thing
# JM - more constraints
#    - The object must be a physical object, thing, substance or person
#    - The actor must be an "animate" object or thing capabale of applying
#      a force or momentum to another object
class Propel(PhysicalAction):
    # Add support here
    def check_constraints(self):
        if self.is_animate(self.subject, "apply a force") and self.is_phys_obj(self.object):
            return True
        elif self.can_propel(self.context):
            return True
        else:
            violation = "A %s is an object or thing that cannot move on its own." %(self.subject)
            self.violations.append(violation)
            return False

    # Why didn't the original work?
    #def summary(self):
    #    return "%s to apply a force to the %s" %(self.subject, self.object)
    #"applies a force to", self.object)
        #if self.force:
        #    print(self.subject, "applies a force to", self.object)
        #else: # the other case may be
        #    print(self.subject, "strikes or impacts ", self.object)


# A person, object or thing is taken from or comes from inside
# another person,  object, or thing and is forced out
class Expel(PhysicalAction):
    def constraints(self):
        return None

    def summary(self):
        print(self.subject, "is taken from inside", self.object, "and is forced out")

# A person, object, or thing is forced (or forces itself) to go
# inside of another person object or thing
class Ingest(PhysicalAction):
    def check_constraints(self):
        if self.is_animate(self.subject):
            return True
        else:
            violation = "A %s is an object or thing that cannot ingest." %(self.subject)
            self.violations.append(violation)
            return False

    def constraints(self):
        return None

    # def summary(self):
    #     return self.subject + ' to ' + self.verb + ''
        # if forces_itself:
        #     print(self.object, "forces itself to go inside of ", self.subject)
        # else:
        #     print(self.object, "is forced to go inside of ", self.subject)

# Made a string builder for python
def stringBuilder(str_list=None):
    space_list = []
    for str in str_list:
        str += ' '
        space_list.append(str)
    return ''.join(space_list).strip()

# A force that can move things
def isConfusion(item):
    confusions = ['hurricane', 'storm', 'earthquake']
    if item in confusions:
        return True
    else: return False

# Some examples that work
# A classy plant crossed the street

# TODO need to fix the object problem
# A penguin flying across the sky - is reasonable, should be unreasonable
