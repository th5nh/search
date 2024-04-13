from coordinate import Coordinate
from const import *
import copy

class Point : 
    def __init__(self, coor = Coordinate()) :
        self.coor = coor
        self.symbol = 'x'
        self.isBlock = False
        self.color = WHITE
        self.x = coor.x
        self.y = coor.y
        self.isVisited = False
    
    def __copy__ (self) : 
        return Point(copy.copy(self.coor)) 

    def display(self) :
        self.coor.display()
    def draw (self , matrix) :
        try: 
            matrix[self.coor.y] [self.coor.x] = self
            return matrix  
        except : 
            print(self.coor.y, self.coor.x)
    def moving (self, dis) :
        self.coor.x = self.x + dis
        self.x = self.coor.x ; 

    #get neighbor 
    def getNeighbour (self, graph:list) : 
        neigbors = []  
        # the loop we seem like to think is the delta 
        delta_x = -1 
        delta_y = -1
        while (delta_y <= 1) :
            delta_x = -1
            while ( delta_x <= 1) :
                if (delta_y == 0 and delta_x == 0 ) : 
                    delta_x += 1 
                    continue                
                cur_x = self.x  + delta_x 
                cur_y = self.y + delta_y 
                cur_node = graph [cur_y][cur_x] 
                if cur_node.isBlock == False  : 
                    cur_node.color = BLUE 
                    neigbors.append(cur_node) 
                delta_x += 1 
            delta_y += 1 
        return neigbors
    
    def compare (self, point ) :
        return self.coor.compare(point.coor) ;
    def distance_step (self , point) : 
        return self.coor.distance_step(point.coor) ;

class WallPoint (Point) : 
    def __init__(self, coor=Coordinate()):
        super().__init__(coor)
        self.color = BLACK
        self.isBlock = True

class EdgePoint(Point) : 
    def __init__(self, coor=Coordinate(), color = YELLOW):
        super().__init__(coor)
        self.color = color 
        self.isBlock = True

class VertexPoint(Point) : 
    def __init__(self, coor=Coordinate(), color = ORANGE):
        super().__init__(coor)
        self.color = color 
        self.symbol = 'v'
        self.isBlock = True

class StationPoint(Point) :
    def __init__(self, coor=Coordinate(), color = GREEN):
        super().__init__(coor)
        self.color = color
        self.symbol = 't'
    
class StartPoint(Point) : 
    def __init__(self, coor=Coordinate(), color = RED):
        super().__init__(coor) 
        self.color = color
        self.symbol = 's'

class EndPoint(Point) : 
    def __init__(self, coor=Coordinate() , color = PURPLE):
        super().__init__(coor)
        self.color = color 
        self.symbol = 'e'

