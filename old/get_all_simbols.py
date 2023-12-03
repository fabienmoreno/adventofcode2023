S=set()
filename="data/input_03.txt"

with open(filename, "r") as input:
    for line in input:
        line=line.rstrip("\n")
        for i in line:
            S.add(i)

print(S)