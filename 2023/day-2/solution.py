import numpy 

inventoryMax = { "red": 12, "green": 13, "blue": 14 }

def oneStarAnswer(data: str) -> int:
    possibleGamesCombined = 0
    for line in data:
        (gameId, subGames) = line.strip("\n").split(": ")
        gameId = gameId.strip("Game ")
        subGames = subGames.split("; ")
        
        if (isGamePossible(subGames)):
            possibleGamesCombined += int(gameId)
    return possibleGamesCombined
            
def isGamePossible(subGames: [str]) -> bool:
    for subGame in subGames:
        inGame = { "red": 0, "green": 0, "blue": 0 }
        turns = subGame.split(", ")

        for turn in turns:
            (amount, color) = turn.split(" ")
            inGame[color] += int(amount)

            if (not checkTurnValidity(inGame)):
                return False
    return True

def checkTurnValidity(inventory: {str : int}) -> bool:
    for color in inventory.keys():
        if inventory[color] > inventoryMax[color]:
            return False
    return True


def twoStarAnswer(data: str) -> int:
    total = 0
    for line in data:
        (gameId, subGames) = line.strip("\n").split(": ")
        gameId = gameId.strip("Game ")
        subGames = subGames.split("; ")
        total += getNumberOfCubesInGame(subGames)
    return total

def getNumberOfCubesInGame(subGames: [str]) -> int:
    inGame = { "red": 0, "green": 0, "blue": 0 }
    for subGame in subGames:
        turns = subGame.split(", ")
        for turn in turns:
            (amount, color) = turn.split(" ")
            if (inGame[color] < int(amount)):
                inGame[color] = int(amount)

    value = numpy.prod(list(inGame.values()))
    return value
        
def main():
    fr = open("data.txt", "r")
    data = fr.readlines()
    fr.close

    print("One star answer: " + str(oneStarAnswer(data)))
    print("Two star answer: ", str(twoStarAnswer(data)))

if __name__ == "__main__":
    main()
    