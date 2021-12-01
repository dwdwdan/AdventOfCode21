#!/usr/bin/env python3

f=open("input.txt")
data=list(map(int,f.readlines()))
count=0
for idx in range(1,len(data)):
    if data[idx-1]<data[idx]:
        count+=1

print("Part A: ", count)

count=0
sum=[]
for idx in range(2,len(data)):
    sum.append(data[idx-2]+data[idx-1]+data[idx])

for idx in range(1,len(sum)):
    if sum[idx-1]<sum[idx]:
        count+=1

print("Part B: ", count)
