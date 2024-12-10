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
            dim = self.grid.shape[0]  # size of the grid
            # determine bounds for slicing
            start_row = max(0, row - 1)
            end_row = min(dim, row + 2) # +2, becouse it would be an incomplet subgrid when slicing
            start_col = max(0, col - 1)
            end_col = min(dim, col + 2) # +2, becouse it would be an incomplet subgrid when slicing

            # slicing
            subgrid = self.grid[start_row:end_row, start_col:end_col]

            # check if any value is -1
            return np.any(subgrid == -1)
        

        valid = True
        # checking the validity of that cell
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
            
            dim = self.grid.shape[0]
            while len(checked_positions) < dim * dim:  # avoiding infinite loops
                row, col = random.randint(0, dim - 1), random.randint(0, dim - 1) # generate random pos
                if (row, col) in checked_positions: # checking not visited
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
        dim = self.grid.shape[0]  # size of the grid
        for row in range(dim):
            for col in range(dim):
                if self.grid[row, col] == -1:
                    continue  
                
                # determine bounds for slicing
                start_row = max(0, row - 1)
                end_row = min(dim, row + 2) # +2, becouse it would be an incomplet subgrid when slicing 
                start_col = max(0, col - 1)
                end_col = min(dim, col + 2) # +2, becouse it would be an incomplet subgrid when slicing

                # slicing
                subgrid = self.grid[start_row:end_row, start_col:end_col]

                # count the number of dragon eggs in the subgrid
                dragon_count = np.sum(subgrid == -1)

                # assign the count to the current cell
                self.grid[row, col] = dragon_count          

class Athena(Island): 
    def __init__(self, r, d):
        super().__init__(r, d)
        self.grid = np.full(((2 * r) - 1, (2 * r) - 1), -9) # init grid full of -9
        self.trials = 2 * d

    def playAthena(self, hades):
        found_dragons = 0
        trials = 0
        
        print("\nAthena's grid:")
        print(self)

        while found_dragons < self.numdragons and trials < self.trials: # eggs missing and trials left
            
            try:
                row = int(input("Enter the row: "))
                col = int(input("Enter the column: "))

                # check for invalid input
                if not (0 <= row < hades.grid.shape[0] and 0 <= col < hades.grid.shape[1]):
                    print("Invalid indices. Please enter values within the grid range.")
                    continue
                
                # sea cell
                if hades.grid[row, col] == -9:
                    print("Sea. Try again.")
                    trials += 1
                    continue

                # update Athena's grid and trials
                self.grid[row, col] = hades.grid[row, col]
                trials += 1
                
                # Check if a dragon egg was found
                if self.grid[row, col] == -1:
                    found_dragons += 1
                    print("You found a dragon egg")
                
                print("\nAthena's grid:")
                print(self)

            except ValueError:
                print("Invalid input. Please enter integer values for row and column.")
                continue

        if found_dragons == self.numdragons:
            return True
        else:
            return False

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
    not_valid = True
    r = 0
    d = 0
    while not_valid:
        try:
            r = int(input("Enter the length of the side of the rhombus: "))
            d = int(input("Enter the number of dragon eggs: "))
            if r > 0 and d > 0: # negative values not allowed
                not_valid = False
            else:
                print("Negative values not allowed.")
        except ValueError:
            print("Invalid input. Please enter integer values for row and column.")
        
    IslandHades = Hades(r, d)
    if IslandHades.plantDragonEggs(): # planting eggs
        IslandAthena = Athena(r, d)
        msg = ''
        if IslandAthena.playAthena(IslandHades): # playing
            msg = "Athena saved Rhodes"
            print(msg)
        else:
            msg = "Dragons have destroyed Rhodes!"
            print(msg)

        try: # writting game
            with open(f"solution_{r}_{d}.txt", "w") as f:
                f.write(f"Hades:\n{IslandHades}\n\nAthena:\n{IslandAthena}\nRes:{msg}")
        except Exception:
            print("Error, something went wrong")
    else:
        print("Eggs could not be planted, because invalid size of the rhombus.")
        