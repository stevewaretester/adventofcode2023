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

lines = txtToLineArray(os.path.join(sys.path[0],"example.txt"))

###Classes
class handBidTypeRank:
    def __init__(self, hand, bid, numHand=None, type=None, rank=None):     
        self.hand = hand
        self.bid = bid
        self.numHand=[]
        self.type = type
        self.rank = rank

###Functions
def cardValueReturn(checkChar):
    nonNumericCards = ["A","K","Q","J","T"]
    if checkChar in nonNumericCards:
        x=nonNumericCards.index(checkChar)
        return 13-int(x-1)
    elif int(checkChar) in range(0,10):
        return int(checkChar)

def handType(hand):
    #tHand = hand
    uniqueCards = list(set(hand))
    if len(uniqueCards)==1: #Five of a kind, where all five cards have the same label: AAAAA
        return 6 #"Five of a kind"
    
    if len(uniqueCards)==2:
        if hand.count(uniqueCards[0])==3 or hand.count(uniqueCards[0])==2:#Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
            return 5 #"Full house"
        else:#Four of a kind, where four cards have the same label and one card has a different label: AA8AA
            return 4 #"Four of a kind"
        
    if len(uniqueCards)==3:
        if hand.count(uniqueCards[0])==3 or hand.count(uniqueCards[1])==3 or hand.count(uniqueCards[2])==3:#Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
            return 3#Three of a kind
        else:#Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
            return 2#Two pair
        
    if len(uniqueCards)==4:#One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        return 1#"One pair",  
    
    if len(uniqueCards)==5:#High card, where all cards' labels are distinct: 23456
        return 0#"High card"

def getOriginalHandIndex(bunchahands, inhand):
    index = 0
    for thing in bunchahands:
        if thing.hand == inhand:
            return index
        index+=1

###The actual program
maxRank=len(lines)

allHands = []#this will be our processed hands.

###Process lines, extra hands and bets
for line in lines:
    handBet = line.split()
    allHands.append(handBidTypeRank(handBet[0],handBet[1]))

presentTypes=set()#set to gather all the unique items

for aHand in allHands:#Let's get the types for each hand
    aHand.type = handType(aHand.hand)
    #print("hand: "+aHand.hand+" bid: "+aHand.bid+" type:"+str(aHand.type))
    presentTypes.add(aHand.type)#add it, if it's unique it'll get added.
    for card in aHand.hand:#might as well convert the hands while we're here
        aHand.numHand.append(cardValueReturn(card))
    print(aHand.numHand)

#print(presentTypes)
allTypes=list(presentTypes)#convert the set into a list, .
#allTypes.reverse()#reverse the order - this will give us largest to smallest
#print(allTypes)

allHands.sort(key=lambda x: x.type, reverse=True)

#Now we need to rank the individual sets of hands#
#previousRank = 0
rankingUp = 0
for typechunk in allTypes:
    ofThisType = list(filter(lambda aHand: aHand.type == typechunk, allHands))#get just the hands of this type so we can compare them.
    manyThisType = len(ofThisType)#get the length of this type, we'll need this for ranking.

    print("there are "+str(manyThisType)+" of type "+str(typechunk))
    
    #now go down the columns filtering by smallest size, then the next smallest, the the next...
        

    

            
    #print(getOriginalHandIndex(allHands, aHand.hand))
