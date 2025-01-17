#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(t1, t2):
    distx = t1[0] - t2[0]
    disty = t1[1] - t2[1]
    hyp = math.sqrt(math.pow(distx, 2) + math.pow(disty, 2))
    return hyp

if __name__ == "__main__":
    d = distance( (2,4) , (6,3) )
    assert round(d,3) == 4.123
    d = distance( (-3,2.2) , (1,2))
    assert round(d,3) == 4.005

#done!
