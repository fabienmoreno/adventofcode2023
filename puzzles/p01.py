from modules.Strings import *

#Only find digits
def part1(filename):
    with open(filename, "r") as input:
        total=0
        for line in input:
            l=Line(line)
            total+=l.find_digits()
    return total

#Find any string in the line
def part2(filename):
    D=[str(x) for x in range(1,10)]
    S=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    Sdir = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    W=S+D

    #Choose de searching method:
    method = "Recursive" #ou "Find"

    if method=="Recursive" :
        Wr=[w[::-1] for w in W]

        #Génération du dictionnaire représentant un graph
        def build_dict(sub_dict, word):
            if len(word)==1:
                if word in sub_dict.keys():
                    sub_dict[word][None]=None
                else: sub_dict[word]={None:None}
            else:
                if word[0] not in sub_dict.keys(): sub_dict[word[0]]={}
                sub_dict[word[0]]=build_dict(sub_dict[word[0]],word[1:])
            return sub_dict
        
        graph_dict={}
        for w in W:
            graph_dict=build_dict(graph_dict,w)
        graph_dictr={}
        for w in Wr:
            graph_dictr=build_dict(graph_dictr,w)

        with open(filename, "r") as input:
            total=0
            for line in input:
                l=Line(line)
                first = l.find_wordsr(graph_dict,1)[1]
                if first in S: first=Sdir[first]

                last = l.find_wordsr(graph_dictr,-1)[1]
                if last in S: last=Sdir[last]

                first_last=first + last
                total+=int(first_last)
    
    elif method=="Find":
        with open(filename, "r") as input:
            total=0
            for line in input:
                l=Line(line)
                first = l.find_words(W,1)[1]
                if first in S: first=Sdir[first]

                last = l.find_words(W,-1)[1]
                if last in S: last=Sdir[last]

                first_last=first + last
                total+=int(first_last)
    return total