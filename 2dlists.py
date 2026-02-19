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
print(board)
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("|", end = "")
            print(board[i],[j], end = "|")
            print()
printBoard(board)