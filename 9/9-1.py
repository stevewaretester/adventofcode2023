import os
import sys
import numbers
#import numpy


def txtToLineArray(txt):
    file = open(txt, "r")
    lines = file.readlines()
    file.close()
    return lines

input = os.path.join(sys.path[0],"input.txt")
lines = txtToLineArray(input)

###Example lines

lines = txtToLineArray(os.path.join(sys.path[0],"example.txt"))


###Classes
class dataObj:
    def __init__(self, array = []):
        self.array = [[]]
        self.array.append([])
        self.array[0] = array

datas = []

for line in lines:
    datas.append(dataObj(line.split()))

for data in datas:
    data.array[1].append("adada")
    print(data.array)