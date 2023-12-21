class Line :
    def __init__(self, string) -> None:
        self.string=string.rstrip("\n")
        self.first=string[0]
    
    def find_digits(self):
        first=""
        last=""
        for i in self.string:
            j=ord(i) #ASCII conversion for fun
            if j>=48 and j<=57:
                first=i
                break
        for i in self.string[::-1]:
            j=ord(i) #ASCII conversion for fun
            if j>=48 and j<=57:
                last=i
                break
        first_last=first + last
        try:
            first_last_number=int(first_last)
            return first_last_number
        except:
            print("Error on : ", self.string)

    def find_first_number(self):
        number_str=""
        for i in self.string:
            j=ord(i)
            if j>=48 and j<=57:
                number_str+=i
            elif number_str!="" and j<48 and j>57:
                break
        try: 
            number=int(number_str)
            return number
        except:
            raise Exception("No number found")

    def find_words(self, words, direction):
        text=self.string[0::1]
        if direction == 1:
            min=len(text)+1
            wmin=""
            for w in words:
                try:
                    j=text.index(w)
                    if j<min: 
                        min=j
                        wmin=w
                except:
                    pass
            if wmin!="": return (min,wmin)
            else: return (-1,"")
        if direction == -1:
            max=-1
            wmax=""
            for w in words:
                try:
                    j=text.rindex(w)
                    if j>max: 
                        max=j
                        wmax=w
                except:
                    pass
            if wmax!="": return (max,wmax)
            else: return (-1,"")

    def find_words2(self, words, direction):
        text=self.string[0::direction]
        if direction==-1:
            words=[w[::-1] for w in words]

        #Génération du dictionnaire représentant un graph
        def build_dict(sub_dict, word):
            if len(word)==1:
                if word in sub_dict.keys():
                    sub_dict[word][None]=None
                else: sub_dict[word]={None:None}
            else:
                if word[0] not in sub_dict.keys(): sub_dict[word[0]]={}
                sub_dict[word[0]]=build_dict(sub_dict[word[0]],word[1:])
            return sub_dict
        
        graph_dict={}
        for w in words:
            graph_dict=build_dict(graph_dict,w)

        def search_graph(sub_dict, text):
            global C
            if None in sub_dict.keys():
                if sub_dict[None]==None: return True
            else:
                if text[0] in sub_dict.keys() and search_graph(sub_dict[text[0]],text[1:]):
                    C=text[0]+C
                    return True
                else: return False
        
        def xsearch(sub_dict, text):
            global C
            C=""
            check=False
            for i in range(len(text)):
                if search_graph(graph_dict,text[i:]):
                    check=True
                    break
            return (check,i)

        result=xsearch(graph_dict, text)
        if result[0]:
            return (result[1], C[::direction])
        else: raise Exception("No value found")

    def find_wordsr(self, graph_dict, direction):
        text=self.string[::direction]

        def search_graph(sub_dict, text):
            global C
            if None in sub_dict.keys():
                if sub_dict[None]==None: return True
            else:
                if text[0] in sub_dict.keys() and search_graph(sub_dict[text[0]],text[1:]):
                    C=text[0]+C
                    return True
                else: return False
        
        def xsearch(sub_dict, text):
            global C
            C=""
            check=False
            for i in range(len(text)):
                if search_graph(graph_dict,text[i:]):
                    check=True
                    break
            return (check,i)

        result=xsearch(graph_dict, text)
        if result[0]:
            return (result[1], C[::direction])
        else: raise Exception("No value found")

    def get_numbers(self):
        #Return numbers values in a dict as {value:[position,length], ...}
        text=self.string
        result_dict={}
        l=len(text)

        def number_lenght(text):
            count=0
            for i in range(len(text)):
                j=ord(text[i])
                if j>=48 and j<=57:
                    count+=1
                else: break
            return count

        i=1
        while i < l:
            j=ord(text[i])
            if j>=48 and j<=57:
                long=number_lenght(text[i:l-1])
                value=int(text[i:i+long])
                result_dict[value]=(i,long)
                i+=long
            else: i+=1
        
        return result_dict

class Game:
    def __init__(self, string) -> None:
        self.string=string.rstrip("\n")
        
        #Check if initialise as a game
        if self.string[0:4]!="Game": raise Exception("This is not a game !")
        ref=self.string.index(":")

        #Find game number
        gl=Line(self.string[0:ref])
        self.game_number = gl.find_first_number()

        #Extract string of draws
        self.draws_str = self.string[ref+2:]

    def build_draw_dict(self):
        d_dict={}
        words=["green","blue","red"]
        D=self.draws_str.split(";")
        count_draw=0
        for d in D:
            I=d.split(",")
            d_dict[count_draw]={}
            for i in I:
                l=Line(i)
                nb_d=l.find_first_number()
                col_d=l.find_words(words,1)[1]
                d_dict[count_draw][col_d]=nb_d
            count_draw+=1
        return d_dict

    def build_color_dict(self):
        c_dict={}
        words=["green","blue","red"]
        for w in words: c_dict[w]=[]
        D=self.draws_str.split(";")
        for d in D:
            d_dict={}
            for w in words: d_dict[w]=0
            I=d.split(",")
            for i in I:
                l=Line(i)
                nb_d=l.find_first_number()
                col_d=l.find_words(words,1)[1]
                d_dict[col_d]=nb_d
            for w in words: c_dict[w].append(d_dict[w])
        return c_dict

class Grid:
    def __init__(self,grid) -> None:
        self.grid=grid

    def getline(self,l):
        return self.grid[l]

    def scan_symbol(self, coordinates: tuple, line):
        (position,length)=coordinates
        
        valid_symbols = ['$', '@', '=', '/', '&', '#', '-', '*', '+', '%']
        invalid_symbols = '01234566789.'
        check = False
        #Check first on left
        if not check and self.getline(line)[position-1] not in invalid_symbols: check=True
        #Check first on right
        if not check and self.getline(line)[position+length] not in invalid_symbols: check=True
        #Check above and below
        cursor=position-1
        while not check and cursor < position+length+1:
            if self.getline(line-1)[cursor] not in invalid_symbols: check=True
            if self.getline(line+1)[cursor] not in invalid_symbols: check=True
            cursor+=1
        #print(coordinates, check)
        return check

class Card:
    def __init__(self,string) -> None:
        self.raw=string.rstrip("\n")
    
    def number(self):
        number=int(self.raw[4:8])
        return number
    
    def win_list(self):
        win_raw=self.raw[10:40]
        L = [int(x) for x in win_raw.split()]
        return L
    
    def draw_list(self):
        draw_raw=self.raw[42:]
        L = [int(x) for x in draw_raw.split()]
        return L
    
    def match_score(self,type):
        D=self.draw_list()
        W=self.win_list()
        count=0
        for i in D:
            if i in W: 
                count+=1
        if type=="score":
            if count==0: total=0
            else: total=2**(count-1)
        elif type=="qty":
            total=count
        return total