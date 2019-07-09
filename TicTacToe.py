#-------------------------------------------------------------
# Written By Ofir Gavish
# Date: 09/07/19
# Name: Tic Tac Toe Game
#-------------------------------------------------------------

#Function that checks if the player last played won
def isWinner(row, column):
    winner = True
    player = list[row][column]

# Check if player won in column
    for n in range(0,2+1):
        if list[row][n] != player:
            winner = False
    if winner:
        return True
    else:
        winner = True

# Check if player won in row
    for n in range(0,2+1):
        if list[n][column] != player:
            winner = False
    if winner:
        return True

# Check if player won in diagonal
    if list[0][0] == player and list[1][1] == player and list[2][2] == player:
        return True
    if list[2][0] == player and list[1][1] == player and list[0][2] == player:
        return True
def printStatus():
    for n in range(0, 2 + 1):
        string = "[ "
        for m in range(0, 2+1):
            if list[n][m] == '_':
                string = string + '_ '
            elif list[n][m] == 'X':
                string = string + 'X '
            else:
                string = string + 'O '
        string = string + "]"
        print(string)

EmptyList = [['_','_','_'],['_','_','_'],['_','_','_']]
list = EmptyList.copy()
count = 0
player = 'X'
while True:
    printStatus()
    print(f"Player {player} - Your turn")
    location = input("Enter location of cell: Row Cell: ")

# row and column will hold the int value of the new cell that the player chose
    row,column = location.split()
    row = int(row)
    column = int(column)

# If cell is not in range -> Ignore and input a different cell
    if row < 0 or row > 2 or column < 0 or column > 2:
        print("Incorrect cell location. Try again")
        continue
# If the cell is not empty -> Ignore and input a different cell
    if list[row][column] != "_":
        print("Cell taken. Choose different Cell")
        continue

#Enter the value of X or O - Player holds the corrent value.
    list[row][column] = player
    count += 1
    if isWinner(row,column):
        print(f'We have a winner! Player {player} won the game')
        printStatus()
        break

# If there isn't a winner and all cells are taken, declare a tie
    if count == 9:
        print("Tie! Try Again")
        list = EmptyList.copy()
        count = 0
        printStatus()
        continue

# Change the player's turn
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
