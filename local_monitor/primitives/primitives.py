
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
    def __init__(self, subject, object):
        self.subject = subject
        self.object = object

        self.pp = None #
        # Maybe something about another connection here
    def constaints_violated(self):
        if violated:
            return self.constraints

# There are five primitives for physical actions
# INJEST - to take something inside an animate object
# EXPEL - to take something from inside an animate object and force it out
# GRASP - to physically grasp an object
# MOVE - to move a body part
# PROPEL - to apply a force to 
class PhysicalAction(ACT):

# 2 state changes for physical and abstract transfers
# PRTRANS -  To change the location of a physical object
# ATRANS - To change an abstract relationship of a physical object
class StateChange(ACT):    

# 2 mental acts
# MTRANS - to transfer information mentally
# MBUILD - to create or combine thoughts
class MentalAct(ACT):

# Instrument for other ACT
# To produce a sound
class Speak(ACT):

# Instrument for other ACT
# To direct a sense organ or focus an organ towards a stimulus
class Attend(ACT):

# A person object or thing changes physical position or localion
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
    def constraints(self):
        return None

    

    def summary(self):
        self.summary= ''.join([self.subject, " moves ", self.object])
        return self.summary
        #print(self.subject, "moves", self.object)

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
class Propel(PhysicalAction):
    def constraints(self):
        return None

    def summary(self):
        if self.force:
            print(self.subject, "applies a force to", self.object)
        else: # the other case may be
            print(self.subject, "strikes or impacts ", self.object)
        

# A person, object or thing is taken from or comes from inside
# another person,  object, or thing and is forced out
class Expel(PhysicalAction):
    def constraints(self):
        return None

    def summary(self):
        print(self.subject, "is taken from inside", self.object, "and is forced out")

# A person, object, or thing is forced (or forces itself) to go
# inside of another person object or thing
class Injest(PhysicalAction):
    def constraints(self):
        return None

    def summary(self):
        if forces_itself:
            print(self.object, "forces itself to go inside of ", self.subject)
        else:
            print(self.object, "is forced to go inside of ", self.subject)
    
# Made a string builder for python
def stringBuilder(str_list=None):
    space_list = []
    for str in str_list:
        str += ' '
        space_list.append(str)
    return ''.join(space_list).strip()
