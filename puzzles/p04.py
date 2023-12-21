from modules.Strings import *

def part1(filename):
    with open(filename, "r") as input:
        result=0
        for line in input:
            C=Card(line)
            D=C.draw_list()
            W=C.win_list()
            count=0
            for i in D:
                if i in W: 
                    count+=1
            if count==0: total=0
            else: total=2**(count-1)
            result=result+total
    return result

