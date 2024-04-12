# from model_matrix import Matrix
# from model_point import Point 
# from const import * 
# from maze import SearchSpace
# from model_path import Path
# import pygame 

# class SearchAlgo : 
#     def __init__(self, matrix : Matrix) -> None:
#         self.matrix = matrix 


# class BFS (SearchAlgo) : 
#     def __init__(self, matrix : Matrix) -> None:
#         super().__init__(matrix)
#     def findPath (self) : 
#         myQueue = [self.matrix.startPoint]  
#         visited = [self.matrix.startPoint]
#         self.matrix.startPoint.isVisited = True
#         #initial path 
#         init_path = Path(self.matrix.startPoint)
#         myPath  = [init_path]   
#         chosen_path = None
#         level = 0
#         cur_pass = []
#         stop_level = 0
#         while len(myQueue) > 0  : 
#         # for i in range(40) :
#             if(stop_level != 0 and stop_level < level) :
#                 break
#             cur_point = myQueue.pop(0) 
#             cur_point.isVisited = True
#             cur_path = myPath.pop(0)
#             cur_path.display()

#             if (level < cur_path.level) :
#                 while(len(cur_pass) > 0) : 
#                     p = cur_pass.pop()
#                     if(p.isVisited == True) :
#                         continue
#                     p.isVisited = True
#                     visited.append(p)
#                 print('level up')
#                 level = cur_path.level            

#             if  cur_point.compare(self.matrix.endPoint) == True :
#                 # choose this path : 
#                 if(chosen_path == None or chosen_path.cost > cur_path.cost ) :
#                     chosen_path = cur_path
#                     stop_level = chosen_path.level
#                 while (len(myQueue) > 0) : 
#                     last_indx = len(myPath) -1
#                     last_path = myPath[last_indx]
#                     last_point = myQueue[last_indx]
#                     if(last_path.cost > chosen_path.cost or last_path.level > stop_level) :
#                         myPath.pop() 
#                         myQueue.pop()
#                     else:
#                         break
#             else :
#                 neighbors = cur_point.getNeighbour(self.matrix.graph)
#                 if (len(neighbors) > 0 ) :                
#                     for neibor in neighbors : 
#                         if (neibor.isVisited == True) : 
#                             continue
#                         new_path = Path(neibor , cur_path.foot_print, cur_path.cost)
#                         myQueue.append(neibor) 
#                         cur_pass.append(neibor)
#                         neibor.isVisited = True
#                         visited.append(neibor)
#                         myPath.append(new_path)
#                         if(self.matrix.endPoint.compare(neibor) == True) : 
#                             break
#             # print(f'Loop in BFS {i}, curent level :{level}, curPath level :  {cur_path.level}')
           
#         for point in visited :
#             #to be reset  
#             point.display()
#             point.color = WHITE
#             point.isVisited = False
#         chosen_path.highlight()

#     def findShortestPath (self, path) : 
#         pass

# class BFS_dev (SearchAlgo) : 
#     def __init__(self, matrix: Matrix) -> None:
#         super().__init__(matrix)
#     def findPath (self) : 
#         myQueue = [self.matrix.startPoint]  
#         myPath = [Path(self.matrix.startPoint)]
#         visited = [self.matrix.startPoint]
#         self.matrix.startPoint.isVisited = True
#         while (len (myQueue) > 0) : 
#             curPoint = myQueue.pop(0) ; 
#             curPath = myPath.pop(0) ; 

#             neibors = curPoint.getNeighbour()


# def test()  : 
#     myMatrix = Matrix()
#     myMatrix.parseFile('input_2.txt')
#     bfs = BFS(myMatrix) ; 
#     bfs.findPath() ; 

#     pygame.init()
#     pygame.display.set_caption('test')

#     #initialize map 
#     COLS, ROWS= myMatrix.width+1, myMatrix.height+1
#     RES = WIDTH , HEIGHT = 800+2*BOUND + (ROWS-1)*(A1), 800+2*BOUND + (COLS-1)*(A1)

#     sc = pygame.display.set_mode(RES)
#     print(RES)
#     clock = pygame.time.Clock()
#     sc.fill(pygame.color.Color(GREY))


#     g = SearchSpace(myMatrix)

#     g.draw(sc)
#     clock.tick(20)

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 exit()


# test() ; 
