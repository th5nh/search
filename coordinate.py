class Coordinate :
    def __init__ (self , x = 0, y = 0):
        self.x = int(x) 
        self.y = int(y)

    def __copy__(self): 
        return Coordinate(self.x , self.y) 
    
    def display(self): 
        print(f"({self.x}, {self.y})", end=" ")

    def compare (self, coor): 
        return self.x == coor.x and self.y == coor.y
    
    def distance_step (self, coor ):
        delta_x = abs (coor.x - self.x) 
        delta_y = abs(coor.y - self.y ) 

        if (delta_x  == 1 and delta_y == 1):
            return 1.5
        if (delta_y == 1 or delta_x == 1): 
            return 1 
        
        return 0