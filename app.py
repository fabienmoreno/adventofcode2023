import time
start=time.perf_counter()

from modules.Strings import Line

#Day 1
filename = "data/input_01.txt"
#Only digits
with open(filename, "r") as input:
    total=0
    for line in input:
        l=Line(line.rstrip("\n"))
        total+=l.find_digits()
    print("Total : ", total)

print("Delay :", (time.perf_counter()-start)*1000, " ms")

#Digits & word
filename = "data/input_01.txt"
S=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
Sdir = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
D=[str(x) for x in range(1,10)]
W=S+D
with open(filename, "r") as input:
    total=0
    for line in input:
        l=Line(line.rstrip("\n"))
        first = l.find_words(W,0,1)[1]
        if first in S: first=Sdir[first]
        last = l.find_words(W,0,-1)[1]
        if last in S: last=Sdir[last]
        first_last=first + last
        total+=int(first_last)
    print("Total : ", total)

print("Delay :", (time.perf_counter()-start)*1000, " ms")


'''
l.first.digit.position()
l.first.digit.value()
l.first.word([List of spelled]).position()
l.first.word([List of spelled]).value()
l.find(digits=True,words=[List],direction=1).position()
l.first.find(digits=True,words=[List]).value()
idem pour last
'''