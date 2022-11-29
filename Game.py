class Game:
    def __init__(self):
        # create gameboard
        self.board = [[0 for i in range(7)] for x in range(7)]

    def setBoard(self, board: list):
        self.board = board

    def place(self, row: int, player: int):
        for i in reversed(range(7)):
            if self.board[i][row] == 0:
                self.board[i][row] = player
                return i
        return -1


    def clear(self, row: int):
        #iterate through each row
        for i in (range(7)):
            if self.board[i][row] != 0:
                self.board[i][row] = 0
                return True
        return False

# check if col is full
    def isOpen(self, row: int):
        if self.board[0][row] != 0:
            return False
        return True

    # checks if game is over
    def isOver(self):
        # check for win condition
        for i in range(7):
            for j in range(7):
                if (self.board[i][j] == 1 or self.board[i][j] == 2):
                    temp = self.board[i][j]
                    count = 0
                    # check across
                    if (j + 3 < 7):
                        for h in range(4):
                            if self.board[i][j + h] == temp:
                                count += 1
                        if count == 4:
                            #print("player ", temp, " wins!")
                            return True
                        else:
                            count = 0

                    # check below
                    if (i + 3 < 7):
                        for h in range(4):
                            if self.board[i + h][j] == temp:
                                count += 1
                        if count == 4:
                            #print("player ", temp, " wins!")
                            return True
                        else:
                            count = 0

                    # check down right
                    if (i + 3 < 7 and j + 3 < 7):
                        for h in range(4):
                            if self.board[i + h][j + h] == temp:
                                count += 1
                        if count == 4:
                            #print("player ", temp, " wins!")
                            return True
                        else:
                            count = 0

                    # check down left
                    if (i + 3 < 7 and j - 3 > -1):
                        for h in range(4):
                            if self.board[i + h][j - h] == temp:
                                count += 1
                        if count == 4:
                            #print("player ", temp, " wins!")
                            return True
                        else:
                            count = 1
        # check for full board
        for i in range(7):
            if (self.board[0][i] == 0):
                # print("game not over")
                return False
        else:
            print("Game Draw!")
            return True

    def displayBoard(self):
        print("--------------------")
        print("0  1  2  3  4  5  6")
        print("--------------------")
        for i in range(7):
            for j in range(7):
                print(self.board[i][j], end="  ")
            print('')
        print("--------------------")
