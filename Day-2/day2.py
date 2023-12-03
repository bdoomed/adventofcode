def partOne():
    with open('input.txt', 'r') as games:

        rules = {
            "numRed": 12,
            "numGreen": 13,
            "numBlue": 14
        }

        totalValue = 0

        for game in games:
            game = game.strip()
            print(game)
            game = game.split(': ')
            gameID = game[0].split(" ")[1]
            # print(gameID)
            grabs = game[1].split("; ")
            possibility = True
            for grab in grabs:
                # print(grab)
                colors = grab.split(", ")
                # print(colors)
                numRed = 0
                numGreen = 0
                numBlue = 0

                for color in colors:
                    if "red" in color:
                        numRed += int(color.split(" ")[0])
                        # print(numRed)
                        if numRed > rules['numRed']:
                            print("Red limit exceeded: ", numRed, " is more than ", rules['numRed'])
                            possibility = False
                    if "green" in color:
                        numGreen += int(color.split(" ")[0])
                        # print(numGreen)
                        if numGreen > rules['numGreen']:
                            print("Green limit exceeded: ", numGreen, " is more than ", rules['numGreen'])
                            possibility = False
                    if "blue" in color:
                        numBlue += int(color.split(" ")[0])
                        # print(numBlue)
                        if numBlue > rules['numBlue']:
                            print("Blue limit exceeded: ", numBlue, " is more than ", rules['numBlue'])
                            possibility = False
            if possibility:
                print("Game is possible. Game ID is ", gameID, " and it will be added to the total.")
                totalValue += int(gameID)
                print(totalValue)
            else:
                print("Game ", gameID, " is impossible.")
        print("Part One Answer: ", totalValue)
partOne()

def partTwo():
    with open('input.txt', 'r') as games:
        totalValue = 0
        for game in games:
            game = game.strip()
            print(game)
            game = game.split(': ')
            gameID = game[0].split(" ")[1]
            # print(gameID)
            grabs = game[1].split("; ")

            numRed = 0
            numBlue = 0
            numGreen = 0

            for grab in grabs:
                # print(grab)
                colors = grab.split(", ")
                print(colors)
                for color in colors:
                    if "red" in color:
                        if numRed < int(color.split(" ")[0]):
                            numRed = int(color.split(" ")[0])
                    if "green" in color:
                        if numGreen < int(color.split(" ")[0]):
                            numGreen = int(color.split(" ")[0])
                    if "blue" in color:
                        if numBlue < int(color.split(" ")[0]):
                            numBlue = int(color.split(" ")[0])
                print("Max red: ", numRed)
                print("Max green: ", numGreen)
                print("Max blue: ", numBlue)
            gamePower = numRed * numBlue * numGreen
            totalValue += gamePower
        print("Part Two Answer: ", totalValue)

partTwo()