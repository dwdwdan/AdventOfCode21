#!/usr/bin/env python3

f=open("input.txt")
lines=f.readlines()
data=[]
for line in lines:
    data.append(line.split())

x=0
depth=0
for dataPoint in data:
    direction=dataPoint[0]
    magnitude=int(dataPoint[1])
    match direction:
        case "up":
            depth=depth-magnitude
        case "down":
            depth=depth+magnitude
        case "forward":
            x=x+magnitude

print("x=",x)
print("depth=",depth)
print("PartA=",x*depth)

x=0
depth=0
aim=0
for dataPoint in data:
    direction=dataPoint[0]
    magnitude=int(dataPoint[1])
    match direction:
        case "forward":
            x=x+magnitude
            depth=depth+(aim*magnitude)
        case "up":
            aim=aim-magnitude
        case "down":
            aim=aim+magnitude

print("PartB=",x*depth)
