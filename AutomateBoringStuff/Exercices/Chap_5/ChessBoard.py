import sys
print(sys.argv[])
chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
def isValidChessBoard(board):
    validPositionNumbers = ["1","2","3","4","5","6","7","8"]
    validPositionLetters = ["a","b","c","d","e","f","g","h"]
    validColors = ["b","w"]
    validPieces = ["pawn","king","queen","bishop","knight","rook"]
    for k,v in board.items():
        position = str(k)
        piece = str(v)
        if position[0] not in validPositionNumbers:
            return False
        if position[1:] not in validPositionLetters:
            return False
        if piece[0] not in validColors:
            return False
        if piece[1:] not in validPieces:
            return False
    return True

print(isValidChessBoard(chessBoard))



