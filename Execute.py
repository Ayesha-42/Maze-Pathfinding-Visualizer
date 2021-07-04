
import sys
from Search import path, maze_gui

def printPath(algo, grid):
	global path
	
	#if algo is Algo.BFS or algo is Algo.DFS:
	if(algo=='bfs' or algo=='dfs' or algo=='cus1'):
		first=path[0]
		path=path[::-1]
		path.insert(0, first)
		
		# to generate the path's moves which act as the required solution to this Robot Navigation Maze problem
	
	for idex, elem in enumerate(path):

		if(idex>0):        
			if elem[0]-path[idex-1][0]== 0 and elem[1]-path[idex-1][1] == 1 :
				print("\t down;",end='')
			elif elem[0]-path[idex-1][0]== 0 and elem[1]-path[idex-1][1] == -1 :
				print("\t up;",end='')
			elif elem[0]-path[idex-1][0]== 1 and elem[1]-path[idex-1][1] == 0:
				print("\t right;",end='')
			elif elem[0]-path[idex-1][0]== -1 and elem[1]-path[idex-1][1] == 0 :
				print("\t left;",end='')
			# to show the final route on the GUI from the goal to the start as the path picked on the grid	
		if(idex>0 and idex<(len(path)-1) and len(sys.argv)==4):
			maze_gui.color("yellow")
			maze_gui.goto(elem[0]*2.5,(elem[1]*3.8))
			maze_gui.stamp()
			
		# to compensate for the overlaps in some unlikely cases, of the start and finish position cells
	for i, y in enumerate(grid):
		for j, x in enumerate(y):
			if x=='G' and len(sys.argv)==4:
				maze_gui.color("green")
				maze_gui.goto(j*2.5, i*3.8)
				maze_gui.stamp()
	for i, y in enumerate(grid):
		for j, x in enumerate(y):
			if x=='S' and len(sys.argv)==4:
				maze_gui.color("red")
				maze_gui.goto(j*2.5, i*3.8)
				maze_gui.stamp()
	