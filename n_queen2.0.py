class NQueens:
    def __init__(self, n):
        self.n = n
        self.solution = [-1] * n
        self.solutions = []
    
    def solve(self):
        self.backtrack(0)
        return self.solutions
    
    def backtrack(self, row):
        if row == self.n:
            self.solutions.append(self.solution.copy())
            return
        
        for col in range(self.n):
            if self.is_safe(row, col):
                self.solution[row] = col
                self.backtrack(row + 1)
                self.solution[row] = -1
    
    def is_safe(self, row, col):
        for i in range(row):
            if (
                self.solution[i] == col or
                self.solution[i] - col == i - row or
                self.solution[i] - col == row - i
            ):
                return False
        return True

n_queens = NQueens(8)
solutions = n_queens.solve()

for solution in solutions:
    print(solution)
