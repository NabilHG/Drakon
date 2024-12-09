import numpy as np
import random 

class Island():
    def __init__(self, r, d):
        def create_board(r):
            dim = 2 * r - 1  # dimension of the square matrix (2*r)-1
            grid = np.full((dim, dim), -9)  # init the grid with -9
            
            for i in range(dim):
                for j in range(dim):
                    if abs(i - (r - 1)) + abs(j - (r - 1)) < r: # Manhattan distance to check is inside the rhombus shape
                        grid[i, j] = 0
            
            return grid

        
        self.grid = create_board(r)
        self.numdragons = d

        print(self.grid)

    # get the value of a given coordinate                     
    def getCell(self, col, row):
        return self.grid[row,col]

    # set the value of a given coordinate
    def setCell(self, col, row, v):
        self.grid[row,col] = v

    # converting the grid to make it more appealing
    def __str__(self):
        content = ''
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[0]):
                if self.grid[i, j] == -9:
                    content += ' · '
                elif self.grid[i, j] == -1:
                    content += ' * '
                else:
                    content += ' 0 '
            content += '\n\n'

        return content


class Hades(Island):
    def __init__(self, r, d):
        super().__init__(r, d)
        
    def isValid(self,row,col):
        def adjacent(row,col):
            dim = self.grid.shape[0]  # Size of the grid
            # Determine bounds for slicing
            start_row = max(0, row - 1)
            end_row = min(dim, row + 2) 
            start_col = max(0, col - 1)
            end_col = min(dim, col + 2)

            # Slice the 3x3 region centered at (row, col)
            subgrid = self.grid[start_row:end_row, start_col:end_col]

            # Check if any value is -1 (dragon egg), excluding the center cell
            return np.any(subgrid == -1)
        

        valid = True

        if self.grid[row, col] == -9:
            valid = False
        elif adjacent(row, col):
            valid = False
        elif self.grid[row, col] == -1:
            valid = False

        return valid

    def plantDragonEggs(self):
        def backtrack(remaining_dragons, checked_positions):
            if remaining_dragons == 0: # all eggs placed
                return True

            # generate random pos that have not been checked yet
            dim = self.grid.shape[0]
            while len(checked_positions) < dim * dim:  # avoiding infinite loops
                row, col = random.randint(0, dim - 1), random.randint(0, dim - 1)
                if (row, col) in checked_positions:
                    continue
                checked_positions.add((row, col))  # mark position as checked

                if self.isValid(row, col):
                    self.grid[row, col] = -1 
                    if backtrack(remaining_dragons - 1, checked_positions):
                        return True
                    # backtracking, remove the dragon egg and try another position
                    self.grid[row, col] = 0

            return False  # no positions left 

        checked_positions = set()  # track positions already checked
        return backtrack(self.numdragons, checked_positions)
    
    def assignNumbersToGrid(self):
        dim = self.grid.shape[0]  # Size of the grid
        for row in range(dim):
            for col in range(dim):
                if self.grid[row, col] == -1:
                    continue  
                
                # Determine bounds for slicing
                start_row = max(0, row - 1)
                end_row = min(dim, row + 2) # +2, becouse it would be an incomplet subgrid when slicing 
                start_col = max(0, col - 1)
                end_col = min(dim, col + 2) # +2, becouse it would be an incomplet subgrid when slicing

                # Slice the 3x3 region centered at (row, col)
                subgrid = self.grid[start_row:end_row, start_col:end_col]

                # Count the number of dragon eggs (-1) in the subgrid
                dragon_count = np.sum(subgrid == -1)

                # Assign the count to the current cell
                self.grid[row, col] = dragon_count          





def letsPlayDrakon():
    print('''
Welcome to the game “Drakon”. You will try to save Rhodes Island
from the dragons. The program will receive as input:
    • R, defining the length of the side of the rhombus.
    • D, defining the number of dragon eggs.
The program will create the grid representing the island and find a
place for the D dragon eggs. Then, another board will be created for
Athena, since she will try to discover the location of the dragon
eggs by selecting cells. Athena has limited time to save the island
from the dragons, so she can only check a maximum of 2*D cells.
The program will generate a txt file containing the solution (the
two grids and the result of the game).
    ''')
    


if __name__ == "__main__":
    letsPlayDrakon()
    
    a = Hades(2,5)
    print(len(a.grid), "eaf")
 