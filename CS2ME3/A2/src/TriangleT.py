## @file TriangleT.py
#  @author Kyle Carnrite
#  @brief Implementation of the TriangleT class
#  @date February 15th
from Shape import Shape

class TriangleT(Shape):

    ## @brief Constructor for TriangleT 
    #  @details Assumes arguments provided are correct type, ss and ms > 0
    #  @param xs, ys, ss, ms: Values for TriangleT  
    def __init__(self, xs, ys, ss, ms):
        if not (ss > 0 and ms > 0):
            raise ValueError
        self.x = xs
        self.y = ys
        self.s = ss
        self.m = ms

    ## @brief Gets x 
    #  @return Returns x
    def cm_x(self):
        return self.x

 
    ## @brief Gets y 
    #  @return Returns y
    def cm_y(self):
        return self.y

    ## @brief Gets mass of TriangleT
    #  @return Returns m
    def mass(self):
        return self.m

    ## @brief Gets moment of inertia for TriangleT 
    #  @return Returns moment of inertia
    def m_inert(self):
        return (self.m * self.s ** 2) / 12
