D=[str(x) for x in range(1,10)]
print(D)

S=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
print(S[0][0])

Sset=set()
for i in S: Sset.update(i[-1])
print(Sset)

T="xhtgthreentqonelvxohjtr4ninesdbvonefmfiveqkr"
print(T[0::1])

def find_words(text, words, position, direction):
    text=text[position::1]
    if direction == 1:
        min=len(text)
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
        max=0
        wmax=""
        for w in words:
            try:
                j=text.rindex(w)
                print(j,w)
                if j>max: 
                    max=j
                    wmax=w
            except:
                pass
        if wmax!="": return (max,wmax)
        else: return (-1,"")
print(find_words(T,S,0,1))