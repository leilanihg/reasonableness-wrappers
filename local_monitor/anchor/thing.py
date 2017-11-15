class LivingThing:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

        def summary(self):
            return self.name + " is a living thing that lives in " + self.habitata

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Object:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Furniture(Object):
    def __init__(self, name, location):
        Object.__init__(name, location)

class Confusion():
    def __init__(self, name, condition):
        self.name = name
        self.condition = condition

class Weather(Confusion):
    def __init__(self, name, condition):
        Confusion.__init__(name, condition)

class Animal(LivingThing):
    def __init_(self, name, habitat, eats, enemies):
        LivingThing.__init__(self, name, habitat)
        self.eats = eats
        self.enemies = enemies

class Plant(LivingThing):
    def __init__(self, name, habitat):
        LivingThing.__init__(self, name, habitat)

class Person(Animal):
    def __init__(self, name, habitat, eats, enemies):
        Animal.__init__(self, name, habitat, eats, enemies)

# Verb things
class Action():
    def __init__(self, name):
        self.name = name

# To be, become seem
# Connects the subject of a sentence to a noun or adjective 
class Linking():
    def __init__(self, name):
        self.name = name

# Used before action or linking verbs to convey additional info
# Possibility - Can, could, etc
# Time - Was, did, has, etc.
# The main verb with its accompanying helping verb is called a verb phrase
class Helping():
    def __init__(self, name):
        self.name = name

# Action words express actions 
# Give, eat, walk, etc. 
class ExpressAction(Action):
    def __init__(self, name):
        Action.__init__(self, name)

# Actions verbs express action or possession
# Have own, etc.  
class Possession(Action):
    def __init__(self, name):
        Action.__init__(self, name)

class Communication():
    def __init__(self, name):
        self.name = name

class SVO:
    def __init__(self, subject, verb, object):
        self.subject = subject
        self.verb = verb
        self.object = object

    def __str__(self):
        return "%s %s %s" % (self.subject, self.verb, self.object)

