from modules.Strings import *

def part1(filename):
    with open(filename, "r") as input:
        result=0
        for line in input:
            C=Card(line)
            D=C.draw_list()
            W=C.win_list()
            count=0
            L=[]
            for i in D:
                if i in W: 
                    count+=1
                    L.append(i)
            if count==0: total=0
            else: total=2**(count-1)
            #print(C.number(), total, L)
            result=result+total
    return result

"""
Card 211: 26 70 22 97 55 51 41 29 61 78 | 
          12 15 84 16  3 38  2 43 66 24 10 71 48 45 53  1 13 23 69 35 74 40  5 77 52"""