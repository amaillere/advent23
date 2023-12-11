import os, errno
import pathlib
import re


def resolve(ints):
    next = []
    izZero = True
    for i in range(0,len(ints)-1):
        diff=ints[i+1]-ints[i]
        # print(ints[i+1],"-",ints[i],"=",diff)
        next.append(diff)
        izZero = izZero and (diff == 0)
    # print(next, izZero)
    if izZero:
        next.insert(0,0)
        diffs=next
    else:
        diffs = resolve(next)
    newVal = ints[0]- diffs[0]
    # print(ints[len(ints) - 1],"+", diffs[len(diffs) - 1],"=",newVal)
    ints.insert(0,newVal)
    # print("return", next)
    return ints

file_in = open("09.txt", 'r')
lines = file_in.readlines()
total1 = 0
total2 = 0
series = []
for line in lines:
    ints=[]
    for i in line.split():
        ints.append(int(i))
    series.append(ints)
    newSeries = resolve(ints)
    total2+=newSeries[0]
    print(newSeries[0])


print("----")
print("answer 1 : "+str(total1))
print("answer 2 : "+str(total2))