from rational_def import numerator, denominator, rational

def rationals_are_equal(x,y):
  '''
  rational number, rational number -> boolean
  Takes in two rational numbers and returns True if they are equivalent and False otherwise.

  >>> rationals_are_equal(rational(1,2),rational(2,4))
  True
  >>> rationals_are_equal(rational(3,5),rational(10,1))
  False
  >>> rationals_are_equal(rational(2,1),rational(1,10))
  False
  '''
if numerator(x)*denominator(y)==numerator(y)*denominator(x):
  return True
else:
  return False
