import requests
from nltk.corpus import stopwords

def split_caption(caption):
    stops = set(stopwords.words("english"))
    tokens = caption.split()
    filtered_words = [word for word in tokens if word not in stops]
    # maybe we want to map stop words to something meaningful
    # in - location
    # in - time
    return filtered_words

def get_base(word):
    obj=requests.get('http://api.conceptnet.io/c/en/'+word).json()
    edges = obj['edges']
    for edge in edges:
        print(edge['surfaceText'])
    # types of _
    # _ is a type of ....
    # context of this term
    #for key in keys:
        #print(obj[key])

# Returns true if there are no edges between words
def not_related(word1, word2):
    obj=requests.get('http://api.conceptnet.io/query?node=/c/en/'+word1+'&other=/c/en/'+word2).json()
    edges = obj['edges']
    if(not edges):
        print(word1+" is not related to "+word2)
        explain_non_relation(word1, word2)
        return True
    else:
        print(word1+" is related to "+word2)
        explain_relation(word1, word2)
        return False

# Propagate through conceptNet to find why they are related
def explain_relation(word1, word2):
    obj=requests.get('http://api.conceptnet.io/query?node=/c/en/'+word1+'&other=/c/en/'+word2).json()
    edges = obj['edges']
    for edge in edges:
        print(edge)
    return 

# Propagate through contextNet to find a contradiction
def explain_non_relation(word1, word2):
    return

def main():
    print(not_related("penguin", "bamboo"))
    tokens = split_caption('penguin in july')
    for word in tokens:
        get_base(word)
    print(tokens)

if __name__ == "__main__":
    #main()
    print (not_related("gorilla", "bamboo"))
    print(not_related("penguin", "bamboo"))
    print(not_related("penguin", "kosher"))
    print(not_related("cheese", "kosher"))
    print(not_related("corn", "kosher"))
    print(not_related("penguin", "bird"))
    get_base("penguin")
