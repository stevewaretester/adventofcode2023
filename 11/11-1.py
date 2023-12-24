import os
import sys
import numbers


def txtToLineArray(txt):
    file = open(txt, "r")
    lines = file.readlines()
    file.close()
    return lines

#input = os.path.join(sys.path[0],"input.txt")
#lines = txtToLineArray(input)
###Example lines

lines = txtToLineArray(os.path.join(sys.path[0],"example.txt"))

print(lines)

newLines = []

#find blank rows
for line in lines:
    newLines.append(line.rstrip('\n'))
    if not '#' in line:
        newLines.append('..........')

for line in newLines:
    print(line)

#find blank columns
rowCount = len(newLines)
print('No. Rows: '+str(rowCount))
down = 0
right = 0
moreRight=True
while moreRight:#cycle the columns
    moreDown = True
    while moreDown:#cycle the rows within the column
        print('down: '+str(down)+', right: '+str(right))
        if down==rowCount:#we're at the bottom
            for i in range(0,len(newLines)-1):
                newLines[i] = newLines[i][:right] + '.' + newLines[i][right:]
                for line in newLines:
                    print(line)
            right+=1
            moreDown = False
            down = 0
            break
            

        if right==len(newLines[0]):#if we're at the end, break out.
            moreDown = False
            break
            
        if newLines[down][right] == '#': #if we found the thing.
            down = 0
            break
        
        down += 1

    if (right >= len(newLines[0])-1) and (down >= rowCount-1):#if we're bottom right.
        print('exit'+str(right))
        moreRight = False
        moreDown = False
        break
    right+=1

for line in newLines:
    print(line)


'''while moreRows:
    across = 0
    moreCols = True
    while moreCols:
    #for across in range(0, len(newLines[0])):
        print('down: '+str(down)+' across:'+str(across))
        if newLines[down][across] == '#':
            down=0
            break
        if newLines[down]>=rowCount-1:
            for line in newLines:
                line.insert(across,'.')
                across+=1
                down = 0

    if down >= rowCount-1 and across >=newLines[0]:
        moreRows = False
        break
    down+=1
'''