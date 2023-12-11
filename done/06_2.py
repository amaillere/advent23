import os, errno
import pathlib
import re
import math




file_in = open("06.txt", 'r')
lines = file_in.readlines()
total1 = 1
total2 = 0

time=int("".join(lines[0].strip().split()[1:]))
distance=int("".join(lines[1].strip().split()[1:]))

print(time)
print(distance)
# for i,t in enumerate(times):
    # t=int(t)
    # count=0
    # refDist = int(distances[i])
    # for chargingTime in range(0,t):
    #     runningTime=t-chargingTime
    #     dist=chargingTime*runningTime
    #     #print(chargingTime, ":",dist)
    #     if dist > refDist:
    #         count += 1
    # print(count)
    # total1*=count

# -ct²+ct-dist=0  (time-ct)*ct=dist
#  -1*x²  +   time*x -distance=0
# b²-4ac =time² - 4( -1 * -distance)
discriminant = pow(time,2)-4*(-1*(0-distance))
print( "disc",discriminant)

moins_b= 0-time
deuxa = -2  
racinededisc = math.sqrt(discriminant)
x1 = math.ceil( (moins_b+racinededisc)/deuxa )
x2 = math.floor( (moins_b-racinededisc)/deuxa )
print(x2-x1+1)
print("---")


print("----")
print("answer 1 : "+str(total1))
print("answer 2 : "+str(total2))