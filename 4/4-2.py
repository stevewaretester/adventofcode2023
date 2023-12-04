import os
import sys
import numbers


def txtToLineArray(txt):
    file = open(txt, "r")
    lines = file.readlines()
    file.close()
    return lines


class scratchCard:
    def __init__(self, cardNo, cardCount, won):
        self.cardNo = cardNo
        self.cardCount = cardCount
        self.won = won

#input file
input = os.path.join(sys.path[0],"input.txt")
lines = txtToLineArray(input)

###Example lines

#lines = txtToLineArray(os.path.join(sys.path[0],"example.txt"))


scratchStack = []
for line in lines:
    #print(line.rstrip('\n'))
    cardNumSplit = line.rstrip('\n').split(":")
    cardNum = cardNumSplit[0].split(" ")[1]
    winScoreSplit=cardNumSplit[1].split("|")
    winners = winScoreSplit[0].split()
    havenumbers = winScoreSplit[1].split()

    multiScore = 0
    for have in havenumbers:
        #print(have+" "+str(multiScore))
        if have in winners:
            multiScore+=1
            

    scratchStack.append(scratchCard(cardNum,1,multiScore))


stackSize = 0
listPos = 0#this keep strack of our index.
#For each scratchcard
for scratcher in scratchStack:
    #print("before Card "+scratcher.cardNo+", count: "+str(scratcher.cardCount)+", won: "+str(scratcher.won)+" Stack: "+str(stackSize))
    stackSize+=scratcher.cardCount
#get the score
    for x in range(scratcher.won):
        if((listPos+x+1)<len(scratchStack)):
            scratchStack[listPos+x+1].cardCount+=scratcher.cardCount
    listPos+=1


print("Stack of Scratchers = "+str(stackSize))