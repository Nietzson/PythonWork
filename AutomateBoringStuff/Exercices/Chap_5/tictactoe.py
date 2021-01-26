theBoard = {'top-L': '', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
while True:
    player1 = input("Player 1: ")
    if player1 not in theBoard.keys():
        print("You must enter a position on the grid!")
    elif theBoard[player1] != " ":
        print("You must enter an empty case, you filthy cheater!")
    else:
        theBoard[player1] = "X"
    printBoard(theBoard)
    player2 = input("Player 2: ")
    if player2 not in theBoard.keys():
        print("You must enter a position on the grid!")
    elif theBoard[player2] != " ":
        print("You must enter an empty case, you filthy cheater!")
    else:
        theBoard[player2] = "O"
    printBoard(theBoard)
