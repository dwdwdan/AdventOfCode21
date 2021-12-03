#!/usr/bin/env python3

from bitstring import BitArray


f=open("input.txt")
lines=f.read().splitlines()
numBits=len(lines[1])

def bits2Int(bitarray):
    return BitArray(bitarray).uint

def countBits(lines):
    """Counts how many 0s there are in each column and stores it in count0.
    Similarly for 1s in count1"""
    count0=[0]*numBits
    count1=[0]*numBits
    for line in lines:
        for idx,bit in enumerate(line):
            if bit == "1":
                count1[idx]=count1[idx]+1
            elif bit == "0":
                count0[idx]=count0[idx]+1
            else:
                raise ValueError("The input file contains characters that aren't 0 or 1")
    return count0,count1

def genGammaEpsilon(count0,count1,numBits):
    epsilonBits=[0]*numBits
    gammaBits=[1]*numBits
    for idx in range(0,numBits):
        if count1[idx]==count0[idx]:
            raise "These have the same count, I don't know what to do"
        elif count1[idx]<count0[idx]:
            gammaBits[idx]=0
            epsilonBits[idx]=1

    gamma=bits2Int(gammaBits)
    epsilon=bits2Int(epsilonBits)
    return gamma,epsilon

count0,count1=countBits(lines)


gamma,epsilon=genGammaEpsilon(count0,count1,numBits)

print("Gamma=",gamma)
print("Epsilon=",epsilon)

print("PartA:",gamma*epsilon)

def filterRows(idx, value, toFilter):
    """Returns a filtered list where index idx==value."""
    output=[]
    for line in toFilter:
        if line[idx]==value:
            output.append(line)
    # print(output)
    return output

def getOxyRating(numBits, lines):
    for idx in range(0,numBits):
        count0,count1=countBits(lines)
        if count1[idx]<count0[idx]:
            lines=filterRows(idx,"0",lines)
        elif count1[idx]>count0[idx]:
            lines=filterRows(idx,"1",lines)
        else:
            lines=filterRows(idx,"1",lines)
    if len(lines)>1:
        raise Exception("There are multiple possible solutions")
    return int(lines[0],2)

def getCO2Rating(numBits, lines):
    for idx in range(0,numBits):
        if len(lines)==1:
            break
        count0,count1=countBits(lines)
        if count1[idx]<count0[idx]:
            lines=filterRows(idx,"1",lines)
        elif count1[idx]>count0[idx]:
            lines=filterRows(idx,"0",lines)
        else:
            lines=filterRows(idx,"0",lines)
    if len(lines)>1:
        raise Exception("There are multiple possible solutions")
    return int(lines[0],2)

oxy=getOxyRating(numBits, lines)
co2=getCO2Rating(numBits, lines)
print("oxy=",oxy)
print("co2=",co2)


print("PartB:",oxy*co2)
