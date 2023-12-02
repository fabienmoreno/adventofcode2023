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
    with open(filename, "r") as input:
        total=0
        for line in input:
            l=Line(line)
            first = l.find_words2(W,1)[1]
            if first in S: first=Sdir[first]
            last = l.find_words(W,-1)[1]
            if last in S: last=Sdir[last]
            first_last=first + last
            total+=int(first_last)
    return total