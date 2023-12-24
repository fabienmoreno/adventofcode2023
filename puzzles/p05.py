from modules.Strings import *

def part1(filename):
    with open(filename, "r") as input:
        seeds_raw=input.readline().rstrip("\n")[6:]
        input.readline() #jump first line break
        seeds_dict={int(x):int(x) for x in seeds_raw.split()}

        for line in input:
            if line[0].isalpha(): #Initialise mapping
                M=Map()
            elif line[0].isnumeric(): #Append offset
                mp=[int(x) for x in line.split()]
                M.append(mp[1], mp[1]+mp[2], mp[0]-mp[1])
            else: #Apply conversion
                for s in seeds_dict.keys():
                    seeds_dict[s]=M.convert(seeds_dict[s])

        for s in seeds_dict.keys(): #Apply final conversion
                    seeds_dict[s]=M.convert(seeds_dict[s])

    return min(seeds_dict.values())

def part2(filename):
    with open(filename, "r") as input:
        seeds_raw=input.readline().rstrip("\n")[6:]
        seeds_list=seeds_raw.split()
        seeds_dict={}

        input.readline() #jump first line break
        
        M=GlobalMap()
        level=0
        for line in input:
            if line[0].isalpha(): #Initialise mapping
                M.addlevel(level)
            elif line[0].isnumeric(): #Append offset
                mp=[int(x) for x in line.split()]
                M.append(level, mp[1], mp[1]+mp[2], mp[0]-mp[1])
            else: #Apply conversion
                for s in seeds_dict.keys():
                    seeds_dict[s]=M.convert(level, seeds_dict[s])
                level+=1
        for s in seeds_dict.keys(): #Apply final conversion
                    seeds_dict[s]=M.convert(level, seeds_dict[s])
        
        rmin=float('inf')
        for k,i in enumerate(seeds_list[0::2]):
            m=int(i)
            print(k,m)
            for j in range(m,m+int(seeds_list[1::2][k])):
                r=j
                for l in range(level):
                     r=M.convert(l, r)
                if r < rmin : rmin=r
                #print(j,r, rmin)

    return rmin