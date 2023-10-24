"""
 Project Title: TicTacToe
 Author: Nathan Sikkema
 Start Date: November 22, 2022
 End Date: December 01, 2022
 Total Duration: 8 Days

 Description:
    A text-based version of Tic Tac Toe.
    Special Features include:
        * Multiplayer
        * 5 different levels of difficulty
        * Instructions included
        * Color-coordinated Titles and Menus
 """
# Imports
import random  # Used to access pre-made time and randomization features
import time

class color:  # used to display the text-based program in an aesthetic manner
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ORANGE = '\033[33m'
    BOLD = '\033[1m'
    U_LINE = '\033[4m'
    ITALICS = '\x1B[3m'
    END = '\033[0m'


board = [[0 for x in range(3)] for y in range(3)]  # 3x3 nested list


#
# Functions
#

def getInteger(prompt):
    """
This is a pre-made function.
    Does not allow you to progress unless you enter a natural number.
    Examples:
        1     - is an integer       - Positive numbers are allowed!
        -1    - is an integer       - Negative numbers are allowed!
        a     - is NOT an integer   - Letters are not permitted.
        !     - is NOT an integer   - Symbols are not permitted.
        1.1   - is NOT an integer   - Decimals are not permitted.
        -1.1  - is NOT an integer   - Negative decimals are not permitted.
Credited to OVS, ICS3U
    """
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print(color.RED + color.BOLD + "\nThat is not an integer.\nPlease try again." + color.END)
            continue
        return num


# Gamemode - Novice, Easy, or Medium
def makeMove():
    """
    Generates a random number that is still available.
    Will return 0 if there are no positions remaining.
    """
    x = random.randint(1, 9)
    while numbers_taken.count(x) == 1:
        x += 1
        if x == 10:
            x = 0
    loc = x
    if loc == 0:
        x = 1
        while numbers_taken.count(x) == 1:
            x += 1
            if x == 10:
                x = 0
        loc = x
    return loc


# Gamemode - Hard
def makeMove_Hard(loc):
    '''
    Generates a position for the computer to go to in the Hard game mode. 
    5 is the best option for the computer to go at for its first move.
    otherwise, it plans a few strategic methods of approach.
    '''
    if numbers_taken.count(5) != 1:
        loc = 5
    elif playerX.count(5) and (
            numbers_taken.count(1) != 1 and numbers_taken.count(3) != 1 and numbers_taken.count(
        7) != 1 and numbers_taken.count(9) != 1):
        # If the player takes the middle, and that is the only point on the board, the best spot for the computer to go would be in the corner.
        gen = random.randint(1, 4)
        if gen == 1:
            if numbers_taken.count(1) != 1:
                loc = 1
        elif gen == 2:
            if numbers_taken.count(3) != 1:
                loc = 3
        elif gen == 3:
            if numbers_taken.count(7) != 1:
                loc = 7
        elif gen == 4:
            if numbers_taken.count(9) != 1:
                loc = 9
    elif ((numbers_taken.count(1) and computerO.count(5) and numbers_taken.count(9)) or (
            numbers_taken.count(3) and computerO.count(5) and numbers_taken.count(7))) and (
            numbers_taken.count(2) != 1 and numbers_taken.count(4) != 1 and numbers_taken.count(
        6) != 1 and numbers_taken.count(8) != 1):
        # This will force the computer to take a middle side point. It is more strategic this way.
        gen = random.randint(1, 4)
        if gen == 1:
            if numbers_taken.count(2) != 1:
                loc = 2
        elif gen == 2:
            if numbers_taken.count(4) != 1:
                loc = 4
        elif gen == 3:
            if numbers_taken.count(6) != 1:
                loc = 6
        elif gen == 4:
            if numbers_taken.count(8) != 1:
                loc = 8
    elif (playerX.count(5) and (
            playerX.count(1) or playerX.count(3) or playerX.count(7) or playerX.count(9))) and (
            numbers_taken.count(1) != 1 and numbers_taken.count(3) != 1 and numbers_taken.count(
        7) != 1 and numbers_taken.count(9) != 1):
        gen = random.randint(1, 4)
        if gen == 1:
            if numbers_taken.count(1) != 1:
                loc = 1
        elif gen == 2:
            if numbers_taken.count(3) != 1:
                loc = 3
        elif gen == 3:
            if numbers_taken.count(7) != 1:
                loc = 7
        elif gen == 4:
            if numbers_taken.count(9) != 1:
                loc = 9
    else:
        x = random.randint(1, 9)
        while numbers_taken.count(x) == 1:
            x += 1
            if x == 10:
                x = 0
        if numbers_taken.count(x) != 1:
            loc = x
        if loc == 10:
            x = 1
            while numbers_taken.count(x) == 0:
                x += 1
                if x == 10:
                    loc = 0
    return loc


# Gamemode - IMPOSSIBLE
def turn_1(loc):
    '''
    This is for the IMPOSSIBLE game mode. 
    It is a specialized function, only used once in gameplay.
    It will give the best choice the computer can make for its first turn.

    '''
    if playerX.count(5) != 1:
        loc = 5
    else:
        gen = random.randint(1, 4)
        if gen == 1:
            loc = 1
        elif gen == 2:
            loc = 3
        elif gen == 3:
            loc = 7
        elif gen == 4:
            loc = 9
    return loc


