from reducer.reduce_ import reduce_

max_ = lambda numbers: reduce_(lambda a, b: a if a >= b else b, numbers)
min_ = lambda numbers: reduce_(lambda a, b: a if a <= b else b, numbers)

numbers = [9, 8, 4, 5, 3, 6]

print(f'min {max_(numbers)}, max {min_(numbers)}')