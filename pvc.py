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

    # block potential win
    for i in range(7):
        if temp.isOpen(i) and temp.place(i, 1):
            if temp.isOver():
                temp.clear(i)
                return i
            temp.clear(i)

    # random move if not in danger of loss
    if temp.isOpen(i) and temp.place(3, 1):
        temp.clear(3)
        return 3

    while True:
        x = int(random.randint(0, 7))
        print("get rand", x)
        if temp.isOpen(x) and temp.place(x, 1):
            temp.clear(x)
            return x





while game.isOver() == False:
    if player == 1:
        print("player", player, "'s turn.")
        move = int(input("enter move: "))
        if game.isOpen(move):
            game.place(move,player)
            if game.isOver():
                print("player", player, "wins!")
            game.displayBoard()
            player = 2
        else:
            print("invalid move, please try again")

    else:
        print("player", player, "'s turn.")
        move = findMove(game.board.copy())
        time.sleep(2)
        if game.isOpen(move):
            game.place(move, player)
            if game.isOver():
                print("player", player, "wins!")
            game.displayBoard()
            player = 1
        else:
            print("invalid move, please try again")

