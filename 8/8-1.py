import os
import sys
import numbers


def txtToLineArray(txt):
    file = open(txt, "r")
    lines = file.readlines()
    file.close()
    return lines

input = os.path.join(sys.path[0],"input.txt")
lines = txtToLineArray(input)

###Example lines

#lines = txtToLineArray(os.path.join(sys.path[0],"example.txt"))#2
#lines = txtToLineArray(os.path.join(sys.path[0],"example1.txt"))#6



###Classes
class posLeftRight:
    def __init__(self, position, left, right):     
        self.position = position
        self.left = left
        self.right = right

###Functions
def findIndexByPos(list, criteria):
    index = 0
    for thing in list:
        if thing.position == criteria:
            return index
        index+=1


start = "AAA"
end = "ZZZ"

instructions = lines.pop(0).rstrip("\n")
lines.pop(0) #remove the leading space
print(instructions)
print(lines)

theMap = []

for line in lines:
    posAndDirection = line.split("=")
    pos = posAndDirection[0].rstrip()
    print(pos)
    saneDirection = posAndDirection[1].replace("(","").replace(")","").rstrip().lstrip().split(", ")#remove all the gunk and take just this.
    print(saneDirection)
    theMap.append(posLeftRight(pos,saneDirection[0],saneDirection[1]))



loop = True
next = start
steps = 1
while loop:
    for direction in instructions:
        print(direction)
        current = ""
        if direction=="L":
            next = theMap[findIndexByPos(theMap,next)].left
        if direction=="R":
            next = theMap[findIndexByPos(theMap,next)].right
        if next==end:
            loop=False#break the loop
            break#break the directions
        steps+=1#otherwise increment the steps.

print(steps)