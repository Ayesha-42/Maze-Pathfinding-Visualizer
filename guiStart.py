import sys
import turtle           # for the graphical user interface implemented for the path visualizer



# To activate the gui window to open and display its contents on the provided console prompt
if(len(sys.argv)==4):
    if(sys.argv[3]=="gui"):
    #Setting up the gui window
        wn = turtle.Screen()               # define the turtle screen
        wn.bgcolor("black")                # set the background colour
        wn.title("A Maze Solving Program")
        wn.setup(0.75,0.75)                 # setup the dimensions of the working window
        turtle.setworldcoordinates(0, 100, 100, 0)  # Makes the grid to be drawn from the left top corner to accomodate size
    else:
        pass
        #raise Exception("The final argument is an incorrect command. Enter 'gui' to enable and view the GUI path visualizer of the program")
else:
    #wn.exit()
    #sys.exit()
    pass





