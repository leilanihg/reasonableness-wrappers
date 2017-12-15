# The performer of an ACT
# Actors must be an animate PP or a natural force
class Actor:
    def __init__(self, name):
        self.name = name

# ACTs can have objects
# ACTS can have directions
# ACTs can have recipients
# TODO - may want to have qualitative directions
class ACT:
    def __init__(self, object, direction, recipient):
        self.object = object
        self.direction = direction
        self.recipient = recipient

# A thing that is acted upon
class Object:
    def __init__(self, name, state):
        self.name = name
        self.state = state

class Towards:
    def __init__(self, object)

# Conceptual Dependency Graph
# Want to print:
#                                    |-> TO
#  ACTOR <==> PRIMITIVE <-- OBJECT <-|
#                                    |<- FROM

class ConceptualDependencyGraph:
    def __init__(self, actor, primitive, object):
        self.actor = actor
        self.primitive = primitive
        self.object = object
    
    def display(self):
        if self.to:
            print("                                  |-> TO")
            print(self.actor, "<==>", self.primitive, "<--", self.object, "<-|")
            print("                                  |<- FROM")


