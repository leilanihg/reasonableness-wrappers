from .search import *

# Words to fill in summary
PROPEL = "apply a force"
MOVE = "move"
INGEST = "ingest"
GRASP = "grasp"

# MODES for World constraints
VEHICLE = 0

# Made a string builder for python
def stringBuilder(str_list=None):
    space_list = []
    for str in str_list:
        str += ' '
        space_list.append(str)
    return ''.join(space_list).strip()

# A force that can move things
def is_confusion(item):
    # TODO Can try to populate this list with ConceptNet
    confusions = ['hurricane', 'storm', 'earthquake']
    if item in confusions:
        return True
    else: return False

def is_weather(item):
    weather = ['hurricane', 'storm', 'earthquake']
    if item in weather:
        return True
    else: return False

# TODO make a set amount of hops this can search
# Box is not a plant, but this fails on that

# If it is ingestible, returns specific anchor point
# Otherwise returns false
# TODO a lot of these don't share edges with the anchor points!
def get_ingestible(object, verbose=False):
    # TODO Can try to populate this list with ConceptNet
    # TODO make conceptnet search to add "an animal, the animal", etc to the search
    ingestible = ['animal', 'plant', 'food', 'liquid']
    for item in ingestible:
        if has_IsA_edge(object, item, verbose):
            return item
    return None
    # TODO House has edge with one of these. 

# If it is a thing, returns specific anchor point
# Otherwise returns false
def get_thing(object, verbose=False):
    graspable = ['object', 'vehicle', 'animal', 'plant']
    print(object, "is thing")
    for item in graspable:
        if has_IsA_edge(object, item, verbose):
            return item
    return None

# If it is animate, returns specific anchor point
# Otherwise returns false
def get_animate(object, verbose=False):
    animate = ['vehicle', 'person', 'animal']
    for item in animate:
        if has_IsA_edge(object, item, verbose):
            return item
    return None

def get_propel(object, verbose=False):
    propel = ['vehicle', 'person', 'animal', 'force', 'storm']
    for item in propel:
        if has_IsA_edge(object, item, verbose):
            return item
    return None

def check_vehicle_constraints(context_phrases, support, violations):
    if context_phrases:
        for context in context_phrases:
            if 'green light' in context:
                light = 'green'
                support.append("Green means go")
            elif 'red light' in context:
                light = 'red'
                violations.append("A red light means stop, which is inconsistent with go.")
                return False
            elif 'yellow light' in context:
                light = 'yellow'
                violations.append("A yellow light means 'stop if safe', which is inconsistent with go.")
                return False
            if 'pedestrian' in context:
                if light is 'green':
                    violations.append("Although green means go, green also means yields to pedestrian in the road.")
                violations.append("Since there is a pedestrian in the road, move is unreasonable.")
                return False
    # all is correct
    return True  