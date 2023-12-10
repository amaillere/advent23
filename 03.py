import os, errno
import pathlib
import re

class Part:

    def __init__(self):    
        self.x = 0
        self.y = 0
        self.val = 0
        self.length = 0

    

class Symbol:

    def __init__(self):    
        self.x = 0
        self.y = 0
        self.sym = ""
        self.parts=[]

    


def isPartNumber(part):
    for x in range(max(0,part.x - 1), min(140,part.x + 2)):
        for y in range ( max(0, part.y-1), min(140, part.y + part.length + 1)):
            char=all[x][y]
            # print(part.val,x,y,char)
            if not(char.isdigit()) and not(char == "."):
                # print(part.val, "at",part.x,":",part.y,"for char",char,"at", x,":",y)
                index=str(x)+"_"+str(y)
                allsyms[index].parts.append(part)
                return True
    # print(part.val, "at",part.x,":",part.y," : Nope")
    return False

file_in = open("03.txt", 'r')
lines = file_in.readlines()
total1 = 0
total2 = 0
all = []
allparts=[]
count = 0 
allsyms ={}
for i,line in enumerate(lines):
    print(i)
    aline=list(line.strip())
    all.append(aline)
    number=0
    x=0
    y=0
    part = None
    for(j,char) in enumerate(line):
        if char.isdigit(): 
            if number==0:
                part=Part()
                number=int(char)
                part.val = number
                part.x=i
                part.y=j
                part.length= 1
                allparts.append(part)
            else:
                number=10*number+(int(char))
                part.val=number
                part.length = part.length +1
        else:
            number = 0
            if char != ".":
                sym= Symbol()
                sym.x=i
                sym.y=j
                sym.sym=char
                index=str(i)+"_"+str(j)
                allsyms[index]=sym
    

for part in allparts:
    if isPartNumber(part):
        total1+=part.val

for name,sym in allsyms.items():
    if len(sym.parts) == 2:
        print(sym)
        val = sym.parts[0].val*sym.parts[1].val
        total2+=val
print("----")
print("answer 1 : "+str(total1))
print("answer 2 : "+str(total2))