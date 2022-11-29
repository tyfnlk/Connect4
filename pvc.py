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
            if temprow == 6:
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
            print("hello", temprow)

            if temprow <5:
                if temp.board[temprow + 1][i] == 1 and temp.board[temprow + 2][i] == 1:
                    print("return this")
                    temp.clear(i)
                    return i
            temp.clear(i)

    # place move in middle if not in danger to open up as much opportunities as possible
    if temp.isOpen(i) and temp.place(3, 1) != -1:
        temp.clear(3)
        return 3

    #make move that could help win
    for i in range(7):
        if temp.isOpen(i):
            temprow = temp.place(i,2)
            tempcount = 0
            if temprow == 6:
                for j in range(4):
                    if temp.board[temprow][j] == 0:
                        if temp.board[temprow][j + 1] == 2 and temp.board[temprow][j + 2] == 2 and temp.board[temprow][
                            j + 3] == 2 and temp.board[temprow][j + 4] == 0:
                            temp.clear(i)
                            return j+4
            temp.clear(i)

    # random move if not in danger of loss
    while True:
        x = int(random.randint(0, 7))
        print("get rand", x)
        if temp.isOpen(x) and temp.place(x, 1) != -1:
            temp.clear(x)
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
