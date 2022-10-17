import random

def drawBoard(board):

    print(' ' + board[7] + ' │ ' + board[8] + ' │ ' + board[9])
    print('───┼───┼───')
    print(' ' + board[4] + ' │ ' + board[5] + ' │ ' + board[6])
    print('───┼───┼───')
    print(' ' + board[1] + ' │ ' + board[2] + ' │ ' + board[3])

def inputPlayerLetter():

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('진영을 선택해 주세요. (X,O)중에 선택해주세요 ')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():

    print('다시하겠습니다? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):

    board[move] = letter

def isWinner(bo, le):

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):

    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):

    return board[move] == ' '

def getPlayerMove(board):

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):

        print('다음 수를 두세요 (1 ~ 9)\n 배열의 순서는 컴퓨터의 숫자판 순서입니다.')
        move = input()

    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Tic Tac Toe 게임을 시작합니다!')

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + '가 먼저 시작하겠습니다.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('당신이 이겼습니다!')
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('비겼습니다')
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('당신이 졌습니다')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('비겼습니다')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break

