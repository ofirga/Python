#Exercise 8
'''for n in range(200,2 - 1,-1):
    print(n)
'''
#Exercise 9
'''for n in range(1,100 + 1):
    if n % 7 == 0:
        print(n)
'''
#exercise 10
'''
sum = 0
num = float(input("Please enter a number to be calculated int the sum. Negative number exits: "))
while (num >= 0):
    sum+=num
    num = float(input("Please enter a number to be calculated int the sum. Negative number exits: "))
print(f'The sum is: {sum}')

#exercise 11 - Azeret
num = int(input("Please enter a number for the azeret calculation: "))
sum = 1
for n in range (num, 1, -1):
    sum *= n
print (f'Azeret is: {sum}')
'''
#exercise 12
LuckListMaster = {11, 15, 21, 32, 40}
LuckList = LuckListMaster.copy()
NumGuesses = 0
while len(LuckList) > 0:
    num = int(input('Guess a number: '))
    NumGuesses += 1
    if (NumGuesses > 20):
        NumGuesses = 0
        LuckList = LuckListMaster.copy()
        print(f'Number of guesses more than 20. Starting from the beggining')
        continue
    if (num <2 or num > 49):
        continue
    if num in LuckList:
        print(f'Correct Guess!!!')
        LuckList.remove(num)
    elif num in LuckListMaster:
        print(f'You guessed that number! Game Over. Number of guesses up till now {NumGuesses}')
        break
    else:
        print(f'Wrong Guess!')

if (len(LuckList) == 0):
    print(f'Hurray! Good job. Guessed all numbers!')
    print(f'Number of guesses: {NumGuesses}')
