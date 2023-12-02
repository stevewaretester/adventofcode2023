#https://adventofcode.com/2023/day/1#part2

import os
import sys


def txtToLineArray(txt):
    file = open(txt, "r")
    lines = file.readlines()
    file.close()
    return lines

class numAndPos:
  def __init__(num, pos):
    self.name = num
    self.age = pos


def numberwang(instr):
#get the starting character position of each word

#for

#get the position of each number
#smush together into a new string

    return 0
    
thisDict = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" :  "9"
}

input = os.path.join(sys.path[0],"input.txt")

#lines = txtToLineArray(input)

lines = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen","five1oneightg"] #values are 29, 83, 13, 24, 42, 14, and 76 and 58 = 281+58=339
print(lines)


total = 0
for line in lines:
    #Convert all the strings into numbers
    
    
    #remove any remaining letters
    
    numbers = ''.join(filter(str.isdigit, line))


    numbersLength = (len(numbers))
    #(provided there actually was a number)
    if numbersLength>0:
        #take the first and last number
        smush = numbers[0]+numbers[numbersLength-1]
        print(smush)
        #add it to the running total
        total+= int(smush)

print("Total: "+str(total))