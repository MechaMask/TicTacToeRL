

class Game:
    def __init__(self, player1, player2):
        if(not(isinstance(player1, Player) or isinstance(player2, Player))):
            raise TypeError("player 1 and player2 must be of type \"Player\"")
        if(player1.type == player2.type):
            raise TypeError("player 1 and player2 can't have the same player type")
        if(player2.type == "x"):
            self.player1 = player2
            self.player2 = player1
        else:
            self.player1 = player1
            self.player2 = player2
        self.gameMatrix = self.createGame()
        self.isPlayer1turn = True
        self.player1IsWinner = False
        self.player2IsWinner = False
        self.gameOver = False
        self.turnsPlayed = 0
    def __repr__(self):
        return "Game("+str(self.player1)+','+str(self.player2)+')'
    def __str__(self):
        return "Game([X] "+str(self.player1)+",[O] "+str(self.player2)+')'
    def gameState(self):
        turnsPlayed = "Turns played: {turnsPlayed}\n".format(turnsPlayed=self.turnsPlayed)
        gameStateStr ="Current player: {currentPlayer}\n".format(currentPlayer=str(self.player1) if self.isPlayer1turn else str(self.player2)  ) + turnsPlayed
        for i in range(len(self.gameMatrix)):
            for j in range(len(self.gameMatrix[i])):
                gameStateStr = gameStateStr + self.gameMatrix[i][j]
            gameStateStr = gameStateStr + "\n"

        return gameStateStr
    def createGame(self):
        a1 = ["-"] * 3
        a2 = ["-"] * 3
        a3 = ["-"] * 3
        matrix = [a1,a2,a3]
        return matrix

    def setBoard(self,input,x,y):
        input = input.lower()
        if(not(input == "x" or input == "o")):
            raise TypeError("input can only be x or o")
        self.gameMatrix[x][y] = input

    def won(self):
        return self.columnWon() or self.rowWon() or self.diagonalWon()
    def columnWon(self):
        hasColumnWinnerP1 = False
        hasColumnWinnerP2 = False
        for i in range(len(self.gameMatrix)):
            hasColumnWinnerP1 = (self.gameMatrix[0][i] == self.gameMatrix[1][i] == self.gameMatrix[2][i] == self.player1.type)
            hasColumnWinnerP2 =  (self.gameMatrix[0][i] == self.gameMatrix[1][i] == self.gameMatrix[2][i] == self.player2.type)
            if(hasColumnWinnerP1 or hasColumnWinnerP2 ):
                self.player1IsWinner = hasColumnWinnerP1
                self.player2IsWinner = hasColumnWinnerP2
                self.gameOver = True
                return  True
        return False
    def rowWon(self):
        hasRowWinnerP1 = False
        hasRowWinnerP2 = False
        for i in range(len(self.gameMatrix)):
            hasRowWinnerP1 = (self.gameMatrix[i][0] == self.gameMatrix[i][1] == self.gameMatrix[i][2] == self.player1.type)
            hasRowWinnerP2 = ( self.gameMatrix[i][0] == self.gameMatrix[i][1] == self.gameMatrix[i][2] == self.player2.type)
            if(hasRowWinnerP1 or hasRowWinnerP2):
                self.player1IsWinner = hasRowWinnerP1
                self.player2IsWinner = hasRowWinnerP2
                self.gameOver = True
                return  True
        return False
    def diagonalWon(self):
        hasDiagonalWinnerP1 = False
        hasDiagonalWinnerP2 = False
        hasDiagonalWinnerP1 = (self.gameMatrix[0][0] == self.gameMatrix[1][1] == self.gameMatrix[2][2] == self.player1.type) or (self.gameMatrix[0][2] == self.gameMatrix[1][1] == self.gameMatrix[2][0] == self.player1.type)
        hasDiagonalWinnerP2 = (self.gameMatrix[0][0] == self.gameMatrix[1][1] == self.gameMatrix[2][2] == self.player2.type) or (self.gameMatrix[0][2] == self.gameMatrix[1][1] == self.gameMatrix[2][0] == self.player2.type)
        if(hasDiagonalWinnerP1 or hasDiagonalWinnerP2):
            self.player1IsWinner = hasDiagonalWinnerP1
            self.player2IsWinner = hasDiagonalWinnerP2
            self.gameOver = True
            return  True
        return False
    def reset(self):
        self.gameMatrix = self.createGame()

    def validPlay(self,input,x,y):
        if(self.gameMatrix[x][y] == "x" or self.gameMatrix[x][y] == "o"):
            return False
        return True

    def playTurn(self,input,x,y):
        input = input.lower()
        message = ""
        if(self.gameOver):
            message = "Invalid move the Game is over"
            print(message)
            return message
        if(self.isPlayer1turn):
            if(not(input == self.player1.type)):
                message = "Invalid input as "+self.player1.username
                print(message)
                return message
            if(not self.validPlay(input,x,y)):
                message = "can't overide this square please choose somewhere else"
                print(message)
                return message
            self.setBoard(input,x,y)
            message = "{player} played their turn".format(player = self.player1.username)
        if(self.isPlayer1turn == False):
            if(not(input == self.player2.type)):
                message = "Invalid input as "+self.player2.username
                print(message)
                return message
            if(not self.validPlay(input,x,y)):
                message = "can't overide this square please choose somewhere else"
                print(message)
                return message
            self.setBoard(input,x,y)

            message = "{player} played their turn".format(player = self.player2.username)

        if(self.turnsPlayed >= 4):
            if(self.won()):
                message = "{player} has won the game".format(player=str(self.player1) if self.player1IsWinner else str(self.player2))
                self.gameOver = True
        self.isPlayer1turn = not self.isPlayer1turn
        self.turnsPlayed = self.turnsPlayed + 1
        print(message)
        return message
class Player:
    def __init__(self,username,type):
        type = type.lower()
        if(not(type == "x" or type == "o")):
            raise TypeError("type must be either \"x\" or \"o\"")
        self.type = type
        self.username = username
    def __repr__(self):
        return self.username
    def __str__(self):
        return self.username
    def input(self,inp):
        return inp


def start(player1,player2,introComments):
    game = Game(player1,player2)
    print(game)
    if(introComments != ""):
        comment = introComments+"\n"
        print(introComments)
    print(game.gameState())
    return game

def startGame(username1,username2,introComments):
    player1 = Player(username1,"x")
    player2 = Player(username2,"o")
    game = Game(player1,player2)
    print(game)
    if(introComments != ""):
        comment = introComments+"\n"
        print(introComments)
    print(game.gameState())
    return game
def move(game,input,x,y,comment):
    game.playTurn(input,x,y)
    print(game.gameState())
    if(comment != ""):
        comment = comment+"\n"
        print(comment)
