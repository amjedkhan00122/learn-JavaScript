# N is the size of the 2D matrix N*N
N = 9

# A utility function to print grid in a formatted way
def printGrid(arr):
    for i in range(N):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(N):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(arr[i][j] if arr[i][j] != 0 else ".", end=" ")
        print()

# Checks whether it will be legal to assign num to the given row, col
def isValid(grid, row, col, num):
    boxStartRow = row - row % 3
    boxStartCol = col - col % 3

    for x in range(N):
        if grid[row][x] == num or grid[x][col] == num:
            return False
        if grid[boxStartRow + x // 3][boxStartCol + x % 3] == num:
            return False
    return True

# Backtracking function to solve Sudoku
def solveSudoku(grid, row=0, col=0):
    if row == N - 1 and col == N:  # If we have filled all cells
        return True

    if col == N:  # Move to the next row
        row += 1
        col = 0

    if grid[row][col] > 0:  # Skip pre-filled cells
        return solveSudoku(grid, row, col + 1)

    for num in range(1, N + 1):  # Try numbers 1 through 9
        if isValid(grid, row, col, num):
            grid[row][col] = num

            if solveSudoku(grid, row, col + 1):  # Recursive step
                return True

        grid[row][col] = 0  # Backtrack

    return False

# Driver Code
if __name__ == "__main__":
    # Example grid with 0 representing unfilled cells
    grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    if solveSudoku(grid):
        printGrid(grid)
    else:
        print("No solution exists")
