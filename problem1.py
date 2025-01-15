#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side

assert hypotenuse(3,4,True) == 5
(2 points)
"""

import math, os

def hypotenuse(l1, l2, ish):
    l1 = float(l1)
    l2 = float(l2)
    ish = bool(ish)
    if ish == False:
        if l1 > l2:
            hyp = l1
            otherside = l2
        if l2 > l1:
            hyp = l2
            otherside = l1
        missingside = math.sqrt((math.pow(hyp,2)) - (math.pow(otherside, 2)))
    if ish == True:
        missingside = math.sqrt((math.pow(l1, 2)  + math.pow(l2, 2)))
    return missingside


if __name__ == "__main__":
    assert hypotenuse(3,4,True) == 5
    assert hypotenuse(5,12,True) == 13
    assert hypotenuse(3,5,False) == 4
    assert hypotenuse(13,12,False) == 5


#done!