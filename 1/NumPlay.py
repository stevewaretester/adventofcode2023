#https://adventofcode.com/2023/day/1#part2

import os
import sys


input = os.path.join(sys.path[0],"input.txt")

lines = ["1twoneighthree3nine4fiveightwosevenine5","two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen","five1oneightg"]

#lines = txtToLineArray(input)

#Object for holding number and position
class numAndPos:
  def __init__(self, num, pos):
    self.num = num
    self.pos = pos


#function for finding a string within a string and returning its numerical translation and position
def findAllInstances(searchin, searchfor, actualInt):
    outputList = []#list we'll add objects to
    lastpos = 0
    moreToFind = True
    while moreToFind:
        position = searchin.find(searchfor,lastpos)
        intpos = searchin.find(str(actualInt),lastpos)
        if position >=0:
            #print(str(searchfor+" @ "+str(position))) #capture the position of the thing
            lastpos = position + len(searchfor)
            outputList.append(numAndPos(actualInt,position))
        else:
            moreToFind = False
    return outputList


textNums = ["one","two","three","four","five","six","seven","eight","nine"]

#Actual logic here
total = 0
for line in lines:
    print(line)
    count=0
    total = 0
    bigArray = []
    for textnum in textNums:#compare against the word-numbers
        count+=1
        if not(textnum in line):#early exit can skip if it's not in.
            #print("no "+textnum+"'s")
            continue#skipthisnumber
        output1 = findAllInstances(line,textnum,count)
        for thing in output1:
            bigArray.append(thing)


    for i in range(1,10):#compare against numerical-numbers
        if not(str(i) in line):#early exit can skip if it's not in.
            #print("no "+str(i)+"'s")
            continue
        output2 = findAllInstances(line,str(i),i)
        for thing in output2:
            bigArray.append(thing)
    
    bigArray.sort(key=lambda x: x.pos)#sort it so we have a top and a bottom across all values
    
    for thing in bigArray:
        print("num:"+str(thing.num)+", pos:"+str(thing.pos))
    
    
    
