grid = [
    [0,0,0,0],  
    [0,0,0,0],  
    [0,0,0,0],      
]
print(grid[0][0])

"The syntax is [row],[col]"

grid2 = [
    [1,2,3],  
    [4,5,6],  
    [7,8,9],      
]
print(grid2[2][2])

for row in grid2:
    for num in row:
        print(num)
        
for i in range(len(grid2)):
    for j in range(len(grid2[0])):
        print(grid2[i][j])
        print(f"({i},{j}) = {grid2[i][j]}", end  = " ")

board = [
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
    else:
        print("That is not a valid square")
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