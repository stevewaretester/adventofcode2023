print(int('1'*2))

list = ['a','b','c']
list.insert(3,'d')
print(list)

haha = ['test','baba','boohoo']
haha[1] = haha[1][:2] + 'Fu ' + haha[0][2:]
print(haha)

print('.'.isdigit())


#print('.......#.....#......'.count('#'))
string = '.......#.....#......'
#print(string.replace('#',"1"))
count = 1
for x in range(0,string.count('#')):
    string = string.replace('#',str(count),1)
    count+=1

print (string)

for i in haha:
    print(haha)
    haha.pop(0)