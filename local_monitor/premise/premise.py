from .relations import *

class Premise:
    """A data structure that stores premises in a meaningful way [hopefully]"""
    def __init__(self, concept, relation, result):
        self.concept = concept
        self.relation = getRelationEnum(relation)
        self.result = result
        # self.reason = 'physcis, ....

    def print_summary(self):
        builder = ''
        builder.join(self.concept).join(' ')
        builder.join(self.relation.value).join(' ')
        builder.join(self.result)
        return "%s%s %s" % (self.concept, self.relation.value, self.result)

# May need a contridction method    
#def print_contradiction(self):
        

# Splits premises into a dictionary by relation
def split_premises(premises):
    relation_dict = {}
    for premise in premises:
        if premise.relation in relation_dict:
            relation_dict[premise.relation].append(premise)
        else:
            relation_dict[premise.relation] = [premise]
    return relation_dict

def main():
    for relation in Relation:
        print(relation)
        print(relation.value)

if __name__ == "__main__":
    main()
