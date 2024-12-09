class Island():
    def __init__(self, r, d):
        self.grid = create_board(r)
        self.numdragons = d


        def create_board(r): #square matrix, r + 2
            pass

    def getCell(self, col, row):
        return self.grid[row,col]

    def setCell(self, col, row, v):
        self.grid[row,col] = v

    def __str__(self):
        pass



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

