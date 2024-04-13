from model_point import EdgePoint 
from coordinate import Coordinate

class Edge : 
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.edgePoints  = self.calculateEdgePoints()

    def calculateEdgePoints (self): 
        x1, y1 = self.start.coor.x, self.start.coor.y
        x2, y2 = self.end.coor.x, self.end.coor.y
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        edgePoints = []

        while x1 != x2 or y1 != y2:
            edgePoints.append(EdgePoint(Coordinate(x1, y1)))
            e2 = 2 * err

            if (e2 > -dy and e2 < dx):
                if(dy > dx) :
                    err -= dy
                    x1 += sx
                else:
                    err += dx
                    y1 += sy
            else :
                if e2 > -dy:
                    err -= dy
                    x1 += sx
                if e2 < dx:
                    err += dx
                    y1 += sy

        edgePoints.append(EdgePoint(Coordinate(x2, y2)))
        return edgePoints
    
    def display (self): 
        for point in self.edgePoints:
            point.display()

    def draw (self, matrix ): 
        for point in self.edgePoints: 
            matrix = point.draw(matrix) 
            
        return matrix


