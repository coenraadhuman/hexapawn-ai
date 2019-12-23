import random
import time
from colorama import init, Fore, Style
init(autoreset=True)

class State:
    playerOneSymbol = "x"
    playerTwoSymbol = "o"

    def __init__(self):
        self.arr = [[self.playerOneSymbol, self.playerOneSymbol, self.playerOneSymbol], [" ", " ", " "], [self.playerTwoSymbol, self.playerTwoSymbol, self.playerTwoSymbol]]
        self.newGame = True
        self.previousState = []
        self.nextStates = []
        self.notFirstState = False
        self.points = 50
        self.name = self.playerOneSymbol + self.playerOneSymbol + self.playerOneSymbol + " " + " " + " " + self.playerTwoSymbol + self.playerTwoSymbol + self.playerTwoSymbol
        
    def change(self, row, col, value):
        self.newGame = False
        self.arr[row][col] = value
        self.generateNewName()
        
    def generateNewName(self):
        self.name = ""
        for row in self.arr:
            for col in row:
                self.name += col
                
    def deepCopy(self):
        state = State()
        newArr = []
        for row in self.arr:
            newRow = []
            for col in row:
                newRow.append(col)
            newArr.append(newRow)
        state.arr = newArr
        state.newGame = self.newGame
        state.nextStates = self.nextStates
        state.name = self.name
        state.previousState = self
        state.notFirstState = True
        return state
        
    def prettyPrint(self):
        for row in self.arr:
            print(row)
        print()
        
    def decisionPrettyPrint(self):
        for row in self.arr:
            print(Fore.YELLOW + str(row))
        print()

class Decision:
    def __init__(self, state):
        self.state = state
        self.start = 0
        self.end = 0

