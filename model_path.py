from model_point import Point  
from coordinate import Coordinate
from const import * 

class Path : 
    def __init__(self, point  : Point = Point() , foot_print : list = [], cost = 0.0) :
        self.foot_print =foot_print.copy()
        self.cost = cost
        self.level = len(foot_print)
        self.addStep(point)
    #this method just receive the next neighbor 
    def addStep (self, to_point :Point ) : 
        lenght = len (self.foot_print) 
        if (lenght > 0 ):
            last_point = self.foot_print[len(self.foot_print)-1]
            self.cost += last_point.distance_step(to_point)

        self.foot_print.append(to_point ) 
        self.level += 1
    def display (self) : 
        for point in self.foot_print : 
            point.display() 
            print ("->", end=" ")
        print (self.cost, end=",")
        print(self.level)
    def highlight( self) : 
        for point in self.foot_print :
            point.color = GREEN
    def contain (self, check_point ) : 
        for point in self.foot_print : 
            if (point.compare (check_point) == True) :
                return True 
        return False
    def destination (self) : 
        return self.foot_print[len(self.foot_print)-1]