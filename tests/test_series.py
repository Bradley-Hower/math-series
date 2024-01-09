from fibonacci_package.series import fibonacci
from fibonacci_package.series import lucas
from fibonacci_package.series import sum_series

## Fibonacci Tests

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

def test_fibonacci_seven():
  actual = fibonacci(7)
  expected = 13
  assert actual == expected

## Lucas Tests

def test_lucas_zero():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_lucas_one():
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test_lucas_two():
  actual = lucas(2)
  expected = 3
  assert actual == expected

def test_lucas_seven():
  actual = lucas(7)
  expected = 29
  assert actual == expected

## sum_series defaults
  
def test_sum_series_default_zero():
  actual = sum_series(0)
  expected = 0
  assert actual == expected

def test_sum_series_default_one():
  actual = sum_series(1)
  expected = 1
  assert actual == expected

def test_sum_series_default_two():
  actual = sum_series(2)
  expected = 1
  assert actual == expected

def test_sum_series_default_seven():
  actual = sum_series(7)
  expected = 13
  assert actual == expected

## sum_series options 2 and 1
  
def test_sum_series_options_zero():
  actual = sum_series(0, 2, 1)
  expected = 2
  assert actual == expected

def test_sum_series_options_one():
  actual = sum_series(1, 2, 1)
  expected = 1
  assert actual == expected

def test_sum_series_options_two():
  actual = sum_series(2, 2, 1)
  expected = 3
  assert actual == expected

def test_sum_series_options_seven():
  actual = sum_series(7, 2, 1)
  expected = 29
  assert actual == expected