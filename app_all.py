import time
from puzzles import *

#Day 1 - Part 1
start=time.perf_counter()
filename = "data/input_01.txt"
result=p01.part1(filename)
print("Result Day 01 / Part 1 : ", result, " Duration : ", (time.perf_counter()-start)*1000, " ms")

#Day 1 - Part 2
start=time.perf_counter()
result=p01.part2(filename)
print("Result Day 01 / Part 2 : ", result, " Duration : ", (time.perf_counter()-start)*1000, " ms")