from rational_def import numerator, denominator, rational

def mul_rational(x,y):
  '''
  rational number, rational number -> rational number
  Multiplies two rational numbers
  
  >>>mul_rational(rational(2,3),rational(1,3))
  rational(2,9)
  >>>mul_rational(rational(4,6),rational(3,2))
  rational(1,1)
  '''
num=numerator(x)*numerator(y)
den=denominator(x)*denominator(y)
return rational(num,den)
