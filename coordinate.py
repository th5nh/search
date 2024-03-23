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

    def add_polygon(self, polygon):
        self.polygons.append(polygon)

    def display(self):
        matrix = [['0' for _ in range(self.width)] for _ in range(self.height)]

        for polygon in self.polygons:
            min_x = min(coord.x for coord in polygon.coordinates)
            min_y = min(coord.y for coord in polygon.coordinates)

            for edge in polygon.edges:
                start = edge.start
                end = edge.end
                # Draw edges
                if start.x == end.x:
                    # Vertical line
                    for y in range(min(start.y, end.y), max(start.y, end.y) + 1):
                        matrix[y - min_y][start.x - min_x] = '1'
                elif start.y == end.y:
                    # Horizontal line
                    for x in range(min(start.x, end.x), max(start.x, end.x) + 1):
                        matrix[start.y - min_y][x - min_x] = '1'

            for coord in polygon.coordinates:
                matrix[coord.y - min_y][coord.x - min_x] = '1'

        for row in matrix:
            print(''.join(row))


# Example usage:
border = Border(10, 5)

polygon1 = Polygon()
polygon1.parse("0,0, 0,4, 9,4, 9,0")
border.add_polygon(polygon1)

polygon2 = Polygon()
polygon2.parse("2,2, 3,2, 3,3, 2,3")
border.add_polygon(polygon2)

border.display()
