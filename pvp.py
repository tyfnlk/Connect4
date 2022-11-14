import Game

game = Game.Game()
player =1

while(game.isOver() == False ):
    if (player ==1):
        print("player", player, "'s turn.")
        move = int(input("enter move: "))
        if(game.place(move, player)):
            game.isOver()
            game.displayBoard()
            player =2
        else:
            print("invalid move, please try again")

    else:
        print("player", player, "'s turn.")
        move = int(input("enter move: "))
        if(game.place(move, player)):
            game.isOver()
            game.displayBoard()
            player =1
        else:
            print("invalid move, please try again")


