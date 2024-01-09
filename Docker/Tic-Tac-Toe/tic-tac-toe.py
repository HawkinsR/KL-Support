#! /usr/bin/python3


import os
import random


def main( act = -1 ):
    print("Starting Tic-Tac-Toe")
    print("V 0.1")

    while ( act != 0 ):
        act = mainMenu()
        actionCall(act)
    print('Thanks for playing!')


def mainMenu():
    menu_items = ["[0] Exit the game", "[1] Play a round"]

    for ( i, value ) in enumerate(menu_items):
        print('{item}'.format(item = value))

    selection = -1

    while ( 0 > selection or 1 < selection ):
        try:
            selection = int(input('Please enter a number: '))
        except ValueError:
            print('Only numbers are accepted')

    clear()
    return selection


def actionCall( act ):
    if ( act == 1 ):
        win = 0
        player = ['X', 'O']
        moveCount =  0

        board = [['1', '|', '2', '|', '3'], [ '-', '-', '-', '-', '-'], ['4', '|', '5', '|', '6'], [ '-', '-', '-', '-', '-'], ['7', '|', '8', '|', '9']]
        while ( win != 1 ):
            printBoard(board)
            board = acceptMove(board, player[moveCount%2])
            printBoard(board)
            win = checkWin(board, str(player[moveCount%2]))
            if (win == 1):
                print(player[moveCount%2] + "'s Wins!")
            moveCount += 1


def printBoard(board):
    clear()
    for i in (board):
            print(' '.join(i))
    print("\n")
    return


def acceptMove(board, player):
    moveCompleted = False
    move = 0

    while (moveCompleted == False):
        move = input('Select a position [1-9]: ')
        for (i, x) in enumerate(board):
            for  (j, y) in enumerate(x):
                if ( move == board[i][j]):
                    board[i][j] = player
                    moveCompleted = True
                    return board


def checkWin(board, player):
    if ( board[0][0] == board[0][2] == board[0][4] == player):
        return 1
    elif (board[2][0] == board[2][2] == board[2][4] == player):
        return 1
    elif (board[4][0] == board[4][2] == board[4][4] == player):
        return 1
    elif (board[0][0] == board[2][0] == board[4][0] == player):
        return 1
    elif (board[0][2] == board[2][2] == board[4][2] == player):
        return 1
    elif (board[0][4] == board[2][4] == board[4][4] == player):
        return 1
    elif (board[0][0] == board[2][2] == board[4][4] == player):
        return 1
    elif (board[0][4] == board[2][2] == board[4][0] == player):
        return 1
    else:
        return 0


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


if __name__ == "__main__":
    main()
