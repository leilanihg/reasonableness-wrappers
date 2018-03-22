from .physical_action import *

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
