import os, errno
import pathlib
import re
import math


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

def allZ(vals):
    res= True
    for a in vals:
        res = res and a.endswith("Z")
    return res
    
az = {k: v for k, v in all.items() if k.endswith("A")}
values={}
for a in az:
    print(a, az[a])
    values[a]=all[a]

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
n = 0
todo = ""
#values = az
# while not(allZ(values)) :
#     if(len(todo) == 0):
#         todo=instructions
#     d=todo[0:1]
#     next={}
#     n=n+1
#     for val in values:
#         #print(val)
#         cross=all[values[val].key]
#         if d == "L":
#             nextVal=cross.l
#         else:
#             nextVal=cross.r
        
#         next[val]=all[nextVal]
#         if(nextVal.endswith("Z")):
#             print(val, nextVal, n)
#     values = next
#     # print(key,n)
#     todo=todo[1:]
total1 = n
a=13019
a=16343

a=lcm(13019,16343)
a=lcm(a,16897)
a=lcm(a,19667)
a=lcm(a,20221)
a=lcm(a,21883)

print("----")
print("answer 1 : "+str(total1))
print("answer 2 : "+str(a))