class Line :
    def __init__(self, string) -> None:
        self.string=string
        self.first=string[0]
    
    def find_digits(self):
        first=""
        last=""
        for i in self.string:
            j=ord(i)
            if j>=48 and j<=57:
                first=i
                break
        for i in self.string[::-1]:
            j=ord(i)
            if j>=48 and j<=57:
                last=i
                break
        first_last=first + last
        try:
            first_last_number=int(first_last)
            return first_last_number
        except:
            print("Error on : ", self.string)

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