from modules.Strings import *

def part1(filename):
    with open(filename, "r") as input:
        M=[]
        for line in input:
            line=line.rstrip("\n")
            M.append(line)
    l=len(M[0]) #Length of original schematic
    h=len(M) #Height of original schematic

    #Add '.' frame
    for j in range(h): M[j]='.'+M[j]+'.'
    dot_line=""
    for i in range(l+2): dot_line+='.'
    M.append(dot_line)
    M.insert(0, dot_line)

    g=Grid(M)
    result=0

    #Iterate over each position
    for i in range(1,h+1):
        l=Line(M[i])
        print(M[i])
        #Get all numbers
        numbers=l.get_numbers()

        #Scan all values
        for k in numbers.keys():
            #Check for symbol for each value
            print(k)
            if g.scan_symbol(numbers[k],i): result+=k
    return result

