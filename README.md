# TPRG-2-Assgn-1-2023
# Area of a rectangle pytest check 
def test_area_rectangle():
    # Test cases for area_rectangle function.
    assert area_rectangle(4, 5) == 20
    assert area_rectangle(0, 0) == 0
    assert area_rectangle(8, 12) == 96

# Area of a triangle
def test_area_triangle():
    #Test cases for area_rectangle function.
    assert area_triangle(3, 4) == 6.0
    assert area_triangle(0, 0) == 0
    assert area_triangle(6, 8) == 24.0

# Area of circle
def test_area_circle():
    #Test cases for area_circle.
    assert area_circle(5) == 78.53981633974483
    assert area_circle(0) == 0
    assert area_circle(10) == 314.1592653589793
