import os, errno
import pathlib
import re

class Map:

    def __init__(self):    
        self.dest = 0
        self.start = 0
        self.length = 0

    def intersects(self, source, length):
        res=[]
        if source>=self.start and source<self.start+self.length: 
            return True
        return False
    def map(self,source):
        if not(self.containsSource(source)):
            raise Exception('pas dans le bon range')
        return self.dest + (source - self.start)
    def __str__(self) -> str:
        return 'map '+str(self.start)+".."+str( self.length)+"->"+str(self.dest)
    
class Plage:

    def __init__(self):    
        self.start = 0
        self.length = 0
    def __str__(self) -> str:
        return 'plage '+str(self.start)+"->"+str( self.length)

class Transition:
    def __init__(self):    
        self.name = ""
        self.maps=[]

    def map(self,source):
        for map in self.maps:
            if map.containsSource(source):
                return map.map(source)
        return source

def transform(plage, maps) -> list[Plage]:

    if len(maps)==0:
        print(" cas 0")
        return [plage]
    map=maps[0]
    print("through --> " ,  map)
    result=[]
    if plage.start < map.start:
        if plage.start + plage.length < map.start:
            # entierement avant la map
            print(" cas 1")
            return [plage]
        else:
            # intersection avec debut de la plage hors de la map
            print("  cas 2")
            first_range = Plage() #plage hors map -> pas de transformation
            first_range.start = plage.start
            first_range.length = map.start - plage.start
            result.append(first_range)

            second_range=Plage() #plage à traiter -> on envoie à la suite pour transformation
            second_range.start = map.start 
            second_range.length = plage.start + plage.length - map.start 
            result.extend(transform(second_range,maps))

            return result
    elif plage.start >= map.start:
        if plage.start >= map.start + map.length:
            # c'est après, on test les maps suivantes
            print(" cas 3")
            return transform(plage, maps[1:])
        else:
            #le debut de ma plage est dans la map
            if  plage.start+ plage.length <= map.start + map.length:
                print(" cas 4")
                # la fin aussi -> on transforme tout
                new_range=Plage()
                new_range.start=map.dest + (plage.start - map.start)
                new_range.length=plage.length
                return [new_range]
            else: 
                # que le début, on split
                print(" cas 5")
                first_range = Plage() # plage dans la map -> on transforme avec dest
                first_range.start = map.dest + (plage.start-map.start )
                first_range.length = map.length - (plage.start-map.start )
                result.append(first_range)

                second_range = Plage() #plage à traiter -> on envoie à la suite
                second_range.start = map.start+ map.length
                second_range.length = plage.length-first_range.length
                result.extend(transform(second_range,maps[1:]))
                return result
    print ("ERROR", plage.start, map.start)


def go():
    file_in = open("05.txt", 'r')
    lines = file_in.readlines()
    total1 = 0
    total2 = 0

    seeds_vals= lines[0].split(':')[1].strip().split()
    seeds = []
    for i in range(0,int(len(seeds_vals)/2)):
        seed = Plage()
        seed.start= int(seeds_vals[i*2])
        seed.length= int(seeds_vals[i*2+1])
        seeds.append(seed)
    

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
            map.start = int(tokens[1])
            map.length = int(tokens[2])
            curr_transition.maps.append(map)

    for transition in transitions:
        for map in transition.maps:
            transition.maps.sort(key=lambda x: x.start)

    plages=seeds;
    for transition in transitions:
        result=[]
        print(transition.name)
        total_range=0
        for plage in plages:
            total_range+=plage.length + 1
        print ("total range", total_range)
        for plage_it in plages:
            print(plage_it)
            result.extend(transform(plage_it,transition.maps))
            print("resultat : ")
            for plage in result:
                print("   ",plage)
        plages=result
    minimum=plages[0].start
    for plage_it in plages:
        minimum=min(plage_it.start, minimum)

    # vals = []
    # for seed in seeds:
    #     val = int(seed)
    #     print(val)
    #     for transition in transitions:
    #         val=transition.map(val)
    #         print("->",val)
    #     print("-->", val)
    #     vals.append(val)

    print("----")
    print("answer 2 : "+ str(minimum))
go()