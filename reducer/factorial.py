from reduce_ import reduce_

factorial = lambda n: reduce_(lambda a, b: a * b, range(1, n + 1))

print(factorial(10))
