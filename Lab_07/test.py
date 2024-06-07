# print 10 
# 0, 1, 2 ,...9
''' For Loop '''

for i in range (0,10):
    if i%2 == 0:
        print(str(i)+" is even")
    else:
        print(str(i)+" is odd")

''' While Loop '''
counter = 0 
while counter < 10:
    if counter % 2 == 0:
        print(str(counter)+" is even")
    else:
        print(str(counter)+" is odd")
    counter = counter + 1

''' list and for '''
lst = ["dog","cat","rat"]
for i in lst:
    print(i)

''' Dictionary and for '''
dict = {"Cat":8,"Dog":2,"Rat":10}
# animal name variables
for item in dict:
    print(item, dict[item])