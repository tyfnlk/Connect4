# import game class
import time
import random
import Game


# create instance of Game from Game class
game = Game.Game()
# set player
player = 1


def findMove(board: list):
    temp = Game.Game()

    temp.setBoard(board.copy())
    #check for potential win in next move
    for i in range(7):
        if temp.isOpen(i) and temp.place(i,2) !=-1:
            if temp.isOver():
                temp.clear(i)
                return i
            temp.clear(i)


    # block potential win on next move
    for i in range(7):
        if temp.isOpen(i) and temp.place(i, 1) != -1:
            if temp.isOver():
                temp.clear(i)
                return i
            temp.clear(i)

    # premptive block for 2 in a row across
    for i in range(7):
        if temp.isOpen(i):
            temprow = temp.place(i,1)
            tempcount = 0
            if temprow == 5:
                for j in range(4):
                    if temp.board[temprow][j] == 0:
                        if temp.board[temprow][j + 1] == 1 and temp.board[temprow][j + 2] == 1 and temp.board[temprow][
                            j + 3] == 1 and temp.board[temprow][j + 4] == 0:
                            temp.clear(i)
                            return j+4
            temp.clear(i)

    #check for any possible 2 in a row stacks

    for i in range(7):
        if temp.isOpen(i):

            temprow = temp.place(i,1)
            if temprow <4 and temprow >1:
                if temp.board[temprow + 1][i] == 1 and temp.board[temprow + 2][i] == 1:
                    temp.clear(i)
                    return i
            temp.clear(i)

    # place move in middle if not in danger to open up as much opportunities as possible
    if temp.isOpen(3):
        return 3

    for i in range(7):
        if temp.isOpen(i):
            j=temp.place(i,2)
            count =0
            #check across
            if (j + 3 < 6):
                for h in range(3):
                    if temp.board[i][j + h] == 2:
                        count += 1
                if count == 3:
                    temp.clear(i)
                    return i
                else:
                    count =0
            # check below
            if (i + 3 < 6):
                for h in range(3):
                    if temp.board[i + h][j] == temp:
                        count += 1
                if count == 3:
                    temp.clear(i)
                    return i
                else:
                    count = 0
            # check down right
            if (i + 3 < 6 and j + 3 < 6):
                for h in range(3):
                    if temp.board[i + h][j + h] == temp:
                        count += 1
                if count == 3:
                    temp.clear(i)
                    return i
                else:
                    count = 0
            # check down left
            if (i + 3 < 6 and j - 3 > -1):
                for h in range(4):
                    if temp.board[i + h][j - h] == temp:
                        count += 1
                if count == 4:
                    temp.clear(i)
                    return i

            temp.clear(i)





    # if not in danger and no move could be identified that pose significant advantage presently,
    #place marker in least advantageous position of opponent

    for x in range(6):
        #test 2 in random spot
        if temp.isOpen(x) and temp.place(x, 2) != -1:
            #check if placement opens win for oponent
            if not temp.isOpen(x):
                temp.clear(x)
                return x
            else:
                temp.place(x,1)
                if temp.isOver():
                    temp.clear(x)
                    temp.clear(x)
                else:
                    temp.clear(x)
                    temp.clear(x)
                    return x

    while True:
        x = int(random.randint(0, 6))
        if temp.isOpen(x):
            return x


while game.isOver() == False:
    if player == 1:
        print("player", player, "'s turn.")
        move = int(input("enter move: "))
        if game.isOpen(move):
            game.place(move, player)
            if game.isOver():
                print("player", player, "wins!")
            game.displayBoard()
            player = 2
        else:
            print("invalid move, please try again")

    else:
        print("player", player, "'s turn.")
        move = findMove(game.board.copy())
        time.sleep(1)
        if game.isOpen(move):
            game.place(move, player)
            if game.isOver():
                print("player", player, "wins!")
            game.displayBoard()
            player = 1
        else:
            print("invalid move, please try again")
