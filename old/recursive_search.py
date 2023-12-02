import time
start=time.perf_counter()


S=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
graph_dict={}

def build_dict(sub_dict, word):
    if len(word)==2:
        sub_dict[word[0]]=word[1]
    else:
        if word[0] not in sub_dict.keys(): sub_dict[word[0]]={}
        sub_dict[word[0]]=build_dict(sub_dict[word[0]],word[1:])
    return sub_dict

for w in S:
    graph_dict=build_dict(graph_dict,w)

print("Duration : ", (time.perf_counter()-start)*1000, " ms")

R="khgdlljfxjt6sehvenfour35pxohne"

def search_graph(sub_dict, text):
    if len(text)==0: return False
    if type(sub_dict)==str:
        if text[0]==sub_dict: return True
        else: return False
    elif type(sub_dict)==dict:
        if text[0] in sub_dict.keys() and search_graph(sub_dict[text[0]],text[1:]):
            return True
        else: return False

def xsearch(sub_dict, text):
    check=False
    for i in range(len(R)):
        if search_graph(graph_dict,R[i:]):
            check=True
            break
    return (check,i)

print(xsearch(graph_dict, R))