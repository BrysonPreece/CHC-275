"""
Name: Bryson Preece
Section: 01
Description: Template for Lab 6
"""

"""
Scenario: We are to build a connect 4 game that runs in the terminal
"""

def drawBoard(board):
    for row in board:
        for space in row:
            print(f"|{space}|", end = '')
        print()
    """
    This function draws the board in  a nice, clean manner into the terminal.
        PARAMETERS:
        board: 2D List corresponding to connect 4 Board
        
        Return Type:
        NONE
    """
 

def switchPlayer(player):
    if player == "O":
        return "X"
    elif player == "X":
        return "O"

    """
    Switches player from X to O or O to X
    
        PARAMETERS: 
        Player (STR): Corresponds to the current player
        
        Return Type:
        Player (STR): Switched Player
    """

    
def dropPiece(board,player,column):
    for row in range(len(board)-1, -1, -1):
        try:
            if board[row][column] == 0:
                board[row][column] = player
                return True
        except Exception as e:
            print(f"An error has occurred: {e}")
    """ 
    Drops piece in specified column
    
        PARAMETERS:
        board (2D List): Game board
        player (STR): current player
        column (int): column to drop piece in
        
        Return Type:
        NONE
    """

    
    
def checkWinner(board,player):
    """
    Checks Board for winner
    
        PARAMETERS:
        board(2d list): Game board
        player(STR): Current player being checked for victory   
        
        Return Type:
        (BOOL): True if win False if not win 
    """
    #Check Horizontal Win
    for row in range(3, len(board)):
        for space in range(0, len(board[row])):
            if board[row][space] == player:
                if board [row][space+1] == player and board[row][space+2] == player and board[row][space+3] == player:
                    print(f"{player} wins!")
                    return True
    #Check Vertical Win
    for row in range(len(board)-3):
        for col in range(len(board[row])):
            if board[row][col] == player:
                if board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                    print(f"{player} wins!")
                    return True
    #Check Left Diagonal win
    for row in range(len(board)):
        for space in range(len(board[row])-3):
            if board[row][space] == player:
                if board [row-1][space+1] == player and board[row-2][space+2] == player and board[row-3][space+3] == player:
                    print(f"{player} wins!")
                    return True
    #Check Right Diagonal Win
    for row in range(len(board)-3):
        for space in range(len(board[row])):
            if board[row][space] == player:
                if board [row+1][space+1] == player and board[row+2][space+2] == player and board[row+3][space+3] == player:
                    print(f"{player} wins!")
                    return True
    return False

def main():
    ROWS = 6
    COLUMNS = 7
    BOARD = [ 
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],        
    ]

    CURRENT_PLAYER = "X"
    #what switch player does is checks to see if current player = x
    #if it is, return O
    #if its not, return X 
    while checkWinner(BOARD, CURRENT_PLAYER) == False:
        print()
        drawBoard(BOARD)
        CURRENT_PLAYER = switchPlayer(CURRENT_PLAYER)
        check1 = False
        while check1 == False:
            col = int(input("Enter the column you would like to drop your piece into (1-7): ").strip()) -1
            if dropPiece(BOARD, CURRENT_PLAYER, col) == True:
                check1 = True
                break
            
    
if __name__ == "__main__":
    main()