#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger(num):
  try:
    num = float(num)
    if num%1 == 0:
      x = True
    else:
      x = False
  except:
    x = False
  return x

if __name__ == "__main__":
  assert isInteger( 9.5 ) == False
  assert isInteger( -2 ) == True    
  assert isInteger("hello") == False
  assert isInteger(0) == True


#done!