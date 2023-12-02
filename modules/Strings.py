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

    def find_words(self, words, position, direction):
        text=self.string[position::1]
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
                col_d=l.find_words(words,0,1)[1]
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
                col_d=l.find_words(words,0,1)[1]
                d_dict[col_d]=nb_d
            for w in words: c_dict[w].append(d_dict[w])
        return c_dict
