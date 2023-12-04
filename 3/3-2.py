#https://adventofcode.com/2023/day/3#part2
#I think I can reuse all this code, but I need to capture the gear positions to do it.
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


###Part 2

class StrAndPos:
    def __init__(self, str, rowPos,colPos):
        self.str = str
        self.rowPos = rowPos
        self.colPos = colPos


###Part 2




#example lines

'''
example = os.path.join(sys.path[0],"example.txt")
lines = txtToLineArray(example)
'''
numberChars= ["0","1","2","3","4","5","6","7","8","9"] #numbers as characters for easy comparison, could do this programmatically but I'm lazy.

symbols = [] #we need to know what the special symbols are
grid = [[]] #setup a 2d array for easy manipulation


#storing the locations of things
gearsLoc = []
numbLoc = []


###Setting up the grid and getting all the symbols.
rowCount = 0
for line in lines:
    colCount = 0
    for character in line.rstrip('\n'):#get rid of the newline symbol
###1 - Get all the GEARS
        #if not character in symbols and not character in numberChars and not character==".":
        if character == "*": # if it's a gear
            if not character in symbols:
                symbols.append(character) #Only add gears once - sloppy but whatever.
            gearsLoc.append(StrAndPos(character,rowCount,colCount)) #add the location of every gear.
###2 - Load the grid so it can be manipulated as a 2d array.
        grid[rowCount].append(character)#add this column to the grid
        colCount +=1
    rowCount +=1
    if len(grid)<len(lines):#if we're not up to the same size as the lines
        grid.append([])#add another line to the grid.

print("Symbols are:")
print(symbols)

print(grid)#Success, we have our 2d Array.

'''3. Finding adjacent symbols and completing entire numbers.
Two mechanisms to use here.

1) Detecting adjacent symbols - this will decide whether we keep a number or not
2) Detecting adjacent numbers
'''
Total = 0#what we'll be printing at the end.
rowCount = 0 #Lets us know what row we're on for easy targetting.
rowMax = len(grid) #number of all rows
#while rowLoop:
for row in grid:
    print(row)
    colMax = len(row)#number of all columns



    symbolFound = False #can use this to early-exit searching for symbols.
    skipBy = 0#we can use this to skip the next few columns - eg if we've found a number string
    colCount = 0 #what current column we're targetting.
    
    for col in row:
        if(skipBy>0):#If we've already captured this number, might as well skip.
            skipBy-=1
            colCount+=1
            continue

        #print(col)
        partNumber = ""
        if col in numberChars:#if it's a number.
            partNumber = col#grab our partnumber now, we'll add to it later

            topLeft = ""
            midLeft = ""
            botLeft = ""
            topRight = ""
            botRight = ""
                        
            if(colCount-1>=0 and rowCount-1>=0):
                topLeft = grid[rowCount-1][colCount-1]#back one, above one - check they aren't out of bounds
            if(colCount-1>=0):#back one - check it isn't out of bounds
                midLeft = grid[rowCount][colCount-1]

            if(colCount-1>=0 and rowCount+1<rowMax):#back one, below one - check they aren't out of bounds
                botLeft = grid[rowCount+1][colCount-1]
                #print("botLeft: "+botLeft)

            if(topLeft in symbols or midLeft in symbols or botLeft in symbols):
                symbolFound = True
                #print(col+" has a backwards symbol")
            
            #start looping.
            sliding = True
            colOffset = colCount #used to move the colCheck forward
            while sliding:
                above = ""
                below = ""
                
                if not symbolFound:
                    if(rowCount-1>=0):#above
                        above=grid[rowCount-1][colOffset]
                    if(rowCount+1<rowMax):#below
                        below=grid[rowCount+1][colOffset]

                    if above in symbols or below in symbols:
                        symbolFound = True
                        #print(grid[rowCount][colOffset]+" has a vertical symbol")

                if colOffset+1<colMax:#if there's any space right:
                    nextChar = grid[rowCount][colOffset+1]
                    
                    if nextChar in symbols:
                        symbolFound = True
                        #print(partNumber+" has a NEXT symbol")
                        sliding = False
                        break
                    elif nextChar in numberChars:
                        colOffset+=1#move our selection to the right and keep adding to it.
                        partNumber=partNumber+nextChar #need to extend our string of numbers.
                        skipBy+=1#this will act as our "skip" for the string of numbers when we return to the main loop.
                    else:
                        sliding = False #if it's not a symbol or a number it's a dot - but we still haven't checked the verticals
                        if not symbolFound:#if we still haven't found a symbol from the back column or the verticals.
                            topRight = ""
                            botRight = ""

                            if(rowCount-1>=0):
                                topRight=grid[rowCount-1][colOffset+1]
                            if(rowCount+1<rowMax):
                                botRight = grid[rowCount+1][colOffset+1]

                            if topRight in symbols or botRight in symbols:
                                symbolFound = True
                                #print(partNumber+" has a forward symbol")
                else:
                    sliding = False#if we're at the end of the row, return what we have.

        if symbolFound:
            print(partNumber+" is a partnumber, row: "+str(rowCount)+", col"+str(colCount))
            #Total+=int(partNumber)
            numbLoc.append(StrAndPos(partNumber,rowCount,colCount))
            symbolFound = False
        elif(len(partNumber)>0):
            print(partNumber+" is NOT a partnumber, row: "+str(rowCount)+", start col"+str(colCount))
        colCount+=1
        #print(colCount)
    rowCount+=1


#let's just check we're getting them correctly.
for gear in gearsLoc:
    print("gear "+"row: "+str(gear.rowPos)+" col:"+str(gear.colPos))

for partNumb in numbLoc:
    print(partNumb.str+" row: "+str(partNumb.rowPos)+" col:"+str(partNumb.colPos))

multiTotal = 0
failText = ""
for gear in gearsLoc:
    adjacentNumbs = []
    for partNumb in numbLoc:
        if abs(gear.rowPos-partNumb.rowPos)<=1: #if within one row.
            if(
                gear.colPos>=partNumb.colPos-1
                and 
                gear.colPos<=(partNumb.colPos+len(partNumb.str))
                ):#If the column for gear is within -1 of the start of the partNumb, and within the +1 of the partNumbs last digit - it's adjecent
                adjacentNumbs.append(partNumb.str)
    if len(adjacentNumbs)==2:#If we have 2 partnumbs
        multiTotal+=int(adjacentNumbs[0])*int(adjacentNumbs[1])#multiply them together and add them to the running total.
        print("R:"+str(gear.rowPos)+"C:"+str(gear.colPos)+"is beside "+adjacentNumbs[0]+" and "+adjacentNumbs[1])
    elif len(adjacentNumbs)==1:
        print("R:"+str(gear.rowPos)+"C:"+str(gear.colPos)+"has only one adjacent"+adjacentNumbs[0])
    elif len(adjacentNumbs)==0:
        print("R:"+str(gear.rowPos)+"C:"+str(gear.colPos)+"has no adjacent")
    else:
        print("R:"+str(gear.rowPos)+"C:"+str(gear.colPos)+" ...something has gone wrong."+str(len(adjacentNumbs)))
        for aNumb in adjacentNumbs:
            print(aNumb)

print("Multiplied gear parts: "+str(multiTotal))