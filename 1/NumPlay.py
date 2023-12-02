

inputList = ["1twoneighthree3nine4fiveightwosevenine5","two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen","five1oneightg"]
textNums = ["one","two","three","four","five","six","seven","eight","nine"]

#print(input)
#for lines in list


class numAndPos:
  def __init__(self, num, pos):
    self.num = num
    self.pos = pos

def findAllInstances(searchin, searchfor, actualInt):
    outputList = []
    lastpos = 0
    moreToFind = True
    while moreToFind:
        position = searchin.find(searchfor,lastpos)
        intpos = searchin.find(str(actualInt),lastpos)
        if position >=0:
            #print(str(searchfor+" @ "+str(position))) #capture the position of the thing
            lastpos = position + len(searchfor)
            outputList.append(numAndPos(actualInt,position))
        else:
            moreToFind = False
    return outputList


for line in inputList:
    print(line)
    count=0
    total = 0
    bigArray = []
    for textnum in textNums:#compare against the word-numbers
        count+=1
        if not(textnum in line):#early exit can skip if it's not in.
            #print("no "+textnum+"'s")
            continue#skipthisnumber
        output1 = findAllInstances(line,textnum,count)
        for thing in output1:
            bigArray.append(thing)


       



        #for thing in bigArray:
        #    for subthing in thing:
        #        print("num:"+str(subthing.num)+", pos:"+str(subthing.pos))
        #print(output)
        
        

    for i in range(1,10):
        if not(str(i) in line):#early exit can skip if it's not in.
            #print("no "+str(i)+"'s")
            continue
        output2 = findAllInstances(line,str(i),i)
        for thing in output2:
            bigArray.append(thing)
    
    bigArray.sort(key=lambda x: x.pos)
    
    for thing in bigArray:
        print("num:"+str(thing.num)+", pos:"+str(thing.pos))
    
    
    #for thing in bigArray:
        #print(thing.num)
    #    print("num:"+str(thing.num)+", pos:"+str(thing.pos))

    ### Do the same for Numerals
    #for i in range(1,10):
#    if not(str(i) in input):#early exit can skip if it's not in.
#        continue
#    findAllInstances(input,str(i),i)    

