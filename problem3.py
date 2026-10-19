from rational_def import numerator, denominator, rational

def print_rational(x):
  '''
  rational number -> None
  This will print a rational number in the form numerator/denominator.

  >>> print_rational(rational(3,4))
  3/4
  >>> print_rational(rational(1,2))
  1/2
  >>> print_rational(rational(5,7))
  5/7
  '''
  print(str(numerator(x))+"/"+str(denominator(x)))
  
