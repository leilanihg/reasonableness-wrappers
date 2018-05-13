from .physical_action import *

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
        print("in Propel")
        subject_constraints = self.check_subject_constraints()
        object_constraints = self.check_object_constraints()
        if not (subject_constraints):
            return self.check_weather_constraints() and object_constraints
        else:
            return subject_constraints and object_constraints

    def get_anchor_point(self, subject):
        anchor_point = get_propel(self.subject)
        print("anchor point:", anchor_point)
        # TODO change this later
        self.subject_anchor = anchor_point
        if anchor_point == 'vehicle':
            self.world = VEHICLE
        return anchor_point

    def check_subject_constraints(self):
        anchor_point = self.get_anchor_point(self.subject)
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
        if not is_weather(self.object): 
            self.add_object_support(self.object, 'item', "propel")
            return True
        else:
            violation = "A %s cannot be propeled" %(self.object)
            self.violations.append(violation)
            return False

    def check_weather_constraints(self):
        if self.context == None:
            return False

        # self.support = []
        # self.violations = []

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