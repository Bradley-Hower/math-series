from fibonacci_package.series import fibonacci

def test_fibonacci_zero():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_fibonacci_one():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_fibonacci_two():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_fibonacci_eight():
  actual = fibonacci(8)
  expected = 13
  assert actual == expected