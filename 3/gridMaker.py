lines = ["467..114..","...*......","..35..633.","......#...","617*......",".....+.58.","..592.....","......755.","...$.*....",".664.598.."]

array = []

array = [["1","2","3"],["4","5","6"]] #Easy Example array

print("LENGTH "+str(len(array)))

array = [[]] #mostly blank example array


print(array)

rowCount = 0
for line in lines:
    #array.append(line)
    print(line)
    for char in line:
        print(char)
        array[rowCount].append(char)
    rowCount+=1
    if len(array)<len(lines):
        array.append([])

rowCount = 0
for row in array:
    print(row)
    colCount = 0
    for col in row:
        #array[rowCount].append(str(col))
        print(array[int(rowCount)][int(colCount)])
        colCount += 1
    rowCount+=1

print(array)
print(array[0][0])
array[0][0]="boobs"
print(array[0][0])
print(array[1][2])
