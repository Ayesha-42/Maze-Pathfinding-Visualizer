#!/usr/bin/env python3
import sys

import time                     # to calculate the estimated time taken to run an algorithm

from collections import deque       # for creating data structures and special lists such as stack and queue for the tree nodes management
from queue import Queue, LifoQueue, PriorityQueue

import turtle           # for the graphical user interface implemented for the path visualizer

path=[]


# linking/importing the classes of the software
from guiStart import *
from MazeGui import *
from Grid import *
from AlgoEnum import Algo
from MazeSearch import MazeSearch
from SearchMethods import *
from Execute import *
maze_gui=Maze()


'''

        ***Assignment 1- Tree Search Program***
    > This is the main of the program
    > it takes the argument values from the console and processes it into their respective functionalities
    > parses the file text into a workable grid array
    > calls for the maze and search specifications to be set up
    > condition gui to set up
    > calls for the search method to run on the maze layout
    > returns path and appropriate output to the console
    > displays nodes expanded (blue) and the final path (yellow) in the gui window

'''


#import shutil
#from guppy import hpy



if __name__ == "__main__":

    # to check if the minimum arguments required to run the basic version of the program are present. otherwise prompts the correct format
    if len(sys.argv) < 3:
        raise Exception("Need two minimum arguments: search.bat maze.txt <algo method: AS, GBFS, BFS, DFS, AS2, CUS1 or CUS2> <gui or extra?>")
    
    
    #takes in the console argument inputs of file and method
    maze_fname = sys.argv[1]; a = sys.argv[2]; 
    algoMap = {'bfs': Algo.BFS, 'dfs': Algo.DFS, 'as': Algo.A_STAR, 'gbfs': Algo.GREEDY, 'cus1': Algo.IDDFS, 'cus2': Algo.IDA_STAR, 'as2': Algo.A_Star_2}
    
    a=a.lower()
    if a in algoMap:
        algo = algoMap[a]
    
    else:
        raise Exception("Algorithm not valid; Use AS, GREEDY, BFS, DFS, CUS1, CUS2 or AS2")
    
    
     #opening and reading file
    file = open(maze_fname, 'r')
    lines=file.readlines()
    file.close()
    
    #passing the file lines on to parse them relevant to the program
    new_grid = Grid()
    grid_objs=new_grid.storeGrid(lines)


    grid=[]
    grid=new_grid.generate_grid(grid_objs)
  

    start_timer = time.time()
    
    # the instance used to manipulate and draw elements on the gui window
    maze_gui=Maze()

    # the instance of the search setup class
    maze = SearchMethods(grid)
   
    if len(sys.argv)==4 and sys.argv[3]=='gui':
        setup_maze(grid)

    else:
        turtle.Screen().bye()

    #polymorphisized- running the search algorithm method
    new_grid, cost, nodes_expanded = maze.solve(algo)

    end_timer = time.time()

    new_maze = ''.join(new_grid)
    #total, used, free = shutil.disk_usage("/")
    #h = hpy()

    if(len(sys.argv)==5): #to accompany the gui visualization display with this console input, it also displays a CLI version of it with addition information
        
      print(new_maze)
      print ("The path cost is "+ str(cost) + " steps")
      print("The number of nodes expanded is "+str(nodes_expanded))
      print ("Elapsed time: " + str(end_timer - start_timer))
      #print("Used: %d GiB" % (used // (2**30)))
      #print h.heap()  

        

    print(maze_fname, a.upper(), nodes_expanded)
    printPath(a, grid)

    endProgram()
