from explain import *
from local_monitor import *

def relation_conflict(relations):
    for rel_1 in relations:
        for rel_2 in relations:
            if not has_any_edge(rel_1, rel_1):
                print(rel_1, "not close to ", rel_2)
