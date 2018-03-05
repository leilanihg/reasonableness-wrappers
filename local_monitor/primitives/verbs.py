from .search import *
from .primitives import *

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
def is_action_verb(verb, verbose):
    if(has_any_edge(verb, 'move', verbose)):
        return True
    elif(has_any_edge(verb, 'action', verbose)):
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
# Performing specific taks
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
def is_communication_verb(verb,verbose):
    return has_any_edge(verb, 'communicate', verbose)

# kick hit
def is_propel_verb(verb, verbose):
    return has_any_edge(verb, 'hit', verbose)

def is_ingest_verb(verb, verbose):
    if has_any_edge(verb, 'eat', verbose) or has_any_edge(verb, 'ingest', verbose):
        return True
    return False 

# Use not any edge, and instead count the hops so that we can use the closest verb
# Just added
# TODO - add IsA and \HasA
def get_verb_type(base, subject, object, context, phrases, verbose=False):
    if is_ingest_verb(base, verbose):
        if verbose:
            print("INGEST verb primitive created.")
        return Ingest(subject, base, object, context, phrases, verbose)

    if is_communication_verb(base, verbose):
        if verbose:
            print("SPEAK verb primitive created.")
        return Speak(subject, base, object, context, phrases, verbose)
    elif is_propel_verb(base, verbose):
        if verbose:
            print("PROPEL verb primitive created.")
        return Propel(subject, base, object, context, phrases, verbose)
    elif is_action_verb(base, verbose):
        if verbose:
            print("MOVE verb primitive created.")
        return Move(subject, base, object, context, phrases, verbose)
    else:
        raise ValueError("don't know how to handle verb {0}".format(base))
