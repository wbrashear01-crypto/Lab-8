from rational_def import numerator, denominator, rational

def div_rational(x,y):
  '''
  rational number, rational number -> rational number
  Divide both rational numbers given by one another.

  >>>div_rational(rational(2,3),rational(3,9))
  rational(2,1)
  '''
num=numerator(x)*denominator(y)
den=denominator(x)*numerator(y)
return(num,den)
