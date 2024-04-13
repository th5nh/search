import pygame
from const import *
from model_matrix import Matrix
from model_point import Point

class Node:
    def __init__(self, point:Point, a, id) -> None:
        self.rect = pygame.Rect(point.x *(A+A1) + BOUND, point.y *(A+A1)+BOUND, a, a)
        self.color = point.color
        self._set_color (self.color)
        self.id = id
        self.is_brick = point.isBlock
        self.x = point.x
        self.y = point.y

    def draw(self, sc:pygame.Surface) -> None:
        pygame.draw.rect(sc, self.color, self.rect)

    def _set_color(self, color):
        self.color = color

    def set_color(self, color, sc:pygame.Surface):
        self.color = color
        self.draw(sc)
        # change the speed here
        pygame.time.delay(7)
        pygame.display.update()

class SearchSpace:
    def __init__(self, myMatrix : Matrix) -> None:
        self.myMatrix = myMatrix
        self.COLS, self.ROWS= myMatrix.width+1, myMatrix.height+1
        self.grid_cells:list[Node] = []
        for i in range(0,self.ROWS):
            for j in range(0, self.COLS):
                # define the brick's appearing
                node = myMatrix.graph[i][j]
                index = self.convert2Dto1D(j,i)
                self.grid_cells.append(Node(node, A,index))
        
        start_id = self.convert2Dto1D(myMatrix.startPoint.x, myMatrix.startPoint.y) 
        end_id = self.convert2Dto1D(myMatrix.endPoint.x, myMatrix.endPoint.y) 
        self.start:Node = self.grid_cells[start_id]
        self.start.id = start_id
        self.start.is_brick = False
        self.start._set_color(ORANGE)
        self.goal:Node = self.grid_cells[end_id]
        self.goal.is_brick = False
        self.goal.id = end_id
        self.goal._set_color(PURPLE)

        if (myMatrix.haveStations == True):
            station_1_id = myMatrix.stationPoint_1.y*self.COLS+myMatrix.stationPoint_1.x
            station_2_id = myMatrix.stationPoint_2.y*self.COLS+myMatrix.stationPoint_2.x
            self.station_1:Node = self.grid_cells[station_1_id]
            self.station_1.id = station_1_id
            self.station_1.is_brick = False     
            self.station_1._set_color(BLUE)
            self.station_1.reached = False
            
            self.station_2:Node = self.grid_cells[station_2_id]
            self.station_2.id = station_2_id
            self.station_2.is_brick = False
            self.station_2._set_color(BLUE)
            self.station_2.reached = False

        self.font = pygame.font.SysFont('Aral', 16) 

    def convert2Dto1D (self,x , y): 
        return  (y )*self.COLS + x

    def draw(self, sc:pygame.Surface):
        for node in self.grid_cells:
            node.draw(sc)
        
        for i in range(self.COLS): 
            label = self.font.render(str(i) ,True, WHITE )
            sc.blit(label , (self.grid_cells[i].rect.center))

        for i in range (self.ROWS): 
            label = self.font.render(str(i) ,True, WHITE )
            sc.blit(label , (self.grid_cells[i*self.COLS].rect.center))  

        label = self.font.render("S" ,True, WHITE )
        sc.blit(label , (self.start.rect.center)) 

        label = self.font.render("G" ,True, WHITE )
        sc.blit(label , (self.goal.rect.center)) 

        if (self.myMatrix.haveStations == True):
            label = self.font.render("R" ,True, WHITE )
            sc.blit(label , (self.station_1.rect.center)) 
            sc.blit(label , (self.station_2.rect.center)) 

        pygame.display.flip()

    def get_length(self):
        return len(self.grid_cells)
    
    def is_start(self, node:Node):
        return node.id == self.start.id

    def is_goal(self, node:Node):
        return node.id == self.goal.id
    
    def is_station(self, node:Node):
        return node.id == self.station_1.id or node.id == self.station_2.id

    def get_neighbors(self, node: Node) -> list[Node]:
        x,y = node.x , node.y

        # define the directions of agent
        up = self.convert2Dto1D(x,y-1) if y-1 >= 0 else None
        down = self.convert2Dto1D(x,y+1) if y+1<self.ROWS else None
        left  =self.convert2Dto1D(x-1,y) if x-1 >= 0 else None
        right = self.convert2Dto1D(x+1,y)if x+1 < self.COLS else None

        left_up = self.convert2Dto1D(x-1,y-1) if y-1 >= 0 and x-1 >= 0 else None
        left_down = self.convert2Dto1D(x-1,y+1) if y+1 < self.ROWS and x-1 >= 0 else None
        right_up = self.convert2Dto1D(x+1,y-1) if y-1 >= 0 and x+1 < self.COLS else None
        right_down = self.convert2Dto1D(x+1,y+1) if y+1 < self.ROWS and x+1 < self.COLS else None

        directions = [up, down, left, right, left_up, left_down, right_up, right_down]
        #directions = [up, down, left, right]
        neighbors = []
        for dir_ in directions:
            if dir_ is not None and not self.grid_cells[dir_].is_brick:
                neighbors.append(self.grid_cells[dir_])

        return neighbors
    
    def movingPolygon (self): 
        pass