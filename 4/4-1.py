import os
import sys
import numbers


def txtToLineArray(txt):
    file = open(txt, "r")
    lines = file.readlines()
    file.close()
    return lines


#input file
input = os.path.join(sys.path[0],"input.txt")
lines = txtToLineArray(input)

###Example lines
'''
example = os.path.join(sys.path[0],"example.txt")
lines = txtToLineArray(example)
'''
scoreTotal = 0
for line in lines:
    print(line.rstrip('\n'))                        #Splitting up this chunk of nonsense:
    #print(line.rstrip('\n'))                       #Card 1:  41 48 83 86 17 | 83 86  6 31 17  9 48 53 #raw
    cardNumSplit = line.rstrip('\n').split(":")     #Card 1>< 41 48 83 86 17 | 83 86  6 31 17  9 48 53 #break in 2
    cardNum = cardNumSplit[0].split(" ")[1]         #Card|1
    winScoreSplit=cardNumSplit[1].split("|")        #         41 48 83 86 17 ><83 86  6 31 17  9 48 53
    winners = winScoreSplit[0].split()              #         41|48|83|86|17  
    havenumbers = winScoreSplit[1].split()          #                          83|86| 6|31|17| 9|48|53
    
    print(cardNum)
    print(winners)
    print(havenumbers)
    
    multiScore = 0
    for have in havenumbers:
        #print(have+" "+str(multiScore))
        if have in winners:
            if multiScore<1:
                multiScore=1
            else:
                multiScore=multiScore*2
    #print(multiScore)
    scoreTotal+=multiScore

print("total: "+str(scoreTotal))