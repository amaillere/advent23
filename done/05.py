import os, errno
import pathlib
import re

class Map:

    def __init__(self):    
        self.dest = 0
        self.source = 0
        self.range = 0

    def containsSource(self, source):
        if source>=self.source and source<self.source+self.range:
            return True
        return False
    def map(self,source):
        if not(self.containsSource(source)):
            raise Exception('pas dans le bon range')
        return self.dest + (source - self.source)

class Transition:
    def __init__(self):    
        self.name = ""
        self.maps=[]

    def map(self,source):
        for map in self.maps:
            if map.containsSource(source):
                return map.map(source)
        return source


def go():
    file_in = open("05.txt", 'r')
    lines = file_in.readlines()
    total1 = 0
    total2 = 0

    seeds= lines[0].split(':')[1].strip().split()
    
    print(seeds)
    curr_transition = None
    transitions=[]
    for line in lines:
        line=line.strip()

        if line.endswith("map:"):
            curr_transition= Transition()
            curr_transition.name=line.split()[0]
            transitions.append(curr_transition)
        if line[0:1].isdigit():
            map = Map()
            tokens = line.split()
            map.dest = int(tokens[0])
            map.source = int(tokens[1])
            map.range = int(tokens[2])
            curr_transition.maps.append(map)

    # for transition in transitions:
    #     print(transition.name)
    #     for map in transition.maps:
    #         print(map.dest, map.source, map.range)
    #     print()
    vals = []
    for seed in seeds:
        val = int(seed)
        print(val)
        for transition in transitions:
            val=transition.map(val)
            print("->",val)
        print("-->", val)
        vals.append(val)

    print("----")
    print("answer 1 : "+str(min(vals)))
    print("answer 2 : "+str(total2))
go()