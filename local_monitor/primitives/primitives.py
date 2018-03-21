from .primitives_helper import *

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
    def check_constraints(self):
        constraints = (self.check_subject_constraints()
            and self.check_world_constraints()) or self.check_weather_constraints()
        print("constraints", constraints)
        return constraints

    def get_anchor_point(self, subject):
        anchor_point = get_animate(self.subject)
        # TODO change this later
        self.subject_anchor = anchor_point
        if anchor_point == 'vehicle':
            self.world = VEHICLE
        return anchor_point

    # Add support here
    def check_subject_constraints(self):
        anchor_point = self.get_anchor_point(self.subject)

        if anchor_point != None:
            self.add_subject_support(self.subject, anchor_point, MOVE)
            print("subject can move")
            return True
        else:
            self.add_subject_violation(self.subject, MOVE)
            return False

    # TODO Based on the definition of move, the object should share edges with the subject
    # since it is a part of it 
    def check_object_constraints(self):
        if self.object == None:
            if self.verbose:
                print("there is no object")
            return True

        return (has_any_edge(self.object, self.subject_anchor, verbose=True))

    def check_world_constraints(self):
        if self.world == VEHICLE:
            vehicle = check_vehicle_constraints(self.pp, self.support, self.violations)
            return vehicle
        return True

    def check_weather_constraints(self):
        if self.context == None:
            return False

        self.support = []
        self.violations = []

        for context in self.context:
            if is_weather(context):
                # make copy of context list and remove context
                contexts_copy = self.context.copy()
                contexts_copy.remove(context)

                # Propel has other constraints, so we need to make a Propel object and check that
                # Change sentence structure so context is subject, and verb type is propel
                if self.verbose:
                    print("PROPEL verb primitive created.")
                newPrimitive = Propel(subject=context, verb=self.verb, object=self.object, 
                    context=contexts_copy, phrases=self.phrases, verbose=self.verbose)
                reasonable = newPrimitive.check_constraints()
                if reasonable:
                    self.support.append("Although a %s cannot move on its own, it can be propeled by a %s."%(self.subject, context))
                    return reasonable
        print("Weather constraint is false")
        return False
# A person, object or thing grabs hold of another person,
# object or thing, or becomes attatched to another person
# object or thing
class Grasp(PhysicalAction):
    def __init__(self):
        self.grabs = False
    
    def check_constraints(self):
        return self.check_subject_constraints() and self.check_object_constraints()

    # Add support here
    def check_subject_constraints(self):
        anchor_point = get_animate(self.subject)
        if anchor_point != None:
            self.add_subject_support(self.subject, anchor_point, GRASP)
            return True
        else:
            self.add_subject_violation(self.subject, GRASP)
            return False

    # very naive check
    # beginning of adding in object constraints
    def check_object_constraints(self):
        if self.object == None:
            return True
        print("called object constraint")
        anchor_point = get_graspable(self.object, self.verbose)
        if anchor_point != None:
            self.add_object_support(self.object, anchor_point, GRASP) 
            return True
        else:
            violation = "A %s is not graspable." %(self.object)
            self.violations.append(violation)
            return False


    # def summary(self):
    #     if self.grabs:
    #         print(self.subject, "grabs", self.object)
    #     else:
    #         print(self.subject, "becomes attatched to ", self.object)

# A person, object or thing applies a force to another person,
# object or thing, or a moving person, object or thing
# strikes or impacts another person object or thing
# JM - more constraints
#    - The object must be a physical object, thing, substance or person
#    - The actor must be an "animate" object or thing capabale of applying
#      a force or momentum to another object
# TODO why is phys_object necessary for propel? 
class Propel(PhysicalAction):
    # TODO change name to be check_subject_constraints    
    def check_constraints(self):
        return self.check_subject_constraints() and self.check_object_constraints()

    def check_subject_constraints(self):
        anchor_point = get_propel(self.subject, self.verbose)
        if anchor_point != None:
            self.add_subject_support(self.subject, anchor_point, PROPEL)
            return True
        else:
            violation = "A %s is an object or thing that cannot move on its own." %(self.subject)
            self.violations.append(violation)
            return False

    def check_object_constraints(self):
        if self.object == None:
            return True
        if not is_confusion(self.object): 
            self.add_object_support(self.object, 'item', PROPEL)
            return True
        else:
            violation = "A %s cannot be propeled" %(self.object)
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
    def check_constraints(self):
        return None

    def summary(self):
        print(self.subject, "is taken from inside", self.object, "and is forced out")

