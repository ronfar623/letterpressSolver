wordList = open("words.txt", "rt").read().splitlines()
wordList.sort(key=len, reverse=True)

def get_gameBoard():
    print('Enter the letters on each line on the game board')
    print('separated by spaces, for example: "a b c d e".')
    line1 = str(input("Line 1: "))
    line2 = str(input("Line 2: "))
    line3 = str(input("Line 3: "))
    line4 = str(input("Line 4: "))
    line5 = str(input("Line 5: "))
    gameBoard = (line1 + " " + line2 + " " + line3 + " " + line4 + " " + line5)
    gameBoard = gameBoard.split()
    return gameBoard


def solver(gameBoard, word):
    counter = 1
    counterBreak = len(word)
    for letter in word:
        if counter == counterBreak and letter in gameBoard:
            return word
        elif letter in gameBoard:
            del gameBoard[(gameBoard.index(letter))]
            counter += 1
        elif not letter in gameBoard:
            return


gameBoard = get_gameBoard()

while True:
    try:
        wordsReturned = int(input('How many words would you like returned? (Enter "-1" for all): '))
        break
    except ValueError:
            print('Oops!  That was not a valid number.  Please try again...')
wordCounter = 0
for word in wordList:
    tempBoard = gameBoard[:]
    if wordCounter == wordsReturned:
        break
    elif solver(tempBoard, word):
        print(word)
        wordCounter += 1
