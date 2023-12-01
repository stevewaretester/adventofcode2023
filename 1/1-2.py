#https://adventofcode.com/2023/day/1#part2

import os
import sys


def txtToLineArray(txt):
    file = open(txt, "r")
    lines = file.readlines()
    file.close()
    return lines

def numberwang(instr):

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

print()
lines = txtToLineArray(input)
#lines = ["noNumbers","one1Number","mo2retha3ntwo4Numbers","only5two6Numbers"] #11+24+56 = 18
#print(lines)


total = 0
for line in lines:
    #Convert all the strings into numbers
    
    
    #remove the letters
    
    
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