# A person, object, or thing is forced (or forces itself) to go
# inside of another person object or thing
class Ingest(PhysicalAction):
    def check_constraints(self):
        return self.check_subject_constraints() and self.check_object_constraints()

    def check_subject_constraints(self):
        anchor_point = get_animate(self.subject, self.verbose)
        if anchor_point != None:
            self.add_subject_support(self.subject, anchor_point, INGEST)
            return True
        else:
            # violation = "A %s is an object or thing that cannot ingest." %(self.subject)
            # self.violations.append(violation)
            self.add_subject_violation(self.subject, INGEST)
            return False

    # very naive check
    # beginning of adding in object constraints
    def check_object_constraints(self):
        if self.object == None:
            return True
        print("called object constraint")
        anchor_point = get_animate(self.object, self.verbose)
        if anchor_point != None: 
            self.add_object_support(self.object, anchor_point, "ingest")
            return True
        else:
            violation = "A %s is not a plant, animal, or liquid and therefore cannot be ingested" %(self.object)
            self.violations.append(violation)
            # TODO add a list of things that it cant be
            return False

# A specific vehicle type primitive
# TODO we should separate this out but make it so that it connects rather than is another primitive.
class Go(Move):
    def check_constraints(self):
        consistent = False
        if self.pp:
            for context in self.pp:
                if 'green light' in context:
                    self.light = 'green'
                    self.support.append("Green means go")
                    consistent = True
                elif 'red light' in context:
                    self.light = 'red'
                    self.violations.append("A red light means stop, which is inconsistent with go.")
                    consistent = False
                elif 'yellow light' in context:
                    self.light = 'yellow'
                    self.violations.append("A yellow light means 'stop if safe', which is inconsistent with go.")
                    consistent = False
                if 'pedestrian' in context:
                    if self.light is 'green':
                        self.violations.append("Although green means go, green also means yields to pedestrian in the road.")
                    self.violations.append("Since there is a pedestrian in the road, move is unreasonable.")
                    consistent = False
        return consistent 

    def check_subject_constraints(self):
        return False

# Another specific vehicle type primitive
class Wait(Move):
    def check_constraints(self):
        consistent = False
        if self.pp:
            for context in self.pp:
                if 'green light' in context:
                    self.light = 'green'
                    self.violations.append("A green light means go, which is inconsistent with waiting.")
                    consistent = False
                elif 'red light' in context:
                    self.light = 'red'
                    self.support.append("A red light means stop.")
                    consistent = True
                elif 'yellow light' in context:
                    self.light = 'yellow'
                    self.support.append("A yellow light means 'stop if safe'.  So waiting is reasonable")
                    consistent = True
                if 'pedestrian' in context:
                    if self.light is 'green':
                        self.support.append("Although green means go, green also means yields to pedestiran in the road.")
                    self.support.append("Since there is a pedestrian in the road, waiting is reasonable.")
                    consistent = True
        print("consistent is", consistent)
        return consistent 

    def check_subject_constraints(self):
        return False

# Another specific vehicle type primitive
class Yield(Move):
    def check_constraints(self):
        return False

    def check_subject_constraints(self):
        return False


# TODO change MOVE to be itself or body, and use PROPEL instead ("a man moves a hurricane", should be propel)
# Some examples that work
# A classy plant crossed the street

# TODO need to fix the object problem
# A penguin flying across the sky - is reasonable, should be unreasonable
