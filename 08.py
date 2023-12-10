import os, errno
import pathlib
import re


class Cross:
    def __init__(self):    
        self.key=""
        self.l = ""
        self.r = ""


file_in = open("08.txt", 'r')
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

az= {k: v for k, v in all.items() if k.endswith("A")}
for a in az:
    print(a)
print(az)
key = "AAA" 
n = 0
todo = ""
# while key != "ZZZ":
#     if(len(todo) == 0):
#         todo=instructions
#     d=todo[0:1]
#     if d == "L":
#         key=all[key].l
#     else:
#         key=all[key].r
#     print(key,n)
#     todo=todo[1:]
#     n=n+1
total1 = n
    
print("----")
print("answer 1 : "+str(total1))
print("answer 2 : "+str(total2))