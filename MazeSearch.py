class MazeSearch:

    # Constructor
    def __init__(self, grid):
        # Initialize the basics needed for the search algorithms
        self.grid = grid       # Intialize the maze grid as the string array passed to it
        self.explored = set()  # Set of all the nodes that have been already explored
        self.goalPositions = self.getGoalPositions()          # Get a set of tuples of goal positions
        self.goalCount = len(self.goalPositions)              # Numbers of dots to find (used for goal test)
        self.start = self.getStartPosition()                # Start position as a tuple
        self.parents = {}        # the parent node being expanded as a reference to backtrack or trace the solution path
        self.frontierMap = {}    # Creating a map of all the nodes that are in the frontier for finding purposes

    # Given a maze, returns a hashset of tuples - (row, col) positions of all the dots
    def getGoalPositions(self):
        return {(j, i) for j, r in enumerate(self.grid) for i, c in enumerate(r) if c == 'G'}

    # Given a maze, returns the start point identified by 'P' as a tuple - (row, col)
    def getStartPosition(self):
        for j, r in enumerate(self.grid): # Get the idx, row(string) from grid
            for i, c in enumerate(r): # Get the idx, character from the string
                if c == 'S':
                    #print(j,i)
                    return (j, i)
        raise Exception("Could not find the start position")


    # Check whether a node has not been visited yet
    def isUnexplored(self, node):
        return node not in self.explored and node not in self.frontierSet

    # Gets a list of all the non-wall neighboring that current node can move to
    def getSuccessors(self, pos):
        assert (isinstance(pos, tuple)) # Making sure pos is a type
        child = []     # Initialize the list of children nodes under the parent node being expanded
        y, x = pos # x = pos[1]; y = pos[0];

        # with respect to the ordering when all is equal
        up = (y-1, x)
        right = (y, x+1)
        down = (y+1, x)
        left = (y, x-1)
       

        # Check if the surrounding nodes are not walls and are unexplored
        if self.grid[up[0]][up[1]] != '#': # Up
            child.append((y-1, x))
        if self.grid[left[0]][left[1]] != '#': # Left
            child.append((y, x-1))
        if self.grid[down[0]][down[1]] != '#': # Down
            child.append((y+1, x))
        if self.grid[right[0]][right[1]] != '#': # Right
            child.append((y, x+1))

        return child

    