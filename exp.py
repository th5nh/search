
import sys, pygame

class Coordinate:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def display(self):
        print(f"({self.x}, {self.y})", end=" ")

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.coordinates = self.calculate_coordinates()

    def calculate_coordinates(self):
        # Calculate the coordinates between the start and end points using Bresenham's line algorithm
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        coordinates = []
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        while x1 != x2 or y1 != y2:
            coordinates.append(Coordinate(x1, y1))
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy
        coordinates.append(Coordinate(x2, y2))
        return coordinates

class Polygon:
    def __init__(self):
        self.coordinates = []
        self.edges = []

    def parse(self, coordinates_str):
        pairs = coordinates_str.split(',')
        for i in range(0, len(pairs)-1, 2):
            coord = Coordinate(pairs[i], pairs[i+1])
            self.coordinates.append(coord)

        # Calculate edges
        num_coords = len(self.coordinates)
        for i in range(num_coords):
            start = self.coordinates[i]
            end = self.coordinates[(i + 1) % num_coords]  # Wrap around to connect last and first coordinates
            edge = Edge(start, end)
            self.edges.append(edge)

    def display(self):
        for edge in self.edges:
            start = edge.start
            end = edge.end
            print(f"Edge: ({start.x},{start.y}) to ({end.x},{end.y})")
        for coord in self.coordinates:
            coord.display()
        print()

    

class Border:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.polygons = []
        self.matrix = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def add_polygon(self, polygon):
        self.polygons.append(polygon)
        for polygon in self.polygons:
            for ver in polygon.coordinates :
                self.draw(ver,1)
            for edge in polygon.edges : 
                for point in edge.coordinates :
                    self.draw(point,2)

    def draw(self,coor,flag = 0) :
        self.matrix[coor.y][coor.x] = flag

    def display(self):
        for row in self.matrix:
            print(row)

# 012100
# 000000



# sys.stdin = open ('input.txt', 'r')


# with open ('input.txt' ,'r') as file :
#     lines = file.readlines()

# size = lines[0].split(',')
# width = int(size[0])
# height = int(size[1])

# maze = Border(width ,height)
# nums = int(lines[2])

# for i in range(nums) :
#     polygon = Polygon()
#     polygon.parse(lines[3+i])
#     maze.add_polygon(polygon)


