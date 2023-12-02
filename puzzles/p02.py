from modules.Strings import *

def part1(filename):
    with open(filename, "r") as input:
        total=0
        max_color={'green': 13, 'blue': 14, 'red': 12}
        for line in input:
            g=Game(line)
            c_dict=g.build_color_dict()
            check=True
            for c in max_color.keys():
                if max_color[c]<max(c_dict[c]):
                    check=False
                    break
            if check: total+=g.game_number
    return total

