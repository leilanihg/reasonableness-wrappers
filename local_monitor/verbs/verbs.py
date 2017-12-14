from ..conceptnet.search import *

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
def is_action_verb(verb):
    if(has_any_edge(verb, 'move')):
        return True
    elif(has_any_edge(verb, 'action')):
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
# Performing specific takss
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
def is_communication_verb(word):
    toTalk = ['talk', 'talks', 'talked', 'talking']
    verb = word #WordNetLemmatizer().lemmatize(word,'v')
    return has_any_edge(verb, 'communicate')   