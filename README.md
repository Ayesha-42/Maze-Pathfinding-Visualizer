# Maze Pathfinding Visualizer

This assignment examines the problem of a robot located at an initial position in a maze with the objective to reach a goal position. The provisions of the maze’s dimensions, wall, agent and goal positions, are referenced in the illustration of the maze, which numerically encoded in the text file passed to it via a console line argument. All necessary locations’ coordinates will be specified in the text file along the prior mentioned grid layout and cell types.
The run-statement to be entered on the console line interface within the folder where the program files are located is of the format– search.bat <filename> <method>
For example- search.bat RobotNav-test.txt BFS
search.bat RobotNav-test.txt GBFS
To run the Graphical-User interface functionality of the program, an addition third argument value ‘gui’ needs to be passed to view that aspect of the program execution, as follows-
search.bat <filename> <method> gui
To envoke the extra information output into the CLI the command is:
search.bat <filename> <method> extra info
<method>= GBFS, AS, BFS, DFS, CUS1, CUS2, AS2
The output first prints out the file’s name which supplied the maze’s grid and position details the method of search requested by the user and that implemented, the number of nodes expanded before reaching the goal node, followed by the path given as a sequence of directional moves followed by the robot to reach from the start to goal configurations in the maze under the problem rules and assumptions. It also may give the message of ‘no solution found’ in case of the program being unable to find a proper solution path or that when no goal state is given in the maze.
 


The Robot Navigation Problem is a type of path finding situation through a maze with obstacles and one starting point to reach one end point from the only, many or none.
This assignment aims to research and implement the multiple search algorithms by processing a given maze grid into a tree or undirected graph of possible moves. Several search techniques are deployed to traverse this tree. The aim is to find a viable path on the basis of the individual characteristics of each type of search algorithm falling under two broad categories- informed and uninformed searches strategies.
Pathfinding algorithms address the problem of finding a path from a source to a destination avoiding obstacles and minimizing the costs (time, distance, risks, fuel, price, etc.). in a maze/labyrinth.



The software deploys four core search algorithms to solve the problem of finding a path through the maze’s designed grid. They are comprised of two uninformed search strategies namely Breadth-First Search and Depth First search. The other two from these are informed search strategies; A star and greedy-best first search.

‘gui’ as the third argument would indicate to the program to launch the turtle window to view the path visualization of the search method being implemented as the expansion of frontier nodes being checked and traversed in the tree. The turtle module opens the screen where the tile objects will be drawn. First the grid of the maze is drawn. A grey boundary wall around the maze is built to give it an enclosure. The expanded nodes in the sequence of their appearance is shown in blue. The initial and final positions are shown in red and green respectively. The valid cells on the grid for the robot to move in are in white and the walls or obstacles are the grey cells. The flickering purple tile is superimposed to show the recursive nature of the IDDFS and IDA* search methods. The final path returned as a result of the search algorithm deployed is shown in yellow at the end.

Although the customary practice is to use a recursive function for DFS, here the stack is looped over as to merge it in with the code formatting and complacency. This does not alter the algorithm sequential decisions and approach of the type of search strategy the DFS calls for in any way. Hence the choice is only of an alternate syntax design keeping algorithm integrity in mind.

A star_2 implemented with a different heuristic=> Euclidian diatance/ pythagorus distance aka the straight line difference.