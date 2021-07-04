
''' 
    > Takes in the text file's lines as input
    > interpreting the coordinates and grid information encodings
    > creates an array which holds each cell value given in the text file as an object
    > returns first the array of the grid with object elements
    > then for the algorithms to work on- returns array of grid as a string representation

'''

import re       # to split the numeric values from the special characters in the text file lines
import sys
from Search import path

class Grid:

    dimensions=[]

    def storeGrid(self, fileLines):
        # using the command of words=re.split('[|,|]', fileLines[0]) to get the separated characters from the file lines
        grid_dimensions = re.findall(r"[\w']+", fileLines[0])
        intial_pos = re.findall(r"[\w']+", fileLines[1])
        goal_pos = re.findall(r"[\w']+", fileLines[2])
        walls=[]
        goal=[]
        init=[]
        #dimensions=[]

        # demarcating the wall cell coordinates (lines: 3 - last file line)
        for k in range(3, len(fileLines)):
            wall_pos = re.findall(r"[\w']+", fileLines[k])
            for num in wall_pos:
                if(num!='(' and num!=')' and num!=','):
                    walls.append(int(num))

        wall_len=len(walls)
        i=0
        while(i<wall_len-3):
            for a in range(walls[i+2]): #width
                for b in range(walls[i+3]): #height
                    walls.append([walls[i]+a,walls[i+1]+b])
            i+=4
        
                
        
        # using command res = [int(sub.split('.')[1]) for sub in test_list] to separate the numerics from the file line
        for num in grid_dimensions: #1st line= grid dimensions [rows, columns]
                if(num!='[' and num!=']' and num!=','):
                     self.dimensions.append(int(num))
        for num in intial_pos:      #2nd the initial state coordinate location (x,y)
                if(num!='[' and num!=']' and num!=','):
                     init.append(int(num))
        for num in goal_pos:        #3rd the goal state coordinate location (x,y)
                if(num!='[' and num!=']' and num!=',' and num!='|'):
                     goal.append(int(num))
        goal_len=len(goal)      #storing the multiple goal position(s)
        m=0
        while(m<goal_len-1):
            goal.append([goal[m],goal[m+1]])
            m+=2
            
        gridInput=[]
        i=1

        #feeding into the array the each cell and its type through the object of class GridCell
        for y in range(self.dimensions[0]):
            for x in range(self.dimensions[1]):
                if([x, y] == init):
                    color="red"
                elif([x, y] in goal):
                    color="green"
                elif([x, y] in walls):
                    color="grey"
                else:
                    color="white"
                temp= GridCell(x, y, i, color)
                gridInput.append(temp)
                i+=1
     
        #gridInput[0].show()
        
        return gridInput
    

    
    # translates the obj consisting array to a string array to work on in the program
    def generate_grid(self, maze):
        str_grid=[]
        global path
        #for str in range(grid.nums[1]):
        str_grid.append(("#"*(self.dimensions[1]+2))+"\n")
        cell="#"

        # converting the cell objects to a character in the string array using nested loops:
        for row in range(self.dimensions[0]):
            for col in range(self.dimensions[1]):
                for obj in maze:
                    if(obj.cellx==col and obj.celly==row):
                        if obj.color=='grey':       # for the walls
                            cell+="#"
                        elif obj.color=="green":    # to indicate goal position(S)
                            cell+="G"
                        elif obj.color=="red":      # to indicate start position
                            cell+="S"
                            path.append((obj.cellx+1, obj.celly+1))     #linking the start position to the final solution's path
                        else:
                            cell+=" "
            cell+="#\n"
            str_grid.append(cell)
            cell="#"
                        
                #j+=1
        str_grid.append("#"+"#"*self.dimensions[1]+"#")
        #print(gstr)
        return str_grid
    
    


class GridCell:
    def __init__(self, x, y, nodeNumber, color):
         self.cellx=x
         self.celly=y
         self.color=color
         self.nodeNumber=nodeNumber
         self.visited=False
         #self.neighbours = EnlistNeighbours()
         
    def show(self):
        print(self.cellx, self.celly, self.color, self.nodeNumber)
    
    def __getItem__(self):
        return self.color
