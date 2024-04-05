class Coordinate :
    def __init__ (self , x = 0, y = 0):
        self.x = int(x) ; 
        self.y = int(y) ; 
    def display(self) : 
        print(f"({self.x}, {self.y})", end=" ")
    
    