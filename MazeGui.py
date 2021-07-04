
import turtle           # for the graphical user interface implemented for the path visualizer
import sys

from guiStart import wn


class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("grey")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)
     

maze_gui=Maze()

def setup_maze(grid):                          # define a function called setup_maze
    global maze_gui
    #global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
            screen_x = (x  *2.5)         # move to the x location on the screen staring at -588
            screen_y = (y * 3.8)          # move to the y location of the screen starting at 288
            
            if character == "#":
                maze_gui.color("grey")
                maze_gui.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                maze_gui.stamp()                          # stamp a copy of the turtle on the screen
                #walls.append((x, y))    # add coordinate to walls list

            if character == " ":
                maze_gui.color("white")
                maze_gui.goto(screen_x, screen_y)
                maze_gui.stamp()
                
             #   path.append((screen_x, screen_y))     # add " " and e to path list
             

            if character == "G":
                maze_gui.color("green")
                maze_gui.goto(screen_x, screen_y)       # send green sprite to screen location
                #end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                maze_gui.stamp()
               

            if character == "S":
                #start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                maze_gui.color("red")
                maze_gui.goto(screen_x, screen_y)
                maze_gui.stamp()



def endProgram():

    #turtle.bye()
    if(len(sys.argv)==4):
        wn.exitonclick()
    else:
        sys.exit()