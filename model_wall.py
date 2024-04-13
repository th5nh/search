from model_point import WallPoint
from coordinate import Coordinate

class Wall : 
    def __init__(self, height = 1, width = 1) -> None:
        self.height = height
        self.width = width
        self.borders = self.buildWall()
        self.symbol = '#'

    def buildWall (self):
        borders = []
        #build bot  
        y = 0
        for i in range (1,self.width) : 
            borders.append(WallPoint(Coordinate(i,y)))
        #build top 
        y = self.height 
        for i in range (1,self.width) : 
            borders.append(WallPoint(Coordinate(i,y)))
        
        #build left 
        x = 0
        for i in range(0,self.height+1) : 
            borders.append(WallPoint(Coordinate(x,i)))
        x = self.width ; 
        for i in range (0, self.height+1) :
            borders.append(WallPoint(Coordinate(x,i)))
        return borders
        
    def display (self): 
        for point in self.borders: 
            point.display()

    def draw (self, matrix): 
        for point in self.borders: 
            matrix = point.draw(matrix)
        return matrix