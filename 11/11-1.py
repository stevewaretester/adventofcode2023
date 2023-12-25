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
#lines = txtToLineArray(os.path.join(sys.path[0],"example.txt"))

print(lines)

###Objects
class galaxy:
  def __init__(self, num, xpos, ypos):
    self.num = num
    self.xpos = xpos
    self.ypos = ypos


newLines = []

#find blank rows
'''
for line in lines:
    newLines.append(line.rstrip('\n'))
    if not '#' in line:
        newLines.append('..........')#add a new blank line
'''
count = 1#find blank rows AND convert to numbers.
for line in lines:
    theLine = line.rstrip('\n')
    print(theLine)
    if not '#' in theLine:
        newLines.append('.'*len(theLine))
    else:

        for x in range(0,theLine.count('#')):
            #theLine = theLine.replace('#',str(count),1)
            print('the Line '+theLine)
            count+=1
            print(theLine)
    newLines.append(theLine)

print("lines post Rows")
for line in newLines:
    print(line)

#find blank columns
rowCount = len(newLines)
print('No. Rows: '+str(rowCount))
right = 0
moreRight=True
while moreRight:#cycle the columns
    down = 0
    moreDown = True
    while moreDown:#cycle the rows within the column
        
        if down==rowCount:#we're at the bottom
            print("right: "+str(right))
            for i in range(0,len(newLines)):#insert the new cols
                newLines[i] = newLines[i][:right] + '.' + newLines[i][right:]

            for line in newLines:
                print(line)

            right+=1#jump past the new column, we know it's all 1s already.
            moreDown = False
            #down = 0
            break

        if right>=len(newLines[0]):#if we're at the end, break out.
            moreDown = False
            break

        #print('down: '+str(down)+', right: '+str(right))
        #if newLines[down][right].isdigit(): #if we found a digit        
        if newLines[down][right] == '#': #if we found the thing.
            moreDown = False
            break
        
        down += 1


    if (right >= len(newLines[0])-1):#if we're outside what's possible
        print('exit'+str(right))
        moreRight = False
        moreDown = False
        break

    right+=1


print("lines post columns")
for line in newLines:
    print(line)

galaxies = []

ypos = 0
for line in newLines:
    xpos=0
    for cha in line:
        #if(cha.isdigit()):
        if cha == '#':
            galaxies.append(galaxy(cha,xpos,ypos))
        xpos+=1
    ypos+=1
#now to turn these into coordinate values


for g in galaxies:
    print("g: "+str(g.num)+" x: "+str(g.xpos)+" y:"+str(g.ypos))

print("No. of Galaxies: "+str(len(galaxies)))
runningTotal = 0
allDone = []

for g in galaxies:
    allDone.append(g)
    #print("new")
    #if len(gCopy)>0:
    for c in galaxies:
        if c in allDone:
            #print("galaxy: "+str(c.num)+" x: "+str(c.xpos)+" y:"+str(c.ypos))
            xout = abs(g.xpos-c.xpos)
            yout = abs(g.ypos-c.ypos)
            runningTotal+=(xout+yout)

'''
for g in galaxies:
    print("g: "+str(g.num)+" x: "+str(g.xpos)+" y:"+str(g.ypos))

for c in allDone:
    print("c: "+str(c.num)+" x: "+str(c.xpos)+" y:"+str(c.ypos))
'''

print(runningTotal)
#now for every galaxy take the absolute value of x and the absolute value of y
#