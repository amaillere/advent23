import os, errno
import pathlib
import re

import os


def parse(chaine):
    count = 0
    res=""
    for char in chaine:
        substr=chaine[count:]
        if char.isdigit():
            res+=char
        elif substr.startswith("one"):
            res+="1"
        elif substr.startswith("two"):
            res+="2"
        elif substr.startswith("three"):
            res+="3"
        elif substr.startswith("four"):
            res+="4"
        elif substr.startswith("five"):
            res+="5"
        elif substr.startswith("six"):
            res+="6"
        elif substr.startswith("seven"):
            res+="7"
        elif substr.startswith("eight"):
            res+="8"
        elif substr.startswith("nine"):
            res+="9"
        count+=1
    return res

file_in = open("01.txt", 'r')
lines = file_in.readlines()
total1 = 0
total2 = 0
for line in lines:
    print("----")
    print(line)
    digits = re.findall("\d+", line)
    nums="".join(digits)
    print(nums)
    firstlast=nums[:1]+nums[-1:]
    print(firstlast)
    total1 += int(firstlast)
    print("-")

    nums = parse(line)
    print(nums)
    firstlast=nums[:1]+nums[-1:]
    print(firstlast)
    total2 += int(firstlast)


print("----")
print("answer 1 : "+str(total1))
print("answer 2 : "+str(total2))

