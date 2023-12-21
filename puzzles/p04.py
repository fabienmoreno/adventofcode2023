from modules.Strings import *

def part1(filename):
    with open(filename, "r") as input:
        result=0
        for line in input:
            C=Card(line)
            result=result+C.match_score()
    return result

