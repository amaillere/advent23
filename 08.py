import os, errno
import pathlib
import re


class Cross:
    def __init__(self):    
        self.key=""
        self.l = ""
        self.r = ""


file_in = open("08_2.txt", 'r')
lines = file_in.readlines()
instructions=lines[0].strip()


total1 = 0
total2 = 0
all={}



for line in lines[2:]:
    cross=Cross()
    cross.key=line[0:3]
    cross.l=line[7:10]
    cross.r=line[12:15]
    #print(cross.key,cross.l, cross.r)
    all[cross.key] = cross
#total1=findZZZ(instructions,"AAA",0)

def allZ(vals):
    res= True
    for a in vals:
        res = res and a.endswith("Z")
    return res
    
az = {k: v for k, v in all.items() if k.endswith("A")}

for a in az:
    print(az[a])


n = 0
todo = ""
values = az
while not(allZ(values)) and n<2:
    print("----")
    if(len(todo) == 0):
        todo=instructions
    d=todo[0:1]
    next={}
    print(values)
    for val in values:
        if d == "L":
            key=all[val].l
        else:
            key=all[val].r
        
        next[key]=all[key]
    print(next)
    values = next
    # print(key,n)
    todo=todo[1:]
    n=n+1
total1 = n
    
print("----")
print("answer 1 : "+str(total1))
print("answer 2 : "+str(total2))