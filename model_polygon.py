from coordinate import Coordinate 
from model_point import EdgePoint , VertexPoint 
from model_edge import Edge

class Polygon : 
    def __init__(self, coors) -> None:
        # An array of vertices that have VertexPo
        self.vertices = [] 
        self.edges = [] 
        for i in range (0,len(coors),2 ):
            coor1 = Coordinate(coors[i], coors[i+1]) 
            self.vertices.append(VertexPoint(coor1))
        numsOfEdges = 0 
        for i in range (len(self.vertices)) :
            start = self.vertices[i] 
            
            end = self.vertices[i+1] if i < len(self.vertices) - 1  else self.vertices[0] 
            self.edges.append(Edge(start, end))
        
        self.sides = len(self.vertices)

    def display (self) : 
        for i in range (self.sides) : 
            self.edges[i].display() 

    def draw (self, matrix) : 
        for i in range (self.sides) : 
            matrix = self.edges[i].draw(matrix)
        for v in self.vertices : 
            matrix = v.draw(matrix) 
        return matrix
