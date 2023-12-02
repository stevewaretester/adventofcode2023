#https://adventofcode.com/2023/day/2
import os
import sys


def txtToLineArray(txt):
    file = open(txt, "r")
    lines = file.readlines()
    file.close()
    return lines


input = os.path.join(sys.path[0],"input.txt")

lines = txtToLineArray(input)


#exampleLines
#lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green","Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue","Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red","Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red","Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

totalPower = 0
for line in lines:#split by lines
    print(line)

    impossGame = False#a boolean we can set to "true" when the game is impossible.

    #gameid = ""
    gameResultsplit = line.split(":")
    gameheader = gameResultsplit[0]
    #gameid = gameheader.split(" ")[1]#get the gameheader from the first half of the split, by splitting that half on a space and taking the second half(quarter?)
    
    #individualScores = gameResultsplit[1].replace(";",",").split(",")

    rounds = gameResultsplit[1].split(";")#split by semicolon into "rounds" eg. what cubes all appeared on the table at once.

    maxRed = 1#we need to know all the reds.
    maxGreen = 1#all the greens
    maxBlue = 1#all the blues
    
    for round in rounds:#going round-by-round...
        individualscore = round.split(",")#split these into individual pairins of cubes and scores

        for colourResult in individualscore:#each allocation of cubes.
            #print(colourResult)
            lstrippedCResult = colourResult.lstrip(' ').split(" ")#remove the leading space and split into two halves.
            colour = lstrippedCResult[1].rstrip('\n')#eg. blue, red, green (also remove the newline if there are any)
            result = int(lstrippedCResult[0])#eg. the numerical value
            
            if colour=="red":
                if result>maxRed:
                    maxRed=result
            elif colour=="green":
                if result>maxGreen:
                    maxGreen=result
            elif colour=="blue":
                if result>maxBlue:
                    maxBlue=result

    power = maxRed * maxGreen * maxBlue
    print("R: "+str(maxRed)+" G:"+str(maxGreen)+" B:"+str(maxBlue))
    print("P: "+str(power))
    totalPower += power

print("TotalPower: "+str(totalPower))