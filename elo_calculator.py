import math
print("Enter Player 1 Elo: ")
playerOneElo = int(input())
print("Enter Player 2 Elo: ")
playerTwoElo = int(input())

k = 40
d = 600

#Outcome is 1 when player 1 wins and 0 when player 1 loses
print("Enter Outcome (1 for P1 win, 0 for P2 loss")
outcome = int(input())
if not (outcome == 0) or (outcome == 1):
    raise Exception("Invalid outcome")
   
Ea = 1 / (1 + math.pow(10, ((playerTwoElo - playerOneElo) / d))) 
print("Expected odds of player 1 win " + str(Ea))

playerOneNewElo = playerOneElo + k * (outcome - Ea)
playerOneNewElo = int(playerOneNewElo)

playerTwoNewElo = playerTwoElo + k * ((1 - outcome) - (1 - Ea))
playerTwoNewElo = int(playerTwoNewElo)


print("New Player One Elo: "  + str(playerOneNewElo))
print("New Player Two Elo: "  + str(playerTwoNewElo))
