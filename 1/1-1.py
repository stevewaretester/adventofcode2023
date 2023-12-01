#https://adventofcode.com/2023/day/1
import os
import sys


def txtToLineArray(txt):
    file = open(txt, "r")
    lines = file.readlines()
    file.close()
    return lines

###testData
#no numbers - reject string
#only one number - double it
#more than 2 numbers - take only first and last
#only 2 numbers - take first and last.

###General approach
#remove all letters from the line.
#take the first and last for each line

input = os.path.join(sys.path[0],"input.txt")

print()
lines = txtToLineArray(input)
#lines = ["noNumbers","one1Number","mo2retha3ntwo4Numbers","only5two6Numbers"] #11+24+56 = 18
#print(lines)


total = 0
for line in lines:
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