class Player:
    def __init__(self, type):
        self.isPlayerOne = type
        self.decisionsMade = []
        
    def move(self, state):
        # check if all my pawns are taken.
        if self.checkPawns(state):
            print()
            if self.isPlayerOne:
                print("Player one does not have any pawns left. Player two wins!")
                print()
                playerOne.reducePoints()
                playerTwo.increasePoints()
            else:
                print("Player two does not have any pawns left. Player one wins!")
                print()
                playerOne.increasePoints()
                playerTwo.reducePoints()
            return self.getFirstState(state)
        else:
            # check if state is stored on storage.
            
            # else generate.
            if len(state.nextStates) == 0:
                self.generateNextStates(state)
                print()
                print(Fore.GREEN + "Generating next states for current state.")
            # decide which state to return.
            totalPoints = 0
            decisions = []
            for x in state.nextStates:
                decisions.append(Decision(x))
                totalPoints = totalPoints + x.points                
            print()
            # calculate ranges.
            isAllZero = True
            for y in range(len(decisions)):
                if decisions[y].state.points != 0:
                    print("-> Decision " + str(y) + ": " + str((decisions[y].state.points / totalPoints) * 100) + "% to be chosen.")
                    decisions[y].state.decisionPrettyPrint()
                    if y == 0:
                        decisions[y].end = int((decisions[y].state.points / totalPoints) * 100)
                    else:
                        decisions[y].start = decisions[y - 1].end + 1
                        decisions[y].end = decisions[y].start + int((decisions[y].state.points / totalPoints) * 100)
                    isAllZero = False
                else:
                    print("-> Decision " + str(y) + ": " + str(decisions[y].state.points) + "% to be chosen.")
                    decisions[y].state.decisionPrettyPrint()
            # make evenly distributed ranges.
            if isAllZero:
                print("Random decisions will be made.")
                print()
                for z in range(len(decisions)):
                    print("-> New random decision " + str(z) + ": " + str(100 / len(decisions)) + "% to be chosen.")
                    if z == 0:
                        decisions[z].start = 0
                        decisions[z].end = (100 / len(decisions))
                    else:
                        decisions[z].start = decisions[z - 1].end + 1
                        decisions[z].end = decisions[z].start + (100 / len(decisions))
                print()
            # generate random value.
            randomValue = random.randrange(0,101,1)
            # return state that value falls under.
            for z in decisions:
                if z.start <= randomValue:
                    if z.end >= randomValue: 
                        self.decisionsMade.append(z.state)
                        return z.state
            # no state is found, thus can't make a move and opponent wins.
            if self.isPlayerOne:
                print("Player one can't make a move. Player two wins!")
                print()
                playerOne.reducePoints()
                playerTwo.increasePoints()
            else:
                print("Player two can't make a move. Player one wins!")
                print()
                playerOne.increasePoints()
                playerTwo.reducePoints()
            return self.getFirstState(state)

    def checkPawns(self, state):
        lost = True
        for row in state.arr:
            for col in row:
                if self.isPlayerOne:
                    if col == state.playerOneSymbol:
                        lost = False
                else:
                    if col == state.playerTwoSymbol:
                        lost = False
        return lost
        
    def getFirstState(self, state):
        x = state
        while x.notFirstState:
            x = x.previousState
        return x
        
    def reducePoints(self):
        if self.isPlayerOne:
            print("Decreasing player one game moves' points.")
        else:
            print("Decreasing player two game moves' points.")
        for x in self.decisionsMade:
            if (x.points - 5) > 0:
                x.points = x.points - 5
            else:
                x.points = 0
        self.decisionsMade = []
                
    def increasePoints(self):
        if self.isPlayerOne:
            print("Increasing player one game moves' points.")
        else:
            print("Increasing player two game moves' points.")
        for x in self.decisionsMade:
            x.points = x.points + 5
        self.decisionsMade = []
    
    def generateNextStates(self, state):
        newStates = []
        # can I move forward?
        for i in range(len(state.arr)):
            for j in range(len(state.arr[i])):
                if self.isPlayerOne:
                    if state.arr[i][j] == state.playerOneSymbol:
                        if (len(state.arr) - 1) >= (i + 1):
                            # print("i: " + str(i) + " -> " + str(i + 1) + " of " + str(len(state.arr)))
                            if state.arr[i + 1][j] == " ":
                                newState = state.deepCopy()
                                newState.change(i, j, " ")
                                newState.change(i + 1, j, state.playerOneSymbol)
                                newStates.append(newState)
                else:
                    if state.arr[i][j] == state.playerTwoSymbol:
                        if 0 <= (i - 1):
                            # print("i: " + str(i) + " -> " + str(i - 1))
                            if state.arr[i - 1][j] == " ":
                                newState = state.deepCopy()
                                newState.change(i, j, " ")
                                newState.change(i - 1, j, state.playerTwoSymbol)
                                newStates.append(newState)
        # can I take the opponent's pawn on the left?
        for i in range(len(state.arr)):
            for j in range(len(state.arr[i])):
                if self.isPlayerOne:
                    if state.arr[i][j] == state.playerOneSymbol:
                        if (len(state.arr) - 1) >= (i + 1):
                            if (len(state.arr[i]) - 1) >= (j + 1):
                                # print("i: " + str(i) + " -> " + str(i + 1) + " of " + str(len(state.arr) - 1))
                                # print("j: " + str(j) + " -> " + str(j + 1) + " of " + str(len(state.arr[i]) - 1))
                                if state.arr[i + 1][j + 1] == state.playerTwoSymbol:
                                    newState = state.deepCopy()
                                    newState.change(i, j, " ")
                                    newState.change(i + 1, j  + 1, state.playerOneSymbol)
                                    newStates.append(newState)
                else:
                    if state.arr[i][j] == state.playerTwoSymbol:
                        if 0 <= (i - 1):
                            if 0 <= (j - 1):
                                # print("i: " + str(i) + " -> " + str(i - 1))
                                # print("j: " + str(j) + " -> " + str(j - 1))
                                if state.arr[i - 1][j - 1] == state.playerOneSymbol:
                                    newState = state.deepCopy()
                                    newState.change(i, j, " ")
                                    newState.change(i - 1, j - 1, state.playerTwoSymbol)
                                    newStates.append(newState)
        # can I take the opponent's pawn on the right?
        for i in range(len(state.arr)):
            for j in range(len(state.arr[i])):
                if self.isPlayerOne:
                    if state.arr[i][j] == state.playerOneSymbol:
                        if (len(state.arr) - 1) >= (i + 1):
                            if 0 <= (j - 1):
                                # print("i: " + str(i) + " -> " + str(i + 1))
                                # print("j: " + str(j) + " -> " + str(j - 1))
                                if state.arr[i + 1][j - 1] == state.playerTwoSymbol:
                                    newState = state.deepCopy()
                                    newState.change(i, j, " ")
                                    newState.change(i + 1, j  - 1, state.playerOneSymbol)
                                    newStates.append(newState)
                else:
                    if state.arr[i][j] == state.playerTwoSymbol:
                        if 0 <= (i - 1):
                            if (len(state.arr[i]) - 1) >= (j + 1):
                                # print("i: " + str(i) + " -> " + str(i - 1))
                                # print("j: " + str(j) + " -> " + str(j + 1))
                                if state.arr[i - 1][j + 1] == state.playerOneSymbol:
                                    newState = state.deepCopy()
                                    newState.change(i, j, " ")
                                    newState.change(i - 1, j + 1, state.playerTwoSymbol)
                                    newStates.append(newState)
        state.nextStates = newStates
        
