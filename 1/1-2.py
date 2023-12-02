#https://adventofcode.com/2023/day/1#part2

import os
import sys


def txtToLineArray(txt):
    file = open(txt, "r")
    lines = file.readlines()
    file.close()
    return lines

class numAndPos:
  def __init__(self, num, pos):
    self.num = num
    self.pos = pos

    

#Reading in the file and parsing it to lines
input = os.path.join(sys.path[0],"input.txt")

lines = txtToLineArray(input)


###testlines
#lines = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen","five1oneightg"] #values are 29, 83, 13, 24, 42, 14, and 76 and 58 = 281+58=339 # round 1 is actually 69
#lines = ["1twoneighthree3nine4fiveightwosevenine5","two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen","five1oneightg"]

#print(lines)


#function for finding a string within a string and returning its numerical translation and position
def findAllInstances(searchin, searchfor, actualInt):
    outputList = []
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


#just an array of text numbers in order so I can do say actualnumber=1 textNums[actualnumber-1], so I know one is 1
textNums = ["one","two","three","four","five","six","seven","eight","nine"]


total = 0 #this is the actual value we need to return.

for line in lines:
    print(line)
    count = 0 #cheap way of doing the actual "number" for the textnums, because I'll increment before doing anything, and one=1, two=1 etc.
    
    bigArray = []#this is an aggregate array across both textnums and numerals to capture
    for textnum in textNums:#compare against the word-numbers
        count+=1#told ya it'd increment.
        if not(textnum in line):#early exit can skip if it's not in.
            #print("no "+textnum+"'s")
            continue#skipthisnumber
        output1 = findAllInstances(line,textnum,count)
        for thing in output1:
            bigArray.append(thing)
       
#adspace here.
    for i in range(1,10):#1-9 (inclusive) baby
        if not(str(i) in line):#early exit can skip if it's not in.
            #print("no "+str(i)+"'s")
            continue
        output2 = findAllInstances(line,str(i),i)
        for thing in output2:
            bigArray.append(thing)
    
    bigArray.sort(key=lambda x: x.pos)#sorts each bigArray from lowest to highest.
    
    smush = str(bigArray[0].num)+str(bigArray[len(bigArray)-1].num)#same as 1-1: takes the lowest and highest numbers as strings, concats them (so 1,2 = 12)
    print(smush)
    total+=int(smush)

    for thing in bigArray:
        print("num:"+str(thing.num)+", pos:"+str(thing.pos))

print("TOTAL = "+str(total))
#52834
