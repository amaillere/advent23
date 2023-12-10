import os, errno
import pathlib
import re


class Card:

    def __init__(self):    
        self.card_num = ""
        self.winning = []
        self.numbers = []
        self.matchesNb = 0
        self.score = 0
        self.weight = 1



file_in = open("04.txt", 'r')
lines = file_in.readlines()
total1 = 0
total2 = 0
weight = 0
allCards = []
for line in lines:
    card = Card()
    allCards.append(card)
    lev1 = line.split(":")
    card_num = lev1[0].split(" ")[1]
    card.card_num = card_num
    nums = lev1[1].split("|")
    for num in nums[0].split(" "):
        num = num.strip()
        if(num.isdigit()):
            card.winning.append(num)
    for num in nums[1].split(" "):
        num = num.strip()
        if(num.isdigit()):
            card.numbers.append(num)
    # print(card_num, len(card.winning), len(card.numbers))
    print(card.card_num, card.winning, card.numbers)
    
    for num in card.numbers:
        if num in card.winning:
            card.matchesNb += 1
            if card.score == 0:
                card.score = 1
            else:
                card.score = card.score * 2
            
    # print(card.score)
    total1+=card.score

for i,card in enumerate(allCards):
    print(card.card_num, card.winning, card.numbers)
    if card.matchesNb > 0:
        limMax=min(len(lines),i+card.matchesNb+1)
        print("card", i+1, "from", i, "to", limMax)
        for j in range(i+1,limMax):
            allCards[j].weight+=card.weight

    total2+=card.weight





#    print(draw_descs)

print("----")
print("answer 1 : "+str(total1))
print("answer 2 : "+str(total2))