import os, errno
import pathlib
import re

class DrawDesc:

    def __init__(self):    
        self.red = 0
        self.blue = 0
        self.green = 0

    
    def test1(self):
        if self.red >  12 or self.green > 13 or self.blue > 14:
            return False
        return True
    def set(self, color, value):
        if(color == "red"):
            self.red = value
        elif(color == "blue"):
            self.blue = value
        if(color == "green"):
            self.green = value




file_in = open("02.txt", 'r')
lines = file_in.readlines()
total1 = 0
total2 = 0
map= {}
for line in lines:
    lev1 = line.split(":")
    game_num = lev1[0].split(" ")[1]
    draw_descs = lev1[1].split(";")
    print(game_num)
    map[game_num]=[]
#    print(draw_descs)
    passTest = True 
    maxR = 0
    maxG = 0
    maxB = 0

    for draw_desc_s in draw_descs:
        draw_desc = DrawDesc()
        draw_desc_arr = draw_desc_s.split(",")
        for draw_detail in draw_desc_arr:
            draw = draw_detail.strip().split(" ")
            color = draw[1]
            num = int(draw[0])
            draw_desc.set(color,num)
            print(color +"->" +str(num))
        passTest = passTest and draw_desc.test1()
        maxR = max( maxR, draw_desc.red)
        maxG = max( maxG, draw_desc.green)
        maxB = max( maxB, draw_desc.blue)
    if passTest:
        total1 = total1 + int(game_num)
    total2+=(maxR * maxG * maxB)
    

print("----")
print("answer 1 : "+str(total1))
print("answer 2 : "+str(total2))