## @file test_All.py
#  @author Kyle Carnrite
#  @brief
#  @date February 15th, 2021
#  @details 
import pytest 
from Shape import *
from CircleT import *
from TriangleT import *
from BodyT import *
from Scene import *
from Plot import *



##########################
# CircleT Testing
##########################

# Constructor test:
a = CircleT(10,20,5,100)
def test_CircleT_Excp1():
    with pytest.raises(ValueError):
        error = CircleT(5, 3, 0, 5)

def test_CircleT_Excp2():
    with pytest.raises(ValueError):
        error2 = CircleT(5,3,5,0)

def test_CircleT_Excp3():
    with pytest.raises(ValueError):
        error3 = CircleT(5,5,0,0)

# cm_x test:
def test_circlet_cm_x1():
    assert a.cm_x() == 10

# cm_y test:
def test_circlet_cm_y1():
    assert a.cm_y() == 20


# mass test:
def test_circlet_mass1():
    assert a.mass() == 100

# m_inert test:
def test_m_inert1():
    assert a.m_inert() == 1250


###########################
# TriangleT Testing:
###########################

# Constructor test
a = TriangleT(10,20,10,100)
def test_TriangleT_Excp1():
    with pytest.raises(ValueError):
        error = TriangleT(5,3,-1,10)

def test_TriangleT_Excp2():
    with pytest.raises(ValueError):
        error = TriangleT(5,3,10,0)

def test_TriangleT_Excp3():
    with pytest.raises(ValueError):
        error = TriangleT(5,3,0,0)

# cm_x test:
def test_TriangleT_cm_x():
    assert a.cm_x() == 10

# cm_y test:
def test_TriangleT_cm_y():
    assert a.cm_y() == 20

# mass test:
def test_TriangleT_mass():
    assert a.mass() == 100

#m_inert test:
def test_m_inert1():
    assert a.m_inert() == pytest.approx(833.3333)

###########################
# BodyT Testing:
###########################

# Constructor tests:
body1 = BodyT([1,2,3],[4,5,6],[7,8,9])
def test_BodyT_Excp1():
    with pytest.raises(ValueError):
        error = BodyT([1,2], [5,5,1], [8,2,9])

def test_BodyT_Excp2():
    with pytest.raises(ValueError):
        error = BodyT([5,8,9], [2,8.2], [8,2,0])

# cm_x test:
def test_BodyT_cm_x():
    assert body1.cm_x() == pytest.approx(2.083333)

# cm_y test:
def test_BodyT_cm_y():
    assert body1.cm_y() == pytest.approx(5.083333)

# mass test:
def test_BodyT_mass():
    assert body1.mass() == 24 

# m_inert test:
def test_m_inert():
    assert body1.m_inert() == pytest.approx(3188.67)

#######################
# Scene Testing
#######################
g = 9.81
m = 100
def Fy(t):
    return -g*m
triangle1 = TriangleT(10,100,50,100)
circle1 = CircleT(10,50,50,100)
scene1 = Scene(triangle1,0, Fy, 0, 0)

# get_shape test:
def test_Scene_get_shape():
    assert scene1.get_shape() == triangle1

# get_init_velo test:
def test_Scene_get_init_velo():
    assert scene1.get_init_velo() == (0, 0)

# set_shape test:
def test_Scene_set_shape():
    scene1.set_shape(circle1)
    assert scene1.get_shape() == circle1

# set_initial_velo test:
def test_Scene_set_init_velo():
    scene1.set_init_velo(1,1)
    assert scene1.get_init_velo() == (1,1)


