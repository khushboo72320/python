#recursive fun is a fun it to itself yo solv a problem


def calculate_factorial(n):
  if n == 0 or n == 1:
     return 1
  else:  
     return n * calculate_factorial(n-1) 
print(calculate_factorial(11))


#fibnocci 
def fibnocci(n): 
   if n == 0:
      return 0
   elif n == 1: 
    return 1
   else:
    return fibnocci(n-1) + fibnocci(n-2)
print(fibnocci(7))


  