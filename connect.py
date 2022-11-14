#create gameboard
board = [[0 for i in range(7)] for x in range(7)]


def checkRow(row: int):
    if (row < 7 and row >-1):
        print("hio")

def place(row: int, player: int):
    for i in reversed(range(7)):
        if board[i][row] == 0:
            board[i][row] = player
            return True
    return False

#checks if game is over
def isOver():
    #check for win condition
    for i in range(7):
        for j in range(7):
            if(board[i][j] == 1 or board[i][j]==2):
                temp = board[i][j]
                count=1
               #check across
                if(j+3 <7):
                    for h in range(3):
                        if board[i][j+h] == temp:
                            count += 1
                    if count == 4:
                        print("player ", temp, " wins!")
                        return True
                    else:
                        count = 1

                #check below
                if(i+3<7):
                    for h in range(3):
                        if board[i+h][j] == temp:
                            count += 1
                    if count == 4:
                        print("player ", temp, " wins!")
                        return True
                    else:
                        count = 1

                #check down right
                if (i + 3 < 7 and j + 3 < 7):
                    for h in range(3):
                        if board[i+h][j+h] == temp:
                            count += 1
                    if count == 4:
                        print("player ", temp, " wins!")
                        return True
                    else:
                        count = 1

                #check down left
                if (i + 3 < 7 and j - 3 > -1):
                    for h in range(3):
                        if board[i+h][j-h] == temp:
                            count += 1
                    if count == 4:
                        print("player ", temp, " wins!")
                        return True
                    else :
                        count =1
    #check for full board
    for i in range(7):
        if(board[0][i] == 0):
            print("game not over")
            return False
    else:
        print("Game Draw!")
        return True

def displayBoard():
    print("--------------------")
    for i in range(7):
        for j in range(7):
            print(board[i][j], end ="  ")
        print('')
    print("--------------------")


