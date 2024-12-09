import numpy as np

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
    
    island = Island(3, 5)
    print(island)
 