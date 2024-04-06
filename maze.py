import pygame
from const import *
import random
from model_matrix import myMatrix
from model_point import Point
# you can change the random seed but when you submit your work, it should be run on my random seed!
# random.seed(2345)
#random.seed(142857) # no path seed

COLS, ROWS = myMatrix.width+1, myMatrix.height+1

RES = WIDTH, HEIGHT = 800+2*BOUND + (ROWS-1)*(A1), 800+2*BOUND + (COLS-1)*(A1)

class Node:
    def __init__(self, point, a, id) -> None:
        
        self.rect = pygame.Rect(point.x *(A+A1) + BOUND, point.y *(A+A1)+BOUND, a, a)

        self.color = point.color
        self.id = id
        self.is_brick = point.isBlock

    def draw(self, sc:pygame.Surface) -> None:
        pygame.draw.rect(sc, self.color, self.rect)

    def _set_color(self, color):
        self.color = color

    def set_color(self, color, sc:pygame.Surface):
        self.color = color
        self.draw(sc)

        # change the speed here
        pygame.time.delay(10)
        pygame.display.update()

class SearchSpace:
    def __init__(self) -> None:
        self.grid_cells:list[Node] = []
        for i in range(0,ROWS):
            for j in range(0, COLS):
                # define the brick's appearing
                node = myMatrix.graph[i][j]
                self.grid_cells.append(Node(node, A,i*COLS + j))
        
        start_id = myMatrix.startPoint.y*COLS+myMatrix.startPoint.x
        end_id = myMatrix.endPoint.y*COLS+myMatrix.endPoint.x

        # self.start:Node = self.grid_cells[start_id]
        # self.start.id = start_id
        # self.start.is_brick = False
        # self.start._set_color(ORANGE)
        # self.goal:Node = self.grid_cells[end_id]
        # self.goal.is_brick = False
        # self.goal.id = end_id
        # self.goal._set_color(PURPLE)
        self.start:Node = self.grid_cells[0]
        self.start.is_brick = False
        self.start._set_color(ORANGE)
        self.goal:Node = self.grid_cells[-1]
        self.goal.is_brick = False
        self.goal._set_color(PURPLE)

        self.font = pygame.font.SysFont('Aral', 15) 

        #add text to wall : 

        

    def draw(self, sc:pygame.Surface):
        for node in self.grid_cells:
            node.draw(sc)
        
        
        for i in range(COLS) : 
            label = self.font.render(str(i) ,True, WHITE )
            sc.blit(label , (self.grid_cells[i].rect.center))

        for i in range (ROWS) : 
            label = self.font.render(str(i) ,True, WHITE )
            sc.blit(label , (self.grid_cells[i*COLS].rect.center))            
        pygame.display.flip()

    def get_length(self):
        return len(self.grid_cells)

    def is_goal(self, node:Node):
        return node.id == self.goal.id

    def get_neighbors(self, node: Node) -> list[Node]:
        x, y = node.id%COLS, node.id//COLS

        # define the directions of agent
        up    = (y-1)*COLS + x if y-1 >= 0 else None
        down  = (y+1)*COLS + x if y+1 < ROWS else None
        left  = y*COLS + (x-1) if x-1 >= 0 else None
        right = y*COLS + (x+1) if x+1 < COLS else None

        left_up = (y-1)*COLS + (x-1) if y-1 >= 0 and x-1 >= 0 else None
        left_down = (y+1)*COLS + (x-1) if y+1 < ROWS and x-1 >= 0 else None
        right_up = (y-1)*COLS + (x+1) if y-1 >= 0 and x+1 < COLS else None
        right_down = (y+1)*COLS + (x+1) if y+1 < ROWS and x+1 < COLS else None

        directions = [up, down, left, right, left_up, left_down, right_up, right_down]
        # directions = [up, down, left, right]
        neighbors = []
        for dir_ in directions:
            if dir_ is not None and not self.grid_cells[dir_].is_brick:
                neighbors.append(self.grid_cells[dir_])

        return neighbors
