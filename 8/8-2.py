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
lines = txtToLineArray(os.path.join(sys.path[0],"example2.txt"))#6

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
hasAz = []
steps = 1
startLength = len(start)
otherzCount = 0
while loop:
    count=0
    #this one is working out when all the things have zs
    for direction in instructions:
        zCount=0

        ##First approach, wait until they sync up.
        for thisOne in start:
            print(steps)
            #print(thisOne.position)
            index = findIndexByPos(start,thisOne.position)
            #print(start[index].position)
            
            if start[index].position[2]=="Z":
                zCount+=1
                #otherzCount+=1
                start[index].stepsToZ = steps
                #hasAz.append(start.pop(index))
            
            if zCount==startLength:#Scenario 1, they all z's up
                print("all zs line up")
                loop = False
                break

            if direction=="L":
                start[index] = theMap[findIndexByPos(theMap,thisOne.left)]#replace current with left for next loop
            if direction=="R":
                start[index] = theMap[findIndexByPos(theMap,thisOne.right)]#replace current with right for next loop
            print(start[index].position)
            
            
            
        
        count+=1
        if otherzCount==startLength:#Scenario 2, we have a first z for all of the things.
            print("found lowest numbers")
            loop = False
            break

    steps+=1

    if(steps%1000000==0):
        print(steps)

print(steps)
#98454000 = too low

#for zhaver in hasAz:
    #print(zhaver.position+" found at "+str(zhaver.stepsToZ))
