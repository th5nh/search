import sys
from coordinate import Coordinate
from coordinate import Polygon
sys.stdin = open ('input.txt', 'r')


with open ('input.txt' ,'r') as file :
    lines = file.readlines()

border = Coordinate()

coor = lines[0]
border.parse(coor)
border.display()

polygons = []
nums = int(lines[2])

for i in range(nums) :
    polygon = Polygon()
    polygon.parse(lines[3+i])
    polygons.append(polygon)

for polygon in polygons :
    polygon.display()

