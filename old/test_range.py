r=range(5,10)
print(r)
k=10
if k in r: print("yes")
else: print("no")

D={}
D[range(1,10)]=30
print(D)

line="79 14 55 13"
seeds_list=line.split()
print(seeds_list[0::2])
print(seeds_list[1::2])

seeds_dict={}

for k,i in enumerate(seeds_list[0::2]):
    for j in range(int(i),int(i)+int(seeds_list[1::2][k])):
        seeds_dict[j]=j

print(seeds_dict)
print(len(seeds_dict))