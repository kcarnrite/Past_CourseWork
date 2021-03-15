## @file BodyT.py
#  @author Kyle Carnrite
#  @brief
#  @date February 15th, 2020
from Shape import Shape

class BodyT(Shape):

    ## @brief Constructor for BodyT 
    #  @details Assumes arguments will be correct type, len(ms) = len(ys) = len(ss), ms > 0 
    #  @param xs, ys, ss, ms: Values for TriangleT  
    def __init__(self, xs, ys, ms):
        # Throw ValueError if the length of xs, ys and ms are not the same
        if not (len(xs) == len(ys) == len(ms)):
            raise ValueError
        
        # Throw Value error if not every value of ms is >0
        for i in ms:
            if not (i > 0):
                raise ValueError

        def cm(z, m):
            ans = 0
            for i in range(len(m)):
                ans += z[i] * m[i]
            return ans / sum(m)
        
        def mmom(x, y, m):
            ans = 0
            for i in range(len(m)):
                ans += m[i] * (x[i]**2 + y[i]**2)
            return ans

        self.cmx = cm(xs, ms)
        self.cmy = cm(ys, ms)
        self.m = sum(ms)
        self.moment = mmom(xs, ys, ms) - (sum(ms) * cm(xs,ms)**2) + cm(ys,ms)**2
        
    ## @brief Gets cmx 
    #  @return Returns cmx
    def cm_x(self):
        return self.cmx

    ## @brief Gets cmy 
    #  @return Returns cmy
    def cm_y(self):
        return self.cmy

    ## @brief Gets mass 
    #  @return Returns m 
    def mass(self):
        return self.m

    ## @brief Gets moment of inertia 
    #  @return Returns moment 
    def m_inert(self):
        return self.moment
