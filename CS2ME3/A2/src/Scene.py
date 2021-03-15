## @file Scene.py
#  @author Kyle Carnrite
#  @brief
#  @date February 15th, 2021
#  @details
from scipy.integrate import odeint

class Scene:

    ## @brief Constructor for BodyT 
    #  @details Assumes arguments will be correct type, len(ms) = len(ys) = len(ss), ms > 0 
    #  @param xs, ys, ss, ms: Values for TriangleT  
    def __init__(self, s, Fx, Fy, vx, vy):
        self.s = s
        self.Fx = Fx
        self.Fy = Fy
        self.vx = vx
        self.vy = vy

    ## @brief Gets shape from Scene 
    #  @return Returns s 
    def get_shape(self):
        return self.s

    ## @brief Gets unbalanced forces 
    #  @return Returns Fx and Fy  
    def get_unbal_forces(self):
        return self.Fx, self.Fy

    ## @brief Gets initial velocity 
    #  @return Returns vx and vy  
    def get_init_velo(self):
        return self.vx, self.vy

    ## @brief Sets shape
    #  @details Assumes argument passed will be Shape 
    def set_shape(self, s):
        self.s = s

    ## @brief Sets unbalanced Forces
    #  @details Assumes arguments passed will be valid type
    def set_unbal_forces(self, Fx, Fy):
        self.Fx = Fx
        self.Fy = Fy

    ## @brief Sets initial velocity 
    #  @details Assumes argument passed will be valid types 
    def set_init_velo(self, vx, vy):
        self.vx = vx
        self.vy = vy

    ## @brief Runs simulation 
    #  @details Assumes arguments passed will be valid types
    #  @return Returns array with values from simulation
    def sim(self, tfinal, nsteps):
        def ode(w,t):
            return [w[2], w[3], self.Fx(t)/self.s.mass(), self.Fy(t)/self.s.mass()]
        t = []
        for i in range (nsteps):
            t.append((i*tfinal)/float(nsteps-1))
        return t, odeint(ode, [self.s.cm_x(), self.s.cm_y(), self.vx, self.vy], t)