def turn_2(loc):
    '''
    This is for the IMPOSSIBLE game mode. 
    It is a specialized function, only used once in gameplay.
    It will give the best choice the computer can go at for its second turn.
    '''
    if computerO.count(5):
        # Player chooses corner first move
        if playerX.count(1) and playerX.count(2):
            loc = 3
        elif playerX.count(1) and playerX.count(4):
            loc = 7
        elif playerX.count(1) and playerX.count(9):
            gen = random.randint(1, 4)
            if gen == 1:
                loc = 2
            elif gen == 2:
                loc = 4
            elif gen == 3:
                loc = 6
            elif gen == 4:
                loc = 8
        elif playerX.count(1) and playerX.count(8):
            loc = 7
        elif playerX.count(1) and playerX.count(6):
            loc = 3
        elif playerX.count(3) and playerX.count(2):
            loc = 1
        elif playerX.count(3) and playerX.count(6):
            loc = 9
        elif playerX.count(3) and playerX.count(7):
            gen = random.randint(1, 4)
            if gen == 1:
                loc = 2
            elif gen == 2:
                loc = 4
            elif gen == 3:
                loc = 6
            elif gen == 4:
                loc = 8
        elif playerX.count(3) and playerX.count(8):
            loc = 9
        elif playerX.count(3) and playerX.count(4):
            loc = 1
        elif playerX.count(7) and playerX.count(4):
            loc = 1
        elif playerX.count(7) and playerX.count(8):
            loc = 9
        elif playerX.count(7) and playerX.count(2):
            loc = 1
        elif playerX.count(7) and playerX.count(6):
            loc = 9
        elif playerX.count(9) and playerX.count(6):
            loc = 2
        elif playerX.count(9) and playerX.count(8):
            loc = 7
        elif playerX.count(9) and playerX.count(2):
            loc = 3
        elif playerX.count(9) and playerX.count(4):
            loc = 7
        # Player chooses middle-edge for first move
        elif playerX.count(2) and playerX.count(1):
            loc = 3
        elif playerX.count(2) and playerX.count(3):
            loc = 1
        elif playerX.count(2) and playerX.count(6):
            loc = 3
        elif playerX.count(4) and playerX.count(1):
            loc = 7
        elif playerX.count(4) and playerX.count(7):
            loc = 1
        elif playerX.count(4) and playerX.count(2):
            loc = 1
        elif playerX.count(6) and playerX.count(3):
            loc = 9
        elif playerX.count(6) and playerX.count(9):
            loc = 3
        elif playerX.count(6) and playerX.count(8):
            loc = 9
        elif playerX.count(8) and playerX.count(7):
            loc = 9
        elif playerX.count(8) and playerX.count(9):
            loc = 7
        elif playerX.count(8) and playerX.count(4):
            loc = 7
    else:
        # Player has 5 and computer has 1,3,7, or 9
        if playerX.count(1) and numbers_taken.count(9) != 1:
            loc = 9
        elif playerX.count(1) and numbers_taken.count(9):
            gen = random.randint(1, 2)
            if gen == 1:
                loc = 3
            elif gen == 2:
                loc = 7
        elif playerX.count(2):
            loc = 8
        elif playerX.count(3) and numbers_taken.count(7) != 1:
            loc = 7
        elif playerX.count(3) and numbers_taken.count(7):
            gen = random.randint(1, 2)
            if gen == 1:
                loc = 1
            elif gen == 2:
                loc = 9
        elif playerX.count(4):
            loc = 6
        elif playerX.count(6):
            loc = 4
        elif playerX.count(7) and numbers_taken.count(3) != 1:
            loc = 3
        elif playerX.count(7) and numbers_taken.count(3) == 1:
            gen = random.randint(1, 2)
            if gen == 1:
                loc = 1
            elif gen == 2:
                loc = 9
        elif playerX.count(8):
            loc = 2
        elif playerX.count(9) and numbers_taken.count(1) != 1:
            loc = 1
        elif playerX.count(9) and numbers_taken.count(1) == 1:
            gen = random.randint(1, 2)
            if gen == 1:
                loc = 3
            elif gen == 2:
                loc = 7
    return loc


def turn_3(loc):
    """
    This is for the IMPOSSIBLE game mode.
    It is a specialized function, only used once in gameplay.
    It will give the best choice the computer can make for its third turn.
    """
    if playerX.count(2) and playerX.count(4) and numbers_taken.count(1) != 1:
        loc = 1
    elif playerX.count(2) and playerX.count(6) and numbers_taken.count(3) != 1:
        loc = 3
    elif playerX.count(4) and playerX.count(8) and numbers_taken.count(7) != 1:
        loc = 7
    elif playerX.count(6) and playerX.count(8) and numbers_taken.count(9) != 1:
        loc = 9

    elif playerX.count(2) and playerX.count(4) and numbers_taken.count(1) == 1:
        gen = random.randint(1, 2)
        if gen == 1:
            loc = 3
        elif gen == 2:
            loc = 7
    elif playerX.count(2) and playerX.count(6) and numbers_taken.count(3) == 1:
        gen = random.randint(1, 2)
        if gen == 1:
            loc = 1
        elif gen == 2:
            loc = 9
    elif playerX.count(4) and playerX.count(8) and numbers_taken.count(7) == 1:
        gen = random.randint(1, 2)
        if gen == 1:
            loc = 1
        elif gen == 2:
            loc = 9
    elif playerX.count(6) and playerX.count(8) and numbers_taken.count(9) == 1:
        gen = random.randint(1, 2)
        if gen == 1:
            loc = 3
        elif gen == 2:
            loc = 7
    else:
        loc = -1
    return loc


def turn_4(loc):
    """
    This is for the IMPOSSIBLE game mode.
    After 3 turns, there will be no winner. (If there is no block move or winning move available)
    """
    loc = makeMove()
    return loc