# introduction
print("Hexapawn Machine Learning")
print()

# create board.
board = State()

# create players, there can only be a single 'player one'.
playerOne = Player(True)
playerTwo = Player(False)

# game wins.
playerOneScore = 0
playerTwoScore = 0

# ask amount of games to play.
games = int(input("Please enter number of games that should be played, using an interger value: "))
print()
print()

# measure simulation execution time.
start = time.time()
for x in range(games):
    # while loop till game is finished.
    print("-- Game has started --")
    print()

    continueGame = True
    playerOneToMove = True
    currentState = 0

    while continueGame:
        # print state number.
        # print()
        print(Fore.CYAN + "State " + str(currentState) + ":")
        board.prettyPrint()
        
        # determine which player will move.
        if playerOneToMove:
            print(Fore.MAGENTA + Style.BRIGHT + "Player one makes a move.")
            playerOneToMove = False
            board = playerOne.move(board)
        else:
            print(Fore.MAGENTA + Style.BRIGHT + "Player two makes a move.")
            playerOneToMove = True
            board = playerTwo.move(board)
            
        # end game if new board is made.
        if board.newGame:
            print()
            if playerOneToMove:
                print("-- Game has ended by player two --")
                playerOneScore = playerOneScore + 1
            else: 
                print("-- Game has ended by player one --")
                playerTwoScore = playerTwoScore + 1
               
            continueGame = False
            
        currentState = currentState + 1
        
        # player reached other side with move!
        for x in board.arr[0]:
            if x == board.playerTwoSymbol:
                print(Fore.CYAN + "State " + str(currentState) + ":")
                board.prettyPrint()
                print("Player two reached other side and wins! Player one loses!")
                print()
                playerOne.reducePoints()
                playerTwo.increasePoints()
                print()
                print("-- Game has ended by player two --")
                playerTwoScore = playerTwoScore + 1
                board = playerTwo.getFirstState(board)
                continueGame = False
        for x in board.arr[2]:
            if x == board.playerOneSymbol:
                print(Fore.CYAN + "State " + str(currentState) + ":")
                board.prettyPrint()
                print("Player one reached other side and wins! Player two loses!")
                print()
                playerOne.increasePoints()
                playerTwo.reducePoints()
                print()
                print("-- Game has ended by player one --")
                playerOneScore = playerOneScore + 1
                board = playerOne.getFirstState(board)
                continueGame = False
        if continueGame:
            badLogic = True
        else:
            print()
            print(Fore.RED + Style.BRIGHT + "Player one score: " + str(playerOneScore) + " and player two score: " + str(playerTwoScore))
            print()
end = time.time()
print(Fore.BLUE + Style.BRIGHT + "Simulation execution time: " + str(end - start) + " seconds.")
