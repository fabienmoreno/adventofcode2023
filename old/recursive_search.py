import time
start=time.perf_counter()


S=["one", "two", "se", "three", "four", "five", "six", "seven", "eight", "nine", "5"]
graph_dict={}

def build_dict(sub_dict, word):
    if len(word)==1:
        if word in sub_dict.keys():
            sub_dict[word][None]=None
        else: sub_dict[word]={None:None}
    else:
        if word[0] not in sub_dict.keys(): sub_dict[word[0]]={}
        sub_dict[word[0]]=build_dict(sub_dict[word[0]],word[1:])
    return sub_dict

for w in S:
    graph_dict=build_dict(graph_dict,w)

print(graph_dict)

print("Duration : ", (time.perf_counter()-start)*1000, " ms")

R="khgdsfurzsfour"

def search_graph(sub_dict, text):
    global C
    #if len(text)==0: return False
    if None in sub_dict.keys():
        if sub_dict[None]==None: return True
    else:
        if text[0] in sub_dict.keys() and search_graph(sub_dict[text[0]],text[1:]):
            print(text[0])
            C=text[0]+C
            return True
        else: return False

def xsearch(sub_dict, text):
    global C
    C=""
    check=False
    for i in range(len(R)):
        if search_graph(graph_dict,R[i:]):
            check=True
            break
    return (check,i)

print(xsearch(graph_dict, R),C)

exit(0)

{
    'o': {'n': {'e': {None: None}}}, 
    't': {'w': {'o': {None: None}}, 'h': {'r': {'e': {'e': {None: None}}}}}, 
    '3': {None: None}, 
    'f': {'o': {'u': {'r': {None: None}}}, 'i': {'v': {'e': {None: None}}}}, 
    's': {'i': {'x': {None: None}}, 'e': {'v': {'e': {'n': {None: None}}}, None: None}}, 
    'e': {'i': {'g': {'h': {'t': {None: None}}}}}, 
    'n': {'i': {'n': {'e': {None: None}}}}
    }
def search_graph_old(sub_dict, text):
    global C
    if len(text)==0: return False
    if type(sub_dict)==str:
        if text[0]==sub_dict:
            print(text[0]) 
            C+=text[0]
            return True
        else: return False
    elif type(sub_dict)==dict:
        if text[0] in sub_dict.keys() and search_graph(sub_dict[text[0]],text[1:]):
            print(text[0])
            C+=text[0] 
            return True
        else: return False

