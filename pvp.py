#import game class
import Game
#create instance of Game from Game class
game = Game.Game()
#set player
player =1

while(game.isOver() == False ):
    if (player ==1):
        print("player", player, "'s turn.")
        move = int(input("enter move: "))
        if(game.place(move, player)):
            if game.isOver():
                print("player", player, "wins!")
            game.displayBoard()
            player =2
        else:
            print("invalid move, please try again")

    else:
        print("player", player, "'s turn.")
        move = int(input("enter move: "))
        if(game.place(move, player)):
            if game.isOver():
                print("player", player, "wins!")
            game.displayBoard()
            player =1
        else:
            print("invalid move, please try again")


