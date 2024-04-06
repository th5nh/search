from coordinate import Coordinate
from const import *
class Point : 
    def __init__(self, coor = Coordinate()) :
        self.coor = coor
        self.symbol = 'x'
        self.isBlock = False
        self.color = WHITE
        self.x = coor.x
        self.y = coor.y
    def display(self) :
        self.coor.display()
    def draw (self , matrix) :
        try: 
            matrix[self.coor.y] [self.coor.x] = self
            return matrix  
        except : 
            print(self.coor.y, self.coor.x)
            print (matrix[1][22])

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

