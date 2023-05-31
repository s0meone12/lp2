# Python function to solve the
# N Queen Problem

# Function to print the solution.
def printSolution(board, N):
    # It is similar to printing the 2-d array.
    for i in range(N):
        for j in range(N):
            print(board[i][j], end =" ")
        
        print()

# Function to check if it is safe to place 
# queen in the cell (row, col) such that 
# it does not attack any other queen.
def isSafe (board, row, col, N):
    # Defining and initializing i and j with row 
    # and col respectively.
    i, j = row, col

    # Checking if the left (main) diagonal has 
    # any queen.
    while (i > -1 and j > -1):
        # If a queen is found, return 'false'
        # that means it is not safe to place a queen.
        if (board[i][j] == 'Q'):
            return False

        # Updating values of i and j
        i -= 1
        j -= 1
    

    i, j = row, col
    # Checking if the right (secondary) diagonal has 
    # any queen.
    while (i > -1 and j < N):
        # If a queen is found, return 'false'
        # that means it is not safe to place a queen.
        if (board[i][j] == 'Q'):
            return False

        # Updating values of i and j
        i -= 1
        j += 1
    
    i, j = row, col
    # Checking if the columns (col) has 
    # any queen.
    while (i > -1):
        # If a queen is found, return 'false'
        # that means it is not safe to place a queen.
        if (board[i][j] == 'Q'):
            return False

        # Updating values of i and j
        i -= 1
    
    # If we have reached here, it means it is safe
    # to place the queen in the cell (row, col)
    # Hence, returning true
    return True


# Function to check whether solution exists
# for N queen problem, for the provided N.
# board -> Chess Board of dimensions N*N
# N -> Size of the chess board
# row -> Row number in which we will try to place 
#      the queen. It's value ranges from [0, N-1].
def solutionExists(board, N, row):
    # If we have placed a queen in all
    # the rows, it means solution exists.
    if (row >= N):
        return True
    
    # Trying to place the queen in every possible
    # cell in the 'row th' row.
    for col in range(N):
        # Using a function to check if it is
        # possible to place a queen in the cell
        # (row, col) such that it does not attack
        # any other queen.
        if (isSafe(board, row, col, N)):
            # If found true, place a queen in the 
            # cell (row, col) and recur for the
            # next row.
            board[row][col] = 'Q'
            
            if (solutionExists(board, N, row + 1)):
                return True

            # This statement will execute only if placing queen in cell (row, col) do not 
            # form any solution. Hence, we will consider
            # to leave this cell empty.
            board[row][col] = '.'
        
    # Returning false if we do not find any valid
    # Solution.
    return False



# Function to Solve the NQueen Problem
def solveNQueenProblem(N):
    # Defining the board, that will be used to print
    # the result if a solution exists
    board = []
    # Initializing all its cells to be empty
    # at first.
    for i in range(N):
        temp = []
        # '.' Represents empty cell
        for j in range(N):
            temp.append('.')

        board.append(temp)
    
    # If the solution do not exists
    if (solutionExists(board, N, 0) == False):
        print("No solution exists for N =", N)
     
    # Otherwise, if the solution exists.
    else:
        print("One of the possible solution for N =", N, "is -")
        printSolution(board, N)

# Driver Code 
# Defining the dimension of square board.
N = 4
# Calling function to solve the
# N queen problem for the given N.
solveNQueenProblem(N)
