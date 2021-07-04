import math     # to calculate the heuristic function
from collections import deque       # for creating data structures and special lists such as stack and queue for the tree nodes management
from queue import Queue, LifoQueue, PriorityQueue
from MazeSearch import MazeSearch
from AlgoEnum import Algo
import turtle

from MazeGui import *
from Search import *
from Search import path, maze_gui
import sys
#from memory_profiler import profile

#@profile(precision=4)


#path=[]


class SearchMethods(MazeSearch):

    def __init__(self, grid):
        MazeSearch.__init__(self, grid)
        #super().__init__(self, grid)

# Solves a maze based on a given algorithm and returns (grid, path cost, number of nodes expanded)
    def solve(self, algo):
        # redirecting the to the algorithm execution according to the type of method requested
            #  informed search A*, A*_version_2 and GBFS
        if algo is Algo.A_STAR or algo is Algo.GREEDY or algo is Algo.A_Star_2:
            return self.solveAG(algo)

            # custom program 1
        if algo is Algo.IDDFS:
            return self.iddfs()

            # Custom program 2
        if algo is Algo.IDA_STAR:
            return self.idastar()

   
        #uninformed search - dfs and bfs        
        # Intialize the data structure depending on the Algorithm
        goals = self.getGoalPositions()
        if len(goals)==0:
            return self.grid, 0, "\nNo solution found."
        
        frontier = Queue(maxsize=0) if(algo is Algo.BFS) else LifoQueue(maxsize=0) #queue for bfs and stack for dfs
        frontier.put((self.start, 0, goals))   # Frontier: ((x, y), path cost) : tuple(tuple(x, y), int)
        frontierSet = {self.start} # Creating a set of all the nodes that are in the frontier for finding purposes
        self.explored = set()           # Set of all the nodes that have been already explored
        self.parents[self.start] = -1
        total=len(goals)
        while not frontier.empty():
            t = frontier.get()      # Remove from frontier
            global path

            node, cost, dots = t    #attributes of the first node in the queue/stack

            if (algo is Algo.BFS):
                frontierSet.remove(node)

            self.explored.add(node)    # Add to Explored set
            
            if node in goals:
                goals = set(goals)   # Create a dots set
                goals.remove(node)
               
                
               # If a dot position is found, remove it from the dots set
                if len(goals) == total-1: # Goal test - if any one goal position is found   
                #if len(goals)==0:                
                    self.markSolutionDB(node)
                    return self.grid, cost, len(self.explored)


            y, x=node
            if(self.start!=node and len(sys.argv)==4):
                maze_gui.color("blue")
                maze_gui.goto(x*2.5,y*3.8)
                maze_gui.stamp()
         
          
            successors = self.getSuccessors(node)
            if algo is Algo.DFS:
                successors=successors[::-1]
            for n in successors:           # Put all the valid neighbors in the frontier
                
                if (n in self.explored or n in frontierSet) and (algo is Algo.BFS):  #skip if visited or already there in frontier
                    continue
                
                if (n in self.explored) and (algo is Algo.DFS):
                    continue

                self.parents[n] = node
                frontier.put((n, cost+1, goals)) # Put in the incremented cost
                frontierSet.add(n)


        return self.grid, cost, "\nNo solution found."      
        #raise Exception('Frontier became empty without a solution')
        
    
        # Gets the Manhattan Distance between two coordinates
    def mDistance(self, node1, node2):
        assert(isinstance(node1, tuple) and isinstance(node2, tuple))
        y1, x1 = node1
        y2, x2 = node2
        return abs(x2 - x1) + abs(y2 - y1)


    # Returns the average of distances for all the dots from the current node
    # this will be our heuristic function
    def heuristicDistance(self, node, goals):
        totalDist = 0
        
        for d in goals:
            totalDist += self.mDistance(node, d)
        return totalDist / len(goals)
    
    # a second heuristic used for studying the difference- A_Star_2 prompt
    def euclidHeuristic(self, node, goals):
        y1, x1 = node
        for g in goals:
            y2, x2 = g
        return ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

    # to solve the maze using A* and Greedy. 
    def solveAG(self, algo):

        ignoreMap = dict()         # the discard/expanded nodes
        frontier = PriorityQueue() # Intialize the a priority queue
        goals = self.getGoalPositions()
               
        if len(goals)==0:
            return self.grid, 0, "\nNo solution found."
        
        score = self.heuristicDistance(self.start, list(goals)) # heuristic[start][goal]
        if(algo is Algo.A_Star_2):
            score = self.euclidHeuristic(self.start, list(goals))
        parents = [self.start]

        frontier.put((score, self.start, 0, goals, parents))   # Frontier: ((x, y), path cost) : tuple(tuple(x, y), int, {dots})
        self.frontierMap[(self.start, tuple(goals))] = 0 # Map of nodes to path cost
              

        while not frontier.empty():
            state = frontier.get()       # Remove from frontier
            _, node, cost, goals, parents = state  # (score, (y, x), cost, dots)
            #print("in the loop"+str(treshold))
            if node in ignoreMap and ignoreMap[node] == cost: # If node has inefficient path cost, skip it
                continue

            if (node, tuple(goals)) in self.frontierMap:
                del self.frontierMap[(node, tuple(goals))]
            self.explored.add((node, tuple(goals)))


            # self.explored.add((node, tuple(dots)))    # Add to Explored set: ((y, x), R)
            #total=len(goals)
            if node in goals:
                goals = set(goals)   # Create a dots set
                goals.remove(node)  # If a dot position is found, remove it from the dots set
                #if len(goals) == total-1:  # Goal test - if all the dot positions have been found
                self.markSolution(node, parents)
                return self.grid, cost, len(self.explored)
                
          
            successors = self.getSuccessors(node)
            for n in successors:           # Put all the valid neighbors in the frontier
                # Check if already explored
                if (n, tuple(goals)) in self.explored:
                    continue

                if algo is Algo.A_STAR: # if A*, score is f = g(cost) + h(mDist)
                    #Manhattan distance for Greedy, MDist + Cost(0) for A* heurisitc function + cost function
                    score = cost+1 + self.heuristicDistance(n, goals)
                elif algo is Algo.A_Star_2:
                    score = cost+1 + self.euclidHeuristic(n, goals)
                else: # if Greedy, score is Manhattan distance
                    score = self.heuristicDistance(n, goals)
                    

                y, x = node
                if(self.start!=node and len(sys.argv)==4):
                    maze_gui.color("blue")
                    maze_gui.goto(x*2.5,y*3.8)
                    maze_gui.stamp()
                # Check if already in frontier and if yes, check it has a better path cost
                if (n, tuple(goals)) in self.frontierMap:
                    if self.frontierMap[(n, tuple(goals))] > cost+1 : #Exisitng path cost is worse, then replace
                        ignoreMap[n] = self.frontierMap[(n, tuple(goals))]
                    else:
                        continue

                p = list(parents)
                p.append(n)
                
                frontier.put((score, n, cost+1, goals, p)) # Put in the incremented cost
                self.frontierMap[(n, tuple(goals))] = cost+1
                
                
        return self.grid, cost, "\nNo solution found."
        #raise Exception('Frontier became empty without a solution')


    # to solve Iterative Deepening Depth-First Search- Custom Search 1- uninformed search strategy            
    def iddfs(self):
        depth=1
        global path
        bottom_reached= False
        goals = self.getGoalPositions()
        self.parents[self.start] = -1
        while not bottom_reached:
            self.parents[self.start]=-1
            result, bottom_reached = self.recursive(self.start, goals, 0, depth)
           
            if result is not None:          #found the goal node while doing DFS with this max depth
                goals = set(goals)   # Create a goals set
                goals.remove(result)

                self.markSolutionDB(result)
                return self.grid, len(path)-1, len(self.parents) #len(self.explored) or count
            
            depth*=len(self.grid[0])+len(self.grid)
            #print("increasing depth to: "+str(depth))
            
        return self.grid, cost, "\nNo solution found."
    
    def recursive(self, node, target, current_depth, max_depth):
        #print("visiting node: ", node)
        self.explored.add(node)

        y, x= node
        if(self.start!=node and len(sys.argv)==4):
            maze_gui.color("purple")
            maze_gui.goto(x*2.5,y*3.8)
            maze_gui.stamp()
            maze_gui.color("blue")
            maze_gui.goto(x*2.5,y*3.8)
            maze_gui.stamp()
        
        
        if node in target:
            #print("goal state found")
            target = set(target)   # Create a dots set
            target.remove(node)
            return node, True
        
        if current_depth == max_depth:
            #print("max depth reached")
            
            if len(self.getSuccessors(node))>0:
                self.explored.clear()   #has more child nodes under it/ not bottom
                return None, False 
            else:
                return None, True
           
            
        i=list()
        bottom_reached = True
        for n in self.getSuccessors(node):

            if not n in self.explored:          #to check for repeated and expanded states
                for k in self.parents.keys():
                    i.append(k)
                if not n in i:
                    self.parents[n]=node

                result, bottom_reached_rec = self.recursive(n, target, current_depth+1, max_depth)
            
                if result is not None:
                    return result, True
                bottom_reached = bottom_reached and bottom_reached_rec
            
        return None, bottom_reached
                
                
        # to solve the Iterative Deepening A* search - Custom Search 2- informed search strategy
    def idastar(self):

        goals=self.getGoalPositions()
        threshold = self.heuristicDistance(self.start, list(goals)) # heuristic[start][goal]
        parents=[]
        parents.append(self.start)
        cost=0
        while True:
            
            flag=self.recursive2(parents, 0, threshold, goals, cost)
            if flag=="FOUND":
                self.markSolution(parents[-1], parents)
                return self.grid, len(parents)-1, self.parents[0]

            if flag == float("inf"):
                return self.grid, cost, "not found"
            
            threshold= flag
            
            
            
            
    def recursive2(self, parents, g, threshold, target, cost):
        node=parents.pop() #get the last element in the list
        self.parents[0]=0   # holder-as a across-class accessor to, in this case, store the number of nodes expanded
        #flag=None
        self.explored.add(node)
        parents.append(node)
        global path

        f=g+self.heuristicDistance(node, list(target))
        cost+=1
        y, x=node
        if(self.start!=node and len(sys.argv)==4):
            #maze_gui.color("purple")
            #maze_gui.goto(x*24,y*-24)
            #maze_gui.stamp()
            #turtle.tracer(0,0)
            maze_gui.color("blue")
            maze_gui.goto(x*2.5,y*3.8)
            maze_gui.stamp()
            #maze_gui.speed(fastest)
            turtle.tracer(0,0)      # to make the process faster in the gui

        if f>threshold:
            return f

        
        min=float("inf")
        
        for n in self.getSuccessors(node):
            if n not in parents and n not in self.explored:
                parents.append(n)
                if n in target:
                    target = set(target)   # Create a goals set
                    target.remove(n)
                  
                    return "FOUND"
                flag=self.recursive2(parents, g+cost+1, threshold, target, cost)
                if flag =="FOUND":      
                    self.parents[0]+=cost       #to hold the cumulative nodes expanded
                    self.parents[1]="yes"
                    return "FOUND"
                if(len(sys.argv)==4):
                    turtle.update()
                if flag<min:
                    self.explored.clear()
                    #cost=0
                    min=flag
                    
                parents.pop()
                
        return min
               
    # Prints the final solution path in the CLI maze
    def markSolution(self, curr, parents):
        #s = '123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        #chars = list(s)

        idx = 0
        global path
        
        for n in parents:
            y, x = n; row = self.grid[y] # Get coordinates an corresponding row
            if self.grid[y][x] == 'S':
                continue
            if (y, x) in self.goalPositions and self.grid[y][x] == 'G':
                #self.grid[y] = row[:x] + chars[idx] + row[x+1:] #  Mark the visted dot with the dot number%10
                #idx += 1
                self.grid[y] = row[:x] + 'G' + row[x+1:]
            else:
                self.grid[y] = row[:x] + 'x' + row[x+1:] # Mark the visted node with a '.'
            path.append((n[1], n[0]))
            # print(''.join(self.grid))

        # to print the path in the CLI for a BFS, DFS or IDDFS (they pass a dictionary of the linked path coordinates)
    def markSolutionDB(self, curr, parents=None):
        parents = self.parents if parents is None else parents
        goalCount = self.goalCount
        global path
        
        while (curr != -1):
            y, x = curr; row = self.grid[y] # Get coordinates an corresponding row
            if self.grid[y][x] == 'S':
                return
                #pass
            if (y, x) in self.goalPositions:
                self.grid[y] = row[:x] + 'G' + row[x+1:] #  Mark the visted dot with the dot number%10
                
            else:
                self.grid[y] = row[:x] + 'x' + row[x+1:] # Mark the visted node with a '.'
                

            path.append((x,y))
            
            curr = parents[curr]
           
            
