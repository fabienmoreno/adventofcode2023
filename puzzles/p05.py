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