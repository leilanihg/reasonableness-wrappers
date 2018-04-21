from .physical_action import *
from ..anchors import *


# A person, object, or thing is forced (or forces itself) to go
# inside of another person object or thing
class Ingest(PhysicalAction):
    def check_constraints(self):
        return self.check_subject_constraints() and self.check_object_constraints()

    def check_subject_constraints(self):
        self.subject_anchor = get_can_ingest(self.subject, self.verbose)
        if self.subject_anchor != None:
            self.add_subject_support(self.subject, self.subject_anchor, INGEST)
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
        if self.subject_anchor == 'person' or self.subject_anchor =='animal':
            anchor_point = get_animate_ingestible(self.object, self.verbose)
            if anchor_point != None:
                self.add_object_support(self.object, anchor_point, "ingest")
                return True
            else:
                violation = "A %s is not a plant, animal, or liquid and therefore cannot be ingested" %(self.object)
                self.violations.append(violation)
            # TODO add a list of things that it cant be
                return False
        if self.subject_anchor == 'vehicle':
            anchor_point = get_vehicle_ingestible(self.object, self.verbose)
            if anchor_point != None:
                self.add_object_support(self.object, anchor_point, "ingest")
                return True
            else:
                violation = "A %s is not oil or gas and therefore cannot be ingested" %(self.object)
                self.violations.append(violation)
                # TODO add a list of things that it cant be
                return False
        if self.subject_anchor == 'plant':
            anchor_point = get_plant_ingestible(self.object, self.verbose)
            if anchor_point != None:
                self.add_object_support(self.object, anchor_point, "ingest")
                return True
            else:
                violation = "A %s is not water or plant food and therefore cannot be ingested" %(self.object)
                self.violations.append(violation)
                # TODO add a list of things that it cant be
                return False

        if self.subject_anchor == 'hurricane' or self.subject_anchor == 'tornado':
            if not is_weather(self.object):
                self.add_object_support(self.object, 'thing', "ingest")
                return True
            else:
                violation = "A %s is a type of weather and cannot be ingested" %(self.object)
                self.violations.append(violation)

        return False

# ingest and expel depends on subject anchor

def get_animate_ingestible(object, verbose=False):
    # TODO Can try to populate this list with ConceptNet
    # TODO make conceptnet search to add "an animal, the animal", etc to the search
    ingestible = ['animal', 'plant', 'food', 'liquid']
    for item in ingestible:
        if has_IsA_edge(object, item, verbose):
            return item
    return None
    # TODO House has edge with one of these.

def get_plant_ingestible(object, verbose=False):
    # TODO Can try to populate this list with ConceptNet
    # TODO make conceptnet search to add "an animal, the animal", etc to the search
    ingestible = ['water', 'plant food', 'rain']
    for item in ingestible:
        if has_IsA_edge(object, item, verbose):
            return item
    return None

def get_vehicle_ingestible(object, verbose=False):
    # TODO Can try to populate this list with ConceptNet
    # TODO make conceptnet search to add "an animal, the animal", etc to the search
    ingestible = ['oil', 'gas']
    for item in ingestible:
        if has_IsA_edge(object, item, verbose):
            return item
    return None

def get_can_ingest(object, verbose=False):
    animate = ['vehicle', 'person', 'animal', 'hurricane', 'tornado', 'plant']
    for item in animate:
        if has_IsA_edge(object, item, verbose):
            return item
    return None