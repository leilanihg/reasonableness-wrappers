from .physical_action import *
from .propel import *
# A person object or thing moves a part of its body or part
# of itself
class Move(PhysicalAction):
    # Add types of movement here?
    def check_constraints(self):
        print("in move")
        constraints = (self.check_subject_constraints() and self.check_object_constraints()
            and self.check_world_constraints()) or self.check_weather_constraints()
        return constraints

    def get_anchor_point(self, subject):
        anchor_point = get_animate(self.subject)
        # TODO change this later
        self.subject_anchor = anchor_point
        if anchor_point == 'vehicle':
            self.world = VEHICLE
        return anchor_point

    # Add support here
    def check_subject_constraints(self):
        anchor_point = self.get_anchor_point(self.subject)

        if anchor_point != None:
            self.add_subject_support(self.subject, anchor_point, MOVE)
            print("subject can move")
            return True
        else:
            self.add_subject_violation(self.subject, MOVE)
            return False

    # TODO, but makes sure it is not weather, even though it should be a propel verb
    def check_object_constraints(self):
        if self.object == None:
            if self.verbose:
                print("there is no object")
            return True

        anchor_point = self.get_anchor_point(self.object)

        if anchor_point != "weather":
            self.add_object_support(self.object, anchor_point, MOVE)
            print("subject can move")
            return True
        else:
            self.add_object_violation(self.object, MOVE)
            return False
        # return (has_any_edge(self.object, self.subject_anchor, verbose=True))
    # TODO Based on the definition of move, the object should share edges with the subject
    # since it is a part of it 

    def check_world_constraints(self):
        if self.world == VEHICLE:
            vehicle = check_vehicle_constraints(self.pp, self.support, self.violations)
            return vehicle
        return True

    def check_weather_constraints(self):
        if self.context == None or len(self.context) == 0:
            return False

        self.support = []
        self.violations = []

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