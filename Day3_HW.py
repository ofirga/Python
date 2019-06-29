
#Exercise 7
'''list = ['Ofir', 'Gal', 'TomER']
print(list)

for word in list:
    print(word.lower())
'''

#Exercise 8
'''list = ['Ofir', 'Gal', 'TomER']
print(list)
NewList=[]
for word in list:
    for letter in word:
        NewList.extend(letter)
print (NewList)
'''
#Exercise 9

Matrix = [[5 ,5 ,5] ,[1 ,-9 ,44 ,7] ,[-20 ,10 ,5]]
LowestList_Sum = 0
LowestList_Index = 0
i=0
for list in Matrix:
    sum = 0
    for item in list:
        sum+=item
    if sum < LowestList_Sum:
        LowestList_Sum = sum
        LowestList_Index = i
    i = i+1
print (f' The sum of the smallest list is: {LowestList_Sum} and is located in location {LowestList_Index}')
