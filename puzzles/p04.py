from modules.Strings import *

def part1(filename):
    with open(filename, "r") as input:
        result=0
        for line in input:
            C=Card(line)
            result=result+C.match_score("score")
    return result

def part2(filename):
    T={}
    with open(filename, "r") as input:
        D={}
        for line in input:
            C=Card(line)
            D[C.number()]=C.match_score("qty")
            T[C.number()]=1
    
    for i in D.keys():
        if D[i]==0: pass
        else: 
            for k in range(i+1, i+1+D[i]):
                T[k]+=T[i]
    #print(T)
    result=sum(T.values())
    return result