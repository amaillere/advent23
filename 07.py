import os, errno
import pathlib
import re

cards_type=["A","K","Q","T","9","8","7","6","5","4","3","2","J"]
cards_rank=["A","B","C","D","E","F","G","H","I","J","K","L","M"]


class Hand:
    def __init__(self):    
        self.h = ""
        self.bet=0
        self.h_mapped=""
        self.value=""

    def map(self,source):
        for map in self.maps:
            if map.containsSource(source):
                return map.map(source)
        return source

    def rank(self):
        scores = []
        hand_mapped=""

        for i,type in enumerate(cards_type):
            scores.append(0)
        for card in self.h:
            i=cards_type.index(card)
            scores[i]+=1
            hand_mapped=hand_mapped+cards_rank[i]
        self.h_mapped=hand_mapped
        pairs=0
        brelan=0
        res="G"
        j=cards_type.index("J")
        for i,score in enumerate(scores):
            if score==5: #ex AAAAA ou JJJJJ
                res="A"
            elif score==4:
                if(i!=j) and scores[j]==1:
                    res="A"
                else:
                    res="B"
            elif score==3:
                brelan=1
            elif score==2:
                pairs+=1

        if brelan==1:

            if pairs==1:
                if scores[j]>0: #ex AAAJJ ou JJJAA
                    res="A"
                else:
                    res="C"
            elif scores[j]==1: # ex AAAJ2
                res="B"
            elif scores[j]==3: # ex AJJJ2
                res="B"
            else: # brelan
                res="D"
        elif pairs == 2:
            if scores[j]==1: # ex AAKKJ
                res="C"
                print(self.h,"->" , res)
            elif scores[j]==2:# ex AAJJ2
                res="B"
            else : # ex AAQ22 
                res = "E"
            
        elif pairs == 1:
            res="F"
        #    print(scores[j])
            if scores[j]==1: # ex AAJ982
                res="D"

        
        self.value=res+"_"+hand_mapped
        
    

file_in = open("07.txt", 'r')
lines = file_in.readlines()
total1 = 0
total2 = 0


hands=[]
for line in lines:
    hand=Hand()
    t=line.strip().split()
    hand.h=t[0]
    hand.bet=int(t[1])
    hand.rank()
    hands.append(hand)

sorted_list=sorted(hands, key=lambda h: (h.value),reverse=True)
for i,h in enumerate(sorted_list): 
    # print(h.h,"->" ,h.value)
    # print(i+1,"*" ,h.bet)

    total1+=(i+1)*h.bet



print("----")
print("answer 1 : "+str(total1))
print("answer 2 : "+str(total2))