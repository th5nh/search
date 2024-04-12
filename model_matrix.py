from model_wall import Wall 
from model_polygon import Polygon
from model_point import StartPoint, EndPoint, StationPoint 
from coordinate import Coordinate
from model_point import Point
import sys 

class Matrix : 
    def __init__(self) -> None:
        pass
    def parseFile (self, fileName :str ) : 
        sys.stdin = open (fileName, 'r')
        with open (fileName ,'r') as file :
            lines = file.readlines()
            size = lines[0].split(',')
            self.width = int(size[0])
            self.height = int(size[1])
            fromToCoors = lines[1].split(',')
            
            startCoor = Coordinate(fromToCoors[0] , fromToCoors[1])
            endCoor = Coordinate(fromToCoors[2], fromToCoors[3])
            stationCoor_1 = Coordinate(fromToCoors[4], fromToCoors[5])

            #define start end point 
            self.startPoint = StartPoint(startCoor) 
            self.endPoint = EndPoint(endCoor) 

            if (len (fromToCoors) > 4 ) :
                self.haveStations = True
                stationCoor_1 = Coordinate(fromToCoors[4], fromToCoors[5])
                stationCoor_2 = Coordinate(fromToCoors[6], fromToCoors[7])
                self.stationPoint_1 = StationPoint(stationCoor_1)
                self.stationPoint_2 = StationPoint(stationCoor_2)
                #defin wall 
            self.border = Wall(self.height, self.width)

            #add polygons  
            self.polygons = [] 
            self.numsOfPolygons = int (lines[2]) 
            for i in range (self.numsOfPolygons) : 
                polygon = Polygon(lines[i+3].split(','))
                self.polygons.append(polygon) ; 

            self.graph = self.draw()
            self.display()

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

        graph = self.stationPoint_1.draw(graph)
        graph = self.stationPoint_2.draw(graph)

        return graph
    def display (self) : 
        for y in range (0,self.height+1, 1) :             
            for x in range(0 , self.width + 1, 1) : 
                self.graph[y][x].display()
            print('')
    def copy(self) : 
        pass






                
            