# Global Functions
def blockMove(loc):
    """
    Find what values the player has and the available values remaining.
    If the player has 2 in a row (horizontally, vertically, or diagonally) the computer will BLOCK it
    It will return -1 if no computer-blocking move available
    """
    p = check_Values("Computer", "X")
    n = check_Values("All", "All")
    # TOP HORIZONTAL
    if p[0] and p[1] and n[2] != 1:
        loc = 3
    elif p[0] and p[2] and n[1] != 1:
        loc = 2
    elif p[1] and p[2] and n[0] != 1:
        loc = 1
    # MID HORIZONTAL
    elif p[3] and p[4] and n[5] != 1:
        loc = 6
    elif p[3] and p[5] and n[4] != 1:
        loc = 5
    elif p[4] and p[5] and n[3] != 1:
        loc = 4
    # BOTTOM HORIZONTAL
    elif p[6] and p[7] and n[8] != 1:
        loc = 9
    elif p[6] and p[8] and n[7] != 1:
        loc = 8
    elif p[7] and p[8] and n[6] != 1:
        loc = 7

    # LEFT VERTICAL
    elif p[0] and p[3] and n[6] != 1:
        loc = 7
    elif p[0] and p[6] and n[3] != 1:
        loc = 4
    elif p[3] and p[6] and n[0] != 1:
        loc = 1
    # MID VERTICAL
    elif p[1] and p[4] and n[7] != 1:
        loc = 8
    elif p[1] and p[7] and n[4] != 1:
        loc = 5
    elif p[4] and p[7] and n[1] != 1:
        loc = 2
    # RIGHT VERTICAL
    elif p[2] and p[5] and n[8] != 1:
        loc = 9
    elif p[2] and p[8] and n[5] != 1:
        loc = 6
    elif p[5] and p[8] and n[2] != 1:
        loc = 3

    # DIAGONAL (L-R)
    elif p[0] and p[4] and n[8] != 1:
        loc = 9
    elif p[0] and p[8] and n[4] != 1:
        loc = 5
    elif p[4] and p[8] and n[0] != 1:
        loc = 1
    # DIAGONAL (R-L)
    elif p[2] and p[4] and n[6] != 1:
        loc = 7
    elif p[2] and p[6] and n[4] != 1:
        loc = 5
    elif p[4] and p[6] and n[2] != 1:
        loc = 3
    else:
        loc = -1
    return loc


def winningMove(loc):
    '''
    This function checks to see if there is any winning move available for the computer to take. 
    It will scan to see all the computer points, and then all the available points.
    If the computer has a chance of winning, and the spot is opened, the computer will place its point there. 
    If the computer has a chance of winning, but the spot is taken, the computer will not be able to go there. 
    It will return -1 if no computer winning move otherwise move
    '''
    c = check_Values("Computer", "O")
    n = check_Values("All", 'All')
    # TOP HORIZONTAL
    if c[0] and c[1] and n[2] != 1:
        loc = 3
    elif c[0] and c[2] and n[1] != 1:
        loc = 2
    elif c[1] and c[2] and n[0] != 1:
        loc = 1
    # MID HORIZONTAL
    elif c[3] and c[4] and n[5] != 1:
        loc = 6
    elif c[3] and c[5] and n[4] != 1:
        loc = 5
    elif c[4] and c[5] and n[3] != 1:
        loc = 4
    # BOTTOM HORIZONTAL
    elif c[6] and c[7] and n[8] != 1:
        loc = 9
    elif c[6] and c[8] and n[7] != 1:
        loc = 8
    elif c[7] and c[8] and n[6] != 1:
        loc = 7

    # LEFT VERTICAL
    elif c[0] and c[3] and n[6] != 1:
        loc = 7
    elif c[0] and c[6] and n[3] != 1:
        loc = 4
    elif c[3] and c[6] and n[0] != 1:
        loc = 1
    # MID VERTICAL
    elif c[1] and c[4] and n[7] != 1:
        loc = 8
    elif c[1] and c[7] and n[4] != 1:
        loc = 5
    elif c[4] and c[7] and n[1] != 1:
        loc = 2
    # RIGHT VERTICAL
    elif c[2] and c[5] and n[8] != 1:
        loc = 9
    elif c[2] and c[8] and n[5] != 1:
        loc = 6
    elif c[5] and c[8] and n[2] != 1:
        loc = 3

    # DIAGONAL (L-R)
    elif c[0] and c[4] and n[8] != 1:
        loc = 9
    elif c[0] and c[8] and n[2] != 1:
        loc = 5
    elif c[4] and c[8] and n[0] != 1:
        loc = 1
    # DIAGONAL (R-L)
    elif c[2] and c[4] and n[6] != 1:
        loc = 7
    elif c[2] and c[6] and n[4] != 1:
        loc = 5
    elif c[4] and c[6] and n[2] != 1:
        loc = 3
    else:
        loc = -1

    return loc


def trickMove(loc):
    """
    Used to add a bit more brain power to the computer turn.
    """
    if numbers_taken.count(5) != 1:
        loc = 5
    else:
        loc = -1
    return loc


# noinspection PyTypeChecker
def setupBoard():
    """
    Sets up the board. it sets each segment to match its number
    the board is set up in a 3x3 manner.
    00 01 02
    10 11 12
    20 21 22
    each point is assigned a number."""
    board[0][0] = ' 1 '
    board[0][1] = ' 2 '
    board[0][2] = ' 3 '
    board[1][0] = ' 4 '
    board[1][1] = ' 5 '
    board[1][2] = ' 6 '
    board[2][0] = ' 7 '
    board[2][1] = ' 8 '
    board[2][2] = ' 9 '


