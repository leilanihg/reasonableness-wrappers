import unittest
from .test import *
from ...primitives.verbs import *

class TestIsActionVerb(unittest.TestCase):
    def runTest(self):
        self.assertEqual(is_action_verb('run'), True)
        #self.assertEqual(is_action_verb('talk'), False)
        self.assertEqual(is_action_verb('cross'), True)
        self.assertEqual(is_action_verb('is'), False)
        self.assertEqual(is_action_verb('raise'), True)
        self.assertEqual(is_action_verb('give'), True)

        self.assertEqual(is_action_verb('has'), False)
        self.assertEqual(is_action_verb('thinking'), False)
        # Add talk and stuff

# TODO - Next step
class TestFindLinkingVerb(unittest.TestCase):
    def runTest(self):
        self.assertEqual(is_linking_verb('is'), True)
        self.assertEqual(is_linking_verb('appearing'), True)
        self.assertEqual(is_linking_verb('smelled'), True)

        self.assertEqual(is_linking_verb('move'), False)
        self.assertEqual(is_linking_verb(''), False)
        self.assertEqual(is_linking_verb('dance'), False)

class TestFindHelpingVerb(unittest.TestCase):
    def runTest(self):
        self.assertEqual(is_helping_verb('is'), True)
        self.assertEqual(is_helping_verb('should'), True)
        self.assertEqual(is_helping_verb('have'), True)

        self.assertEqual(is_helping_verb('move'), False)
        self.assertEqual(is_helping_verb(''), False)
        self.assertEqual(is_helping_verb('smell'), False)

class TestIsPossessionVerb(unittest.TestCase):
    def runTest(self):
        self.assertEqual(is_possession_verb('is'), False)
        self.assertEqual(is_possession_verb('should'), False)
        self.assertEqual(is_possession_verb('have'), True)

        self.assertEqual(is_possession_verb('move'), False)
        self.assertEqual(is_possession_verb(''), False)
        self.assertEqual(is_possession_verb('smell'), False)

        self.assertEqual(is_possession_verb('have'), True)
        self.assertEqual(is_possession_verb('bought'), True)
        self.assertEqual(is_possession_verb('possess'), True)
        self.assertEqual(is_possession_verb('providing'), True)

class TestIsCommunicationVerb(unittest.TestCase):
    @ignore_warnings
    def runTest(self):
        self.assertEqual(is_communication_verb('is'), False)
        self.assertEqual(is_communication_verb('should'), False)
        self.assertEqual(is_communication_verb('have'), False)

        self.assertEqual(is_communication_verb('move'), False)
        self.assertEqual(is_communication_verb(''), False)
        self.assertEqual(is_communication_verb('smell'), False)

        self.assertEqual(is_communication_verb('talk'), True)
        self.assertEqual(is_communication_verb('told'), True)
        self.assertEqual(is_communication_verb('tell'), True)
        self.assertEqual(is_communication_verb('said'), True)
        self.assertEqual(is_communication_verb('talked'), True)


class TestVerbType(unittest.TestCase):
    @ignore_warnings
    def runTest(self):
        self.assertEqual(find_verb_type('is'), 'linking')
        self.assertEqual(find_verb_type('should'), 'helping')
        self.assertEqual(find_verb_type('have'), 'helping')

        self.assertEqual(find_verb_type('move'), 'action')
        self.assertEqual(find_verb_type(''), 'preposition')
        self.assertEqual(find_verb_type('smell'), 'linking')

        self.assertEqual(find_verb_type('talk'), 'communication')
        self.assertEqual(find_verb_type('told'), 'communication')
        self.assertEqual(find_verb_type('tell'), 'communication')
        self.assertEqual(find_verb_type('said'), 'communication')
        self.assertEqual(find_verb_type('talked'), 'communication')