board = [
    [0,0,0],  
    [0,0,0],  
    [0,0,0]    
]
grid = [
    [0,0,0],  
    [0,0,0],  
    [0,0,0]   
]

currentplayer = "O"
print(board)
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("|", end = "")
            print(board[i],[j], end = "|")
        print()
printBoard(board)

def placepiece(board,currentplayer,row,col):
    if board[row][col] == 0:
        board[row][col] = currentplayer
        return True
    else:
        print("That is not a valid square")
        return False
def switchplayer(currentplayer):
    if currentplayer == "O":
        return "X"
    elif currentplayer == "X":
        return "O"
def checkwinner(board,currentplayer):
    for i in range(len(board)):
        if board[i][0] == currentplayer and board [i][1] == currentplayer and board[i][2] == currentplayer:
            print(f"{currentplayer} wins!")
            return True
        
        
    for j in range(len(board[0])):
        if board[0][j] == currentplayer and board[1][j] == currentplayer and board[2][j] == currentplayer:
            print(f"{currentplayer}wins!")
            return True
    
    if board[0][0] == board[1][1] == board [2][2] == currentplayer:
        print(f"{currentplayer} wins!")
        return True

    if board[0][2] == board[1][1] == board [2][0] == currentplayer:
        print(f"{currentplayer} wins!")
        return True
    for row in board:
        for space in row:
            if space == 0:
                return False
    return True

def main():
    grid = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
curr = "X"
while checkwinner(grid,curr) == False:
    curr = switchplayer(curr)
    check = False
    while check == False:
        row = int(input(f"Enter the Row: ").strip())
        col = int(input(f"Enter the Col: ").strip())
        if placepiece(grid,curr,row,col) == True:
            check = True

if __name__ == "__main__":
    main()
    