def displayBoard():
    """
    r = is everything that is not a separating line. example: [' 1 ', ' 2 ', ' 3 '] this includes the spaces and numbers.
        when r is below 2, it will print a horizontal divider.
        when r == 2, it will not print a horizontal divider.
    c = takes the item out of the r. example: [' 1 ']
        when c is below 2, it will print a vertical divider.
        when c == 2, it will not print a vertical divider.
    """
    for r in range(3):
        print(" ", end="")
        for c in range(3):
            colored_board = board[r][c]
            if colored_board == ' x ':
                colored_board = color.GREEN + color.BOLD + ' x ' + color.END
            elif colored_board == ' o ':
                colored_board = color.RED + color.BOLD + ' o ' + color.END
            print(colored_board, end="")
            if c < 2:
                print("|", end="")
        print()
        if r < 2:
            print(" ---|---|---")


def check_Values(gamemode, player_choice):
    """
    This function is used to check all the values of each list used throughout the game.
    """
    if gamemode == 'Human' and player_choice == 'X':
        x1 = playerX.count(1)
        x2 = playerX.count(2)
        x3 = playerX.count(3)
        x4 = playerX.count(4)
        x5 = playerX.count(5)
        x6 = playerX.count(6)
        x7 = playerX.count(7)
        x8 = playerX.count(8)
        x9 = playerX.count(9)
        human_X = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
        return human_X
    elif gamemode == 'Human' and player_choice == 'O':
        # Player O
        o1 = playerO.count(1)
        o2 = playerO.count(2)
        o3 = playerO.count(3)
        o4 = playerO.count(4)
        o5 = playerO.count(5)
        o6 = playerO.count(6)
        o7 = playerO.count(7)
        o8 = playerO.count(8)
        o9 = playerO.count(9)
        human_O = [o1, o2, o3, o4, o5, o6, o7, o8, o9]
        return human_O
    elif gamemode == 'Computer' and player_choice == 'X':
        # Player (Human vs. Computer)
        p1 = playerX.count(1)
        p2 = playerX.count(2)
        p3 = playerX.count(3)
        p4 = playerX.count(4)
        p5 = playerX.count(5)
        p6 = playerX.count(6)
        p7 = playerX.count(7)
        p8 = playerX.count(8)
        p9 = playerX.count(9)
        computer_X = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
        return computer_X
    elif gamemode == 'Computer' and player_choice == 'O':
        # Computer O
        c1 = computerO.count(1)
        c2 = computerO.count(2)
        c3 = computerO.count(3)
        c4 = computerO.count(4)
        c5 = computerO.count(5)
        c6 = computerO.count(6)
        c7 = computerO.count(7)
        c8 = computerO.count(8)
        c9 = computerO.count(9)
        computer_O = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
        return computer_O
    elif gamemode == 'All' and player_choice == 'All':
        # Numbers taken
        n1 = numbers_taken.count(1)
        n2 = numbers_taken.count(2)
        n3 = numbers_taken.count(3)
        n4 = numbers_taken.count(4)
        n5 = numbers_taken.count(5)
        n6 = numbers_taken.count(6)
        n7 = numbers_taken.count(7)
        n8 = numbers_taken.count(8)
        n9 = numbers_taken.count(9)
        all = [n1, n2, n3, n4, n5, n6, n7, n8, n9]
        return all


def location_insert(loc, playerXO):
    """
    Used to insert the shape into the location.
    """
    if loc == 1:
        board[0][0] = playerXO  # the move is played
    elif loc == 2:
        board[0][1] = playerXO
    elif loc == 3:
        board[0][2] = playerXO
    elif loc == 4:
        board[1][0] = playerXO
    elif loc == 5:
        board[1][1] = playerXO
    elif loc == 6:
        board[1][2] = playerXO
    elif loc == 7:
        board[2][0] = playerXO
    elif loc == 8:
        board[2][1] = playerXO
    elif loc == 9:
        board[2][2] = playerXO


# noinspection PyTypeChecker
def Winner_int(X_Values, O_Values, winner):
    """
    Used to find a winner and highlight the winning values.
    Cf - Color format
    """
    # Player X Win options
    if (X_Values[0] and X_Values[1] and X_Values[2]) or (
            X_Values[0] and X_Values[3] and X_Values[6]) or (
            X_Values[0] and X_Values[4] and X_Values[8]) or (
            X_Values[1] and X_Values[4] and X_Values[7]) or (
            X_Values[2] and X_Values[4] and X_Values[6]) or (
            X_Values[2] and X_Values[5] and X_Values[8]) or (
            X_Values[3] and X_Values[4] and X_Values[5]) or (
            X_Values[6] and X_Values[7] and X_Values[8]):
        Cf = color.GREEN + color.BOLD + ' X ' + color.END
        if X_Values[0] and X_Values[1] and X_Values[2]:
            board[0][0] = Cf
            board[0][1] = Cf
            board[0][2] = Cf
        elif X_Values[0] and X_Values[3] and X_Values[6]:
            board[0][0] = Cf
            board[1][0] = Cf
            board[2][0] = Cf
        elif X_Values[0] and X_Values[4] and X_Values[8]:
            board[0][0] = Cf
            board[1][1] = Cf
            board[2][2] = Cf
        elif X_Values[1] and X_Values[4] and X_Values[7]:
            board[0][1] = Cf
            board[1][1] = Cf
            board[2][1] = Cf
        elif X_Values[2] and X_Values[4] and X_Values[6]:
            board[0][2] = Cf
            board[1][1] = Cf
            board[2][0] = Cf
        elif X_Values[2] and X_Values[5] and X_Values[8]:
            board[0][2] = Cf
            board[1][2] = Cf
            board[2][2] = Cf
        elif X_Values[3] and X_Values[4] and X_Values[5]:
            board[1][0] = Cf
            board[1][1] = Cf
            board[1][2] = Cf
        elif X_Values[6] and X_Values[7] and X_Values[8]:
            board[2][0] = Cf
            board[2][1] = Cf
            board[2][2] = Cf
        winner = 1
    # Player O Win options
    elif (O_Values[0] and O_Values[1] and O_Values[2]) or (
            O_Values[0] and O_Values[3] and O_Values[6]) or (
            O_Values[0] and O_Values[4] and O_Values[8]) or (
            O_Values[1] and O_Values[4] and O_Values[7]) or (
            O_Values[2] == 1 and O_Values[4] and O_Values[6]) or (
            O_Values[2] and O_Values[5] and O_Values[8]) or (
            O_Values[3] and O_Values[4] and O_Values[5]) or (
            O_Values[6] and O_Values[7] and O_Values[8]):
        Cf = color.RED + color.BOLD + ' O ' + color.END
        if O_Values[0] and O_Values[1] and O_Values[2]:
            board[0][0] = Cf
            board[0][1] = Cf
            board[0][2] = Cf
        elif O_Values[0] and O_Values[3] and O_Values[6]:
            board[0][0] = Cf
            board[1][0] = Cf
            board[2][0] = Cf
        elif O_Values[0] and O_Values[4] and O_Values[8]:
            board[0][0] = Cf
            board[1][1] = Cf
            board[2][2] = Cf
        elif O_Values[1] and O_Values[4] and O_Values[7]:
            board[0][1] = Cf
            board[1][1] = Cf
            board[2][1] = Cf
        elif O_Values[2] and O_Values[4] and O_Values[6]:
            board[0][2] = Cf
            board[1][1] = Cf
            board[2][0] = Cf
        elif O_Values[2] and O_Values[5] and O_Values[8]:
            board[0][2] = Cf
            board[1][2] = Cf
            board[2][2] = Cf
        elif O_Values[3] and O_Values[4] and O_Values[5]:
            board[1][0] = Cf
            board[1][1] = Cf
            board[1][2] = Cf
        elif O_Values[6] and O_Values[7] and O_Values[8]:
            board[2][0] = Cf
            board[2][1] = Cf
            board[2][2] = Cf
        winner = 2
    return winner


# Other
def Player_turn(shape):
    """
    Used for each time the player is asked for input when a game is in progress.
    """
    time.sleep(0.5)
    while True:
        loc = getInteger(
            color.ORANGE + f"\nPlayer {shape}: " + color.END + "Please enter 1-9 to make your move (0 to quit): ")
        print()
        if loc == 0:
            break
        y = numbers_taken.count(loc)
        if y and (0 < loc < 10):
            print(color.RED + color.BOLD + f"{loc} is already taken. Please try again." + color.END)
        elif y == 0 and (0 < loc < 10):
            break
        else:
            print(
                color.RED + color.BOLD + f"\n{loc} is out of range.\nPlease try again." + color.END)
        print()
    return loc


# Gamemodes - Computer
def turn_novice(playerXO):
    """
    This is the Novice difficulty for the computer.
    The loop is used when the player or computer makes a turn.
    This loop is only entered when there is no winner.
    """
    # CODE FOR HUMAN PLAYER HERE
    if player == ' x ':
        print(color.U_LINE + color.DARKCYAN + "\nPlayer Turn" + color.END)
        loc = Player_turn(shape='X')
        numbers_taken.append(loc)
        playerX.append(loc)
    # COMPUTER TURN
    else:
        time.sleep(0.5)
        print(color.DARKCYAN + color.U_LINE + "\n\nComputer Turn" + color.END)
        loc = makeMove()
        numbers_taken.append(loc)
        computerO.append(loc)
        print(color.ORANGE + "\nPlayer O: " + color.END, end='')
        print(f"Entered the number: {loc}\n")
    location_insert(loc, playerXO)
    numbers_taken.sort()
    return loc


def turn_easy(playerXO):
    """
    This is an easy difficulty for the computer.
    The loop is used when the player or computer makes a turn.
    This loop is only entered when there is no winner.
    """
    # CODE FOR HUMAN PLAYER HERE
    if player == ' x ':
        print(color.U_LINE + color.DARKCYAN + "\nPlayer Turn" + color.END)
        loc = Player_turn(shape='X')
        numbers_taken.append(loc)
        playerX.append(loc)
    # COMPUTER TURN
    else:
        time.sleep(0.5)
        print(color.DARKCYAN + color.U_LINE + "\n\nComputer Turn" + color.END)
        loc = 1
        w = winningMove(loc)
        b = blockMove(loc)
        m = makeMove()
        if w != -1:
            loc = w
        elif b != -1:
            loc = b
        else:
            loc = m
        numbers_taken.append(loc)
        computerO.append(loc)
        if loc != 0:
            print(color.ORANGE + "\nPlayer O: " + color.END, end='')
            print(f"Entered the number: {loc}\n")
        else:
            print("\nThere is no spaces left to choose from.\n")
    location_insert(loc, playerXO)
    numbers_taken.sort()
    return loc


def turn_medium(playerXO):
    """
    This is the medium difficulty for the computer.
    The loop is used when the player or computer makes a turn.
    This loop is only entered when there is no winner.
    """
    # CODE FOR HUMAN PLAYER HERE
    if player == ' x ':
        print(color.U_LINE + color.DARKCYAN + "\nPlayer Turn" + color.END)
        loc = Player_turn(shape='X')
        numbers_taken.append(loc)
        playerX.append(loc)

    # CODE FOR COMPUTER LOOP

    else:
        time.sleep(0.5)
        print(color.DARKCYAN + color.U_LINE + "\n\nComputer Turn" + color.END)
        loc = 1
        w = winningMove(loc)
        b = blockMove(loc)
        t = trickMove(loc)
        m = makeMove()
        if w != -1:
            loc = w
        elif b != -1:
            loc = b
        elif t != -1:
            loc = t
        else:
            loc = m
        numbers_taken.append(loc)
        computerO.append(loc)
        if loc != 0:
            print(color.ORANGE + "\nPlayer O: " + color.END, end='')
            print(f"Entered the number: {loc}\n")
        else:
            print("\nThere is no spaces left to choose from.\n")

    location_insert(loc, playerXO)
    numbers_taken.sort()
    return loc  # if 0 was entered we need to know


def turn_hard(playerXO):
    """
    This is the Hard difficulty for the computer.
    The loop is used when the player or computer makes a turn.
    This loop is only entered when there is no winner.
    """
    # CODE FOR HUMAN PLAYER HERE
    if player == ' x ':
        print(color.U_LINE + color.DARKCYAN + "\nPlayer Turn" + color.END)
        loc = Player_turn(shape='X')
        numbers_taken.append(loc)
        playerX.append(loc)
    else:
        time.sleep(0.5)
        print(color.DARKCYAN + color.U_LINE + "\n\nComputer Turn" + color.END)
        loc = 1
        w = winningMove(loc)
        b = blockMove(loc)
        t = trickMove(loc)
        m = makeMove_Hard(loc)
        if w != -1:
            loc = w
        elif b != -1:
            loc = b
        elif t != -1:
            loc = t
        else:
            loc = m
        numbers_taken.append(loc)
        computerO.append(loc)
        if loc != 0:
            print(color.ORANGE + "\nPlayer O: " + color.END, end='')
            print(f"Entered the number: {loc}\n")
        else:
            print("\nThere is no spaces left to choose from.\n")
    location_insert(loc, playerXO)
    numbers_taken.sort()
    return loc


def turn_impossible(playerXO, turn):
    """
    This is the Impossible difficulty for the computer.
    The loop is used when the player or computer makes a turn.
    This loop is only entered when there is no winner.
    It is impossible to beat.
    It has specialized functions for each turn to ensure victory
    """
    # CODE FOR HUMAN PLAYER HERE
    if player == ' x ':
        print(color.U_LINE + color.DARKCYAN + "\nPlayer Turn" + color.END)
        loc = Player_turn(shape='X')
        numbers_taken.append(loc)
        playerX.append(loc)
    else:
        time.sleep(0.5)
        print(color.DARKCYAN + color.U_LINE + "\n\nComputer Turn" + color.END)
        w = winningMove(loc=1)
        b = blockMove(loc=1)
        if w != -1:
            loc = w
        elif b != -1:
            loc = b
        else:
            if turn == 1:
                loc = turn_1(loc=1)
            elif turn == 2:
                loc = turn_2(loc=1)
            elif turn == 3:
                turn3 = turn_3(loc=1)
                if turn3 != -1:
                    loc = turn3
            elif turn == 4:
                loc = turn_4(loc=1)
            else:
                loc = makeMove()

        numbers_taken.append(loc)
        computerO.append(loc)
        print(color.ORANGE + "\nPlayer O: " + color.END, end='')
        print(f"Entered the number: {loc}\n")
    location_insert(loc, playerXO)
    numbers_taken.sort()
    return loc


# Player vs. Player Function
def human_turn(playerXO):
    """
    The loop is used when player X or player O makes a turn. This loop is only entered when there is no winner.
    """
    # CODE FOR PLAYER X HERE
    if player == ' x ':
        loc = Player_turn(shape='X')
        numbers_taken.append(loc)
        playerX.append(loc)

    # CODE FOR PLAYER O HERE
    elif player == ' o ':
        loc = Player_turn(shape='O')
        numbers_taken.append(loc)
        playerO.append(loc)

    location_insert(loc, playerXO)
    numbers_taken.sort()
    return loc  # if 0 was entered we need to know


#
# --------------- The Game -------------------
#

print("""
  _____ _   _____       _____
 |_   _(_)_|_   _|_ _ _|_   _|__  ___
   | | | / _|| |/ _` / _|| |/ _ \/ -_)
   |_| |_\__||_|\__,_\__||_|\___/\___|
   """)
running = True
while running:
    play_again = 'force_yes'  # Used so that when the game starts, it does not ask the player again if they want to enter the menu they picked
    print(color.YELLOW + color.BOLD + color.U_LINE + "\n\nMain Menu" + color.END)
    game_mode = getInteger('''
    (1) - Player vs. Player
    (2) - Human vs. Computer
    (3) - Help
    (4) - Exit

    Please select one of the menus: ''')
    userX = 0  # Wins that the player X has
    userO = 0  # Wins that the player O has
    draw = 0  # When there is no winner
    # Human vs. Human
    if game_mode == 1:
        while True:
            if play_again.lower() == 'y' or play_again.lower() == 'yes' or play_again.lower() == '1' or play_again.lower() == 'force_yes':
                print(color.BLUE + color.BOLD + "\n\nPlayer vs. Player\n" + color.END)
                print(color.BOLD + color.GREEN + "GameBoard:\n" + color.END)
                setupBoard()
                playerX = []  # Players list of numbers taken.
                playerO = []  # Computers list of numbers taken.
                numbers_taken = []  # All the numbers taken.
                player = ' x '  # set to ' o ' for player O and ' x ' for player X.
                displayBoard()
                winner = 0

                while human_turn(player) != 0 and numbers_taken != [1, 2, 3, 4, 5, 6, 7, 8,
                                                                    9]:  # When the player does not quit and when there are still available positions on the board

                    displayBoard()
                    if player == ' x ':  # switch player between moves
                        player = ' o '
                    else:
                        player = ' x '
                    x = check_Values("Human", "X")
                    o = check_Values("Human", "O")
                    winner = Winner_int(x, o, winner)
                    if winner == 1 or winner == 2:
                        # If there is a winner, it will break out of the loop
                        break
                if numbers_taken == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    x = check_Values("Human", "X")
                    o = check_Values("Human", "O")
                    winner = Winner_int(x, o, winner)
                playerX.sort()
                playerO.sort()
                print(color.BOLD + color.YELLOW + color.U_LINE + "\nGAME OVER\n" + color.END)
                print("The Final Gameboard: \n")
                displayBoard()
                #
                # Winning values and display
                #
                # print(f"Winner: {winner}")
                print()
                if winner == 1:
                    print("Player X won!")
                    userX += 1
                elif winner == 2:
                    print("Player O won!")
                    userO += 1
                else:
                    print("Neither player won.")
                    draw += 1
                print(color.DARKCYAN + color.U_LINE + "\nStats:" + color.END)
                print(
                    f"\tPlayer X wins: {userX}\n\tPlayer O wins: {userO}\n\tDraws: {draw}")  # Displays statistics
                play_again = input(
                    "\nWould you like to play against your human opponent again? (y/n): ")  # Asks the user if they want to play again
            elif play_again.lower() == "n" or play_again.lower() == "no" or play_again.lower() == "2" or play_again.lower() == '0':
                print("Thank you for playing!")
                break
            else:
                print(
                    color.RED + color.BOLD + f"'{play_again}' is an invalid entry.\nPlease try again." + color.END)
                play_again = input(
                    "\nWould you like to play against your human opponent again? (y/n): ")
    # Human vs. Computer:
    elif game_mode == 2:
        while True:
            if play_again.lower() == 'y' or play_again.lower() == 'yes' or play_again.lower() == '1' or play_again.lower() == 'force_yes':
                setupBoard()
                playerX = []  # Players list of numbers taken.
                computerO = []  # Computers list of numbers taken.
                numbers_taken = []  # All the numbers taken.
                player = ' x '  # set to ' o ' for player O and ' x ' for player X.
                winner = 0
                difficulty = "Gamemode Difficulty"
                while difficulty != 0 and difficulty != -1:
                    print(color.BLUE + color.BOLD + "\n\nPlayer vs. Computer" + color.END)
                    # Asks the player which level of difficulty they want to play at
                    difficulty = getInteger('''
(1) - Novice
(2) - Easy
(3) - Medium
(4) - Hard
(5) - Impossible
(6) - Exit
(7) - Gamemode help

Please select a number with your choice difficulty level: ''')
                    if difficulty == 1:
                        print(color.BOLD + color.GREEN + "\nNovice GameBoard:\n" + color.END)
                        displayBoard()
                        while turn_novice(player) != 0 and numbers_taken != [1, 2, 3, 4, 5, 6, 7, 8,
                                                                             9]:
                            displayBoard()
                            if player == ' x ':  # switch player between moves
                                player = ' o '
                            else:
                                player = ' x '
                            p = check_Values('Computer', 'X')
                            c = check_Values('Computer', 'O')
                            winner = Winner_int(p, c, winner)
                            if winner == 1 or winner == 2:
                                break
                        if numbers_taken == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            p = check_Values('Computer', 'X')
                            c = check_Values('Computer', 'O')
                            winner = Winner_int(p, c, winner)
                        break
                    elif difficulty == 2:
                        print(color.BOLD + color.GREEN + "\nEasy GameBoard:\n" + color.END)
                        displayBoard()
                        while turn_easy(player) != 0 and numbers_taken != [1, 2, 3, 4, 5, 6, 7, 8,
                                                                           9]:
                            displayBoard()
                            if player == ' x ':  # switch player between moves
                                player = ' o '
                            else:
                                player = ' x '
                            p = check_Values('Computer', 'X')
                            c = check_Values('Computer', 'O')
                            winner = Winner_int(p, c, winner)
                            if winner == 1 or winner == 2:
                                break
                        if numbers_taken == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            p = check_Values('Computer', 'X')
                            c = check_Values('Computer', 'O')
                            winner = Winner_int(p, c, winner)
                        break
                    elif difficulty == 3:
                        print(color.BOLD + color.GREEN + "\nMedium GameBoard:\n" + color.END)
                        displayBoard()
                        while turn_medium(player) != 0 and numbers_taken != [1, 2, 3, 4, 5, 6, 7, 8,
                                                                             9]:
                            displayBoard()
                            if player == ' x ':  # switch player between moves
                                player = ' o '
                            else:
                                player = ' x '
                            p = check_Values('Computer', 'X')
                            c = check_Values('Computer', 'O')
                            winner = Winner_int(p, c, winner)
                            if winner == 1 or winner == 2:
                                break
                        if numbers_taken == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            p = check_Values('Computer', 'X')
                            c = check_Values('Computer', 'O')
                            winner = Winner_int(p, c, winner)
                        break
                    elif difficulty == 4:
                        print(color.BOLD + color.GREEN + "\nHard GameBoard:\n" + color.END)
                        displayBoard()
                        while turn_hard(player) != 0 and numbers_taken != [1, 2, 3, 4, 5, 6, 7, 8,
                                                                           9]:
                            displayBoard()
                            if player == ' x ':  # switch player between moves
                                player = ' o '
                            else:
                                player = ' x '
                            p = check_Values('Computer', 'X')
                            c = check_Values('Computer', 'O')
                            winner = Winner_int(p, c, winner)
                            if winner == 1 or winner == 2:
                                break
                        if numbers_taken == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            p = check_Values('Computer', 'X')
                            c = check_Values('Computer', 'O')
                            winner = Winner_int(p, c, winner)
                        break
                    elif difficulty == 5:
                        print(color.BOLD + color.GREEN + "\nImpossible GameBoard:\n" + color.END)
                        displayBoard()
                        turn = 0
                        while turn_impossible(player, turn) != 0 and numbers_taken != [1, 2, 3, 4,
                                                                                       5, 6, 7, 8,
                                                                                       9]:
                            displayBoard()
                            if player == ' x ':  # switch player between moves
                                player = ' o '
                                turn += 1
                            else:
                                player = ' x '
                            p = check_Values('Computer', 'X')
                            c = check_Values('Computer', 'O')
                            winner = Winner_int(p, c, winner)
                            if winner == 1 or winner == 2:
                                break
                        if numbers_taken == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            p = check_Values('Computer', 'X')
                            c = check_Values('Computer', 'O')
                            winner = Winner_int(p, c, winner)
                        break
                    elif difficulty == 6 or difficulty == 0:
                        difficulty = 0  # breaks out of the loop, and sends the user to the Main Menu
                    elif difficulty == 7:
                        # Displays the different options and their description for each game difficulty level
                        print(color.BOLD + color.GREEN + "\n\tGame Mode selection:" + color.END)
                        print('''
        The user is given an option to choose their game mode when they play against the computer.
        Below is a brief description of each game mode.

        Novice:
            In Novice mode, the computer has no strategy or skill at all.
            A great way to learn how to play!
        Easy:
            In easy mode, the computer will try to block you or take a win if it is available.
            Other than that, the computer will not have a strategy for point selection.

        Medium:
            In medium mode, the computer will do all that is in easy mode.
            Plus it will also try to block you off of your first move. It has a bit more strategy.

        Hard:
            In hard mode, the computer will do all in medium mode.
            Plus it will also think ahead. It will think about what you can do if you choose the following move.

        Impossible:
            As the name suggests, it is impossible to beat.

''')
                        enter = input(
                            "Press enter to continue.")  # So that the user is not automatically forced to the next section
                        difficulty = -1
                    else:
                        print(
                            color.RED + color.BOLD + f"\n'{difficulty}' is out of range.\nPlease try again." + color.END)
                # End GAME LOOP
                if difficulty != 0:  # If the player did not exit the game
                    playerX.sort()
                    computerO.sort()
                    print(color.BOLD + color.YELLOW + color.U_LINE + "\nGAME OVER\n" + color.END)
                    print("The Final Gameboard: \n")
                    displayBoard()
                    #
                    # Winning values and display
                    #
                    print()
                    if winner == 1:
                        print("Player won!")
                        userX += 1
                    elif winner == 2:
                        print("Computer won!")
                        userO += 1
                    else:
                        print("Neither player won.")
                        draw += 1
                    print(color.DARKCYAN + color.U_LINE + "\nStats:" + color.END)
                    print(f"\tPlayer X wins: {userX}\n\tPlayer O wins: {userO}\n\tDraws: {draw}")
                    play_again = input(
                        "\n\nWould you like to play against the computer again? (y/n): ")
                elif difficulty == -1:  # Allows the user to choose their game mode difficulty now
                    play_again = 'y'
                else:
                    break
            elif play_again.lower() == "n" or play_again.lower() == "no" or play_again.lower() == "2" or play_again.lower() == '0':
                print("Thank you for playing!")
                break
            else:
                print(
                    color.RED + f"'{play_again}' is an invalid entry.\nPlease try again." + color.END)
                play_again = input("\n\nWould you like to play against the computer again? (y/n): ")
    # Help Menu
    elif game_mode == 3:
        print(color.BLUE + color.BOLD + "\nHelp Menu\n" + color.END)
        print(color.BOLD + color.GREEN + "\tRules of the game:" + color.END)
        print('''
    \t*  The game is played on a grid that's 3 squares by 3 squares.
    \t*  You are X, and your friend (or the computer) is O.
    \t*  Players take turns putting their marks in empty squares.
    \t*  The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
    \t*  When all 9 squares are full, the game is over.

''')
        print(color.BOLD + color.GREEN + "\tHow to play:" + color.END)
        print('''

    \t*  Pick a number between 1-9.
    \t\t*  Only numbers that are available will be accepted.
    \t*  Beat your opponent by getting 3 in a row.

''')
        enter = input(
            "Press enter to continue.")  # Gives the player time to read through the above
        # information before sending them back to the main menu0
    # Exit Menu
    elif game_mode == 4 or game_mode == 0:
        # When the user no longer wants to play
        print("\nGoodbye!")
        running = False
        break
    # Error Statement
    else:
        print(
            color.RED + color.BOLD + f"\n'{game_mode}' is out of range.\nPlease try again." + color.END)
