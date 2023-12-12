import os, errno
import pathlib
import math



file_in = open("11_2.txt", 'r')
lines = file_in.readlines()
total1 = 0
total2 = 0




class Galaxy:
    def __init__(self,x,y):
        self.x = x
        self.y = y




def display():
    print("".join("-" for i in range(w)))
    for y in range(0,h):
        line=""
        for x in range(0,w):
            line+=map[x][y]
        print(line)
    
def isLineEmpty(n):
    for i in range(w):
        if map[i][n]=="#":
           return False
    return True 

def isColEmpty(n):
    for i in range(h):
        if map[n][i]=="#":
           return False
    return True 



w=len(lines[0].strip())
h=len(lines)
map = [["." for column in range(h)] for row in range(w)]
galaxies=[]


# init universe
for y,line in enumerate(lines):
    for x,char in enumerate(line.strip()):
        if char=="#":
            map[x][y]="#"
            galaxies.append(Galaxy(x,y))

#expand



display()

for y in reversed(range(0,h)):
    print(y)
    if isLineEmpty(y):
        print("line empty", y)
        for col in map:
            col.insert(y,".")
        h+=1


for x in reversed(range(0,w)):
    if isColEmpty(x):
        newLine = ["." for i in range(w)]  
        map.insert(x,newLine)
        w+=1 
display()

print("----")
print("answer 1 : "+str(total1))
print("answer 2 : "+str(total2))