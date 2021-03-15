## @file CircleT.py
#  @author Kyle Carnrite
#  @brief Implementation of CircleT class 
#  @date February 15th, 2021

from Shape import Shape

class CircleT(Shape):
    ## @brief Constructor for CircleT 
    #  @details Assumes arguments provided are correct type, m and r > 0
    #  @param xs, ys, rs, ms: Values for CircleT  
    def __init__(self, xs, ys, rs, ms):
        if not (ms > 0 and rs > 0):
            raise ValueError
        self.x = xs
        self.y = ys
        self.r = rs
        self.m = ms

    ## @brief Gets x   
    #  @return Returns x
    def cm_x(self):
        return self.x

    ## @brief Gets y 
    #  @return Returns y
    def cm_y(self):
        return self.y

    ## @brief Gets m 
    #  @return Returns mass 
    def mass(self):
        return self.m

    ## @brief Gets moment of inertia 
    #  @return Returns moment of inertia
    def m_inert(self):
        return ((self.m* self.r ** 2)/ 2)
