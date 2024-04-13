from coordinate import Coordinate
from const import *
import copy

class Point : 
    def __init__(self, coor = Coordinate()):
        self.coor = coor
        self.symbol = 'x'
        self.isBlock = False
        self.color = WHITE
        self.x = coor.x
        self.y = coor.y
        self.isVisited = False
    
    def __copy__ (self): 
        return Point(copy.copy(self.coor)) 

    def display(self):
        self.coor.display()

    def draw (self , matrix):
        try: 
            matrix[self.coor.y] [self.coor.x] = self
            return matrix  
        except: 
            print(self.coor.y, self.coor.x)

    def moving (self, dis):
        self.coor.x = self.x + dis
        self.x = self.coor.x 
    
    def compare (self, point ):
        return self.coor.compare(point.coor)

    def distance_step (self , point): 
        return self.coor.distance_step(point.coor)

class WallPoint (Point): 
    def __init__(self, coor=Coordinate()):
        super().__init__(coor)
        self.color = BLACK
        self.isBlock = True

class EdgePoint(Point): 
    def __init__(self, coor=Coordinate(), color = SAND):
        super().__init__(coor)
        self.color = color 
        self.isBlock = True

class VertexPoint(Point): 
    def __init__(self, coor=Coordinate(), color = SILK):
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