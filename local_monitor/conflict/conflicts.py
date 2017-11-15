from ..conceptnet.explain import *
from ..conceptnet.search import *

# def relation_conflict(relations):
#     for rel_1 in relations:
#         for rel_2 in relations:
#             if not has_any_edge(rel_1, rel_1):
#                 print(rel_1, "not close to ", rel_2)

# Only returns one conflict as of now
def relation_conflict(rel):
    conflicts = []
    for key,premises in rel.items():
        for premise1 in premises:
            for premise2 in premises:
                if isinstance(premise1.result, str) and isinstance(premise2.result, str):
                    if not premise1.concept == premise2.concept and not has_any_edge(premise1.result, premise2.result):
                        conflicts.append((premise1, premise2))
                # This is for verbs
                elif isinstance(premise1.result, bool) and isinstance(premise2.result, bool): 
                    if not premise1.result == premise2.result:
                        conflicts.append((premise1, premise2))
    return conflicts

def explain_relation_conflict(relations):
    print("THE INPUT STATEMEMENT IS UNREASONABLE")
    print("  Using data from ConceptNet5")
    for rel in relations:
        [rel1, rel2] = rel
        print(rel1.print_summary(), "not close to ",rel2.print_summary())