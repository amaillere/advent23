import os, errno
import pathlib
import re




file_in = open("06.txt", 'r')
lines = file_in.readlines()
total1 = 1
total2 = 0

times=lines[0].strip().split()[1:]
distances=lines[1].strip().split()[1:]

for i,t in enumerate(times):
    t=int(t)
    count=0
    refDist = int(distances[i])
    for chargingTime in range(0,t):
        runningTime=t-chargingTime
        dist=chargingTime*runningTime
        #print(chargingTime, ":",dist)
        if dist > refDist:
            count += 1
    print(count)
    total1*=count
        
print("---")
for t in distances:
    
    print(t)

print("----")
print("answer 1 : "+str(total1))
print("answer 2 : "+str(total2))