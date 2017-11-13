# Used to printint to sderr
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def find_IsA_path(start, end, path=None, queue=None, seen=None):
    if path is None:
        path = []
        path.append(clean_search(start))

    if queue is None:
        queue = []

    if seen is None:
        seen = []
        
    search = clean_search(start)
    if(debug):
        eprint("Now searching through the IsA hiearchy for", search, path)
        eprint("We've seen", seen)
    obj = requests.get(query_prefix+search+'?rel=/r/IsA&limit=1000').json()
    edges = obj['edges']
    
    if(has_IsA_edge(start,end)):
        if(debug):
            eprint("Found an edge between", start, "and", end)
        path.append(end)
        return path
    else:
        new_queue = []
        if(start not in seen): # Might need more preprocessing
            for edge in edges:
                from_node = clean_search(edge['start']['label'])
                to_node = clean_search(edge['end']['label'])
                rel = edge['rel']['label']
                # May need more processing
                if(search_equals(from_node, search) and rel == 'IsA'): # make sure its the right way
                    node = (to_node, len(path))
                    if node not in queue and node not in new_queue and \
                            not search_equals(node[0], start):
                        new_queue.append(node)
                        if len(new_queue) >=10:
                            break
            seen.append(start)
        merged_queue = []
        merged_queue.extend(new_queue)
        merged_queue.extend(queue)
        if debug: 
            eprint("new queue is ", merged_queue)
        if merged_queue:
            node = merged_queue.pop(0)[0]
            if node not in path:
                if(len(path) < limit-1 ):
                    if(debug): eprint("recursing with ", node)
                    path.append(node)
                    newpath = find_IsA_path(node, end, path, merged_queue, seen)
                    return newpath
                else: # we've gone too far
                    if not (containsConcept(end, merged_queue)):
                        if(debug): eprint("We've gone too far")
                        path.pop()
                        node=path[-1]
                        newpath = find_IsA_path(node, end, path, 
                                                [(x,y) for (x,y) in merged_queue if y != 2],
                                                seen)
                        return newpath
                    else: 
                        path.append(end)
                        return path
    return None

def search_equals(string1, string2):
    if(clean_search(string1) == clean_search(string2)):
        return True
    return False

def clean_search(input):
    cleaned = input.lower()
    if(cleaned.startswith("a ")):
        cleaned = cleaned.replace("a ", "", 1)
    elif(cleaned.startswith("an ")):
        cleaned = cleaned.replace("an ", "", 1)           
    return cleaned.replace(" ", "_").lower()