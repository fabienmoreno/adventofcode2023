import time
start=time.perf_counter()

class Line :
    def __init__(self, string) -> None:
        self.string=string
        self.first=string[0]
    
    def first_last_digit(self):
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
        

filename = "01/input.txt"
with open(filename, "r") as input:
    total=0
    for line in input:
        l=Line(line.rstrip("\n"))
        total+=l.first_last_digit()
    print("Total : ", total)


stop = time.perf_counter()
print("Delay :", (stop-start)*1000, " ms")


