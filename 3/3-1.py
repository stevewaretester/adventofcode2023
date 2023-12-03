#https://adventofcode.com/2023/day/3
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


#example lines
lines = ["467..114.."
         ,"...*......"
         ,"..35..633."
         ,"......#..."
         ,"617*......"
         ,".....+.58."
         ,"..592....."
         ,"......755."
         ,"...$.*...."
         ,".664.598.."]

numberChars= ["0","1","2","3","4","5","6","7","8","9"] #numbers as characters for easy comparison, could do this programmatically but I'm lazy.

symbols = [] #we need to know what the special symbols are
grid = [[]] #setup a 2d array for easy manipulation

###Setting up the grid and getting all the symbols.
rowCount = 0
for line in lines:
    for character in line.rstrip('\n'):#get rid of the newline symbol
###1 - Get all the symbols
        if not character in symbols and not character in numberChars and not character==".":
            symbols.append(character) #we want to know all the special characters used to denote stuff - i.e anything not a number or a dot (or a newline)
###2 - Load the grid so it can be manipulated as a 2d array.
        grid[rowCount].append(character)#add this column to the grid
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
rowCount = 0 #we'll likely need this at some point.

rowLoop = True#keep looping ROWS while this is true
#while rowLoop:
for row in grid:
    #print(row)
    colMax = len(grid)
    rowMax = len(grid[0])


    symbolFound = False #can use this to early-exit searching for symbols.
    skipBy = 0#we can use this to skip the next few columns - eg if we've found a number string
    colCount = 0
    colLoop = True#keep looping ROWS while this is true
    
    for col in row:
        if(skipBy>0):#We've already captured this number, might as well skip.
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
            if(colCount-1<=0 and rowCount+1<rowMax):#back one, below one - check they aren't out of bounds
                print(str(rowCount)+"/"+str(rowMax))
                botLeft = grid[rowCount+1][colCount-1]

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
                        print(grid[rowCount][colOffset]+" has a vertical symbol")

                if colOffset+1<colMax:#if there's any space right:
                    nextChar = grid[rowCount][colOffset+1]
                    
                    if nextChar in symbols:
                        symbolFound = True
                        print(partNumber+" has a NEXT symbol")
                        sliding = False
                        break
                    elif nextChar in numberChars:
                        colOffset+=1#move our selection to the right and keep adding to it.
                        partNumber=partNumber+nextChar #need to extend our string of numbers.
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
                                print(partNumber+" has a forward symbol")
        if symbolFound:
            #print(partNumber+" is a partnumber")
            Total+=int(partNumber)
            symbolFound = False
        colCount+=1
    rowCount+=1

print(str(Total))













#check each number as adjacent to a symbol

#top left = -1col, -1row
#top mid = 0 col, -1 row
#top right = +1 col, -1 row
#behind = -1 col, 0 row
#infront = -1 col, 0 row
#bot left = -1col, +1row
#bot mid = 0 col, +1 row
#bot right = +1 col, +1 row

#second a number is found as adjacent - identify the entire string.