import os
import sys
import numbers


def txtToLineArray(txt):
    file = open(txt, "r")
    lines = file.readlines()
    file.close()
    return lines


class raceTimeDis:
    def __init__(self, pos, time, distance):     
        self.pos = pos
        self.time = time
        self.distance = distance


input = os.path.join(sys.path[0],"input.txt")
lines = txtToLineArray(input)

###Example lines

#lines = txtToLineArray(os.path.join(sys.path[0],"example.txt"))



times = lines[0].split()
del times[0]
print(times)
distances = lines[1].split()
del distances[0]
print(distances)

#winningMovesList = []    
winningMovesTotal = 1
for i in range(0,len(distances)):
    print("Tim: "+str(times[i])+" Dis: "+str(distances[i]))
    distance=int(distances[i])
    time=int(times[i])
    #let's calculate the minimum time it needs to be held in order to beat the distance
    mintime=0
    for heldTimeMin in range(1,time):
        travelled = heldTimeMin*(time-heldTimeMin)
        if travelled>distance:#must BEAT the record, not match it, so must be greater than.
            mintime=heldTimeMin
            break
    #calculate the maximum held time it needs to be held in order to beat the distance
    
    maxtime=0
    for heldTimeMax in range(time,mintime,-1):
        print(heldTimeMax)
        travelled = heldTimeMax*(time-heldTimeMax)
        print("Travelled: "+str(travelled))
        if travelled>distance:#we're waiting to LOSE the distance.
            maxtime=heldTimeMax
            break
    winningMoves=maxtime-mintime+1
    print("minTime: "+str(mintime),"maxTime: "+str(maxtime)+"numberOfWins: "+str(winningMoves))
    
    #winningMovesList.append(winningMoves)
    winningMovesTotal*=winningMoves

print("WinningMoves: "+str(winningMovesTotal))
    
