import os, errno
import pathlib
import re



class Node:
    def __init__(self,x,y,val):    
        self.key=strkey(x,y)
        self.x = x
        self.y = y
        self.value=val
        self.visited = False
        self.links = []
        self.dist = 0
    
    def __str__(self) -> str:
        return(self.value)

def strkey(x,y):
    return str(x)+"-"+str(y)

def join(a,b):
    if not(b in a.links):
        a.links.append(b)
    if not(a in b.links):
        b.links.append(a)
        


file_in = open("10.txt", 'r')
lines = file_in.readlines()
total1 = 0
total2 = 0
nodes={}
nodes2remove=[]
start= None
h=len(lines)
w=len(lines[0].strip())
for y,line in enumerate(lines):
    line=line.strip()
    for x in range(0, len(line)):
        n=Node(x,y,line[x:x+1])
        nodes[n.key]=n
        if n.value == "S":
            start=n.key
print(w,"*",h, start)
for key in nodes.keys():
    node=nodes[key]
    dirs=[]
    if node.value =="|":
        dirs=["north","south"]
    elif node.value =="-":
        dirs=["east","west"]
    elif node.value =="F":
        dirs=["east","south"]
    elif node.value =="7":
        dirs=["west","south"]
    elif node.value =="J":
        dirs=["north","west"]
    elif node.value =="L":
        dirs=["north","east"]
    if key=="63-78":
        print(dirs, node.value)

    if "north" in dirs:
        destkey = strkey(node.x, node.y-1)
        if destkey in nodes.keys():
            if nodes[destkey].value in ["F","|","7","S"]:
                join(node, nodes[destkey])
    if "south" in dirs:
        destkey = strkey(node.x, node.y+1)
        if destkey in nodes.keys():
            if nodes[destkey].value in ["L","|","J","S"]:
                join(node, nodes[destkey])
    if "east" in dirs:
        destkey = strkey(node.x+1, node.y)
        if destkey in nodes.keys():
            if nodes[destkey].value in ["7","-","J","S"]:
                join(node, nodes[destkey])
    if "west" in dirs:
        destkey = strkey(node.x-1, node.y)
        if destkey in nodes.keys():
            if nodes[destkey].value in ["L","-","F","S"]:
                join(node, nodes[destkey])
todo_nodes=nodes[start].links
dist=0
while len(todo_nodes)>0:
    dist+=1
    next=[]
    for node in todo_nodes:
        print(dist,node.key)
        if not(node.visited):
            node.visited=True
            node.dist=dist
            for neighbour in node.links:
                if not(neighbour.visited):
                    print("->",neighbour.key)

                    next.append(neighbour)

    todo_nodes=next

print("----")
print("answer 1 : "+str(dist))
print("answer 2 : "+str(total2))