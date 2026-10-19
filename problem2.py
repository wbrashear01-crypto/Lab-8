from rational_def import numerator, denominator, rational

def div_rational(x,y):
  '''
  rational number, rational number -> rational number
  Divides the first rational number by the second rational number.

  >>> div_rational(rational(2,3),rational(3,9))
  rational(2,1)
  >>> div_rational(rational(1,2),rational(3,5))
  rational(5,6)
  >>> div_rational(rational(3,4),rational(2,5))
  rational(15,8)
  '''
num=numerator(x)*denominator(y)
den=denominator(x)*numerator(y)
return(num,den)
