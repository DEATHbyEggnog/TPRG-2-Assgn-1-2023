'''
TPRG 2131 Fall 2023 Assignment 1
Sept, 2023
Phil J <philip.jarvis@durhamcollege>


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.
A/V calculator Menu
(Level 0)
Enter Q/q to quit – select either will gracefully close the 
application and cancel the calculated view option, if set.
Enter V/v to change the calculated view or D/d for default 
view.
(Level 1)
1. First Area/Volume* calulation
2. Second Area/Volume* calculation
3. Third Area/Volume* calculation
4. Fourth Area/Volume* calculation
5. Fifth Area/Volume* calculation

As this stands it will NOT work with your A_V_calc.py file.
'''

#Import functions for testing from other file A_V_calc_starter.py
from A_V_calc import area_circle, volume_sphere, area_rectangle, volume_cube, area_triangle

def test_area_rectangle():
    # Test cases for area_rectangle function.
    assert area_rectangle(4, 5) == 20
    assert area_rectangle(0, 0) == 0
    assert area_rectangle(8, 12) == 96
    
def test_area_triangle():
    #Test cases for area_rectangle function.
    assert area_triangle(3, 4) == 6.0
    assert area_triangle(0, 0) == 0
    assert area_triangle(6, 8) == 24.0
    
def test_area_circle():
    #Test cases for area_circle.
    assert area_circle(5) == 78.53981633974483
    assert area_circle(0) == 0
    assert area_circle(10) == 314.1592653589793
    
def test_volume_sphere():
    #Test cases for volume_sphere.
    assert volume_sphere(5) == 523.5987755982989
    assert volume_sphere(0) == 0
    assert volume_sphere(10) == 4188.790204786391
    
def test_volume_cube():
    #Test cases for volume_cube.
    assert volume_cube(3) == 27
    assert volume_cube(0) == 0
    assert volume_cube(5) == 125
    
