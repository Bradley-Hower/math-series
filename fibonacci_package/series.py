def fibonacci(n):
  """A series of numbers where the subsequent number is the sum of the prior two. Begins with zero. By definition, Fibonacci at index 0 is 0 and fibonacci at index 1 is 1. To resolve, recusion is required.
  ex: fibonacci(0) = 0
      fibonacci(1) = 1
      fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 + 0 = 1
      fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
      fibonacci(7) = fibonacci(6) + fibonacci(5) = 8 + 5 = 13
  """
  if n < 0:
     return "Sorry, only positives"
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)
  
def lucas(n):
  """A series of numbers where the subsequent number is the sum of the prior two. Begins with two. By definition, Fibonacci at index 0 is 2 and fibonacci at index 1 is 1. To resolve, recusion is required.
    ex: lucas(0) = 2
    lucas(1) = 1
    lucas(2) = lucas(1) + lucas(0) = 1 + 2 = 3
    lucas(3) = lucas(2) + lucas(1) = 3 + 1 = 4
    lucas(7) = lucas(6) + lucas(5) = 18 + 11 = 29
  """
  if n < 0:
     return "Sorry, only positives"
  if n == 0:
    return 2
  if n == 1:
    return 1
  return lucas(n-1) + lucas(n-2)




def sum_series(n, first=0, second=1):
  if n < 0:
    return "Sorry, only positives"
  if n == 0:
    return first
  if n == 1:
    return second
  return sum_series(n-1, first, second) + sum_series(n-2, first, second)


