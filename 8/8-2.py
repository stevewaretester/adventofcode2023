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
#lines = txtToLineArray(os.path.join(sys.path[0],"example2.txt"))#6

###Classes
class posLeftRight:
    def __init__(self, position, left, right, stepsToZ = None):     
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

#start = "AAA"
start = []

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

start = list(filter(lambda anA: anA.position[2] == "A", theMap))

for astart in start:
    print(str(findIndexByPos(start,astart.position))+" pos: "+astart.position+" left: "+astart.left+" right: "+astart.right)
print(len(start))
loop = True
#next = start
steps = 0
while loop:
    count=0
    for direction in instructions:
        zCount=0

        ##First approach, wait until they sync up.
        for thisOne in start:
            #print(thisOne.position)
            if direction=="L":
                start[findIndexByPos(start,thisOne.position)] = theMap[findIndexByPos(theMap,thisOne.left)]
            if direction=="R":
                start[findIndexByPos(start,thisOne.position)] = theMap[findIndexByPos(theMap,thisOne.right)]
            if thisOne.position[2]=="Z":
                zCount+=1
                thisOne.stepsToZ = steps
        count+=1
        if zCount==len(start):
            loop = False
            break
        steps+=1
    if(steps%1000==0):
        print(steps)

print(steps)
#98454000 = too low