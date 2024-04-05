from model_wall import Wall 
from model_polygon import Polygon
from model_point import StartPoint, EndPoint 
from coordinate import Coordinate
from model_point import Point
import sys 

class Matrix : 
    def __init__(self) -> None:
        pass
    def parseFile (self, fileName) : 
        sys.stdin = open (fileName, 'r')
        with open (fileName ,'r') as file :
            lines = file.readlines()
            size = lines[0].split(',')
            self.width = int(size[0])
            self.height = int(size[1])
            fromToCoors = lines[1].split(',')
            
            startCoor = Coordinate(fromToCoors[0] , fromToCoors[1])
            endCoor = Coordinate(fromToCoors[2], fromToCoors[3])

            #define start end point 
            self.startPoint = StartPoint(startCoor) 
            self.endPoint = EndPoint(endCoor) 

            #defin wall 
            self.border = Wall(self.height, self.width)

            #add polygons  
            self.polygons = [] 
            self.numsOfPolygons = int (lines[2]) 
            for i in range (self.numsOfPolygons) : 
                polygon = Polygon(lines[i+3].split(','))
                self.polygons.append(polygon) ; 

            self.graph = self.draw()

    def draw(self) : 
        graph = [] 
        for y in range (0, self.height+1, 1) : 
            horizon = []
            for x in range(0 , self.width + 1, 1) : 
                horizon.append(Point(Coordinate(x, y)))
            graph.append(horizon)
        for polygon in self.polygons: 
            graph = polygon.draw(graph) 
        graph = self.border.draw(graph) 
        graph = self.startPoint.draw(graph) 
        graph = self.endPoint.draw(graph) 
        return graph
    def display (self) : 
        for y in range (self.height, -1, -1) :             
            for x in range(0 , self.width + 1, 1) : 
                self.graph[y][x].display()
            print('')

        
                 


myMatrix = Matrix () 
myMatrix.parseFile('input.txt')
myMatrix.display()





                
            