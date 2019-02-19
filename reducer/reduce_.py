def reduce_(callback, reducible_values):
  reduced_value = None
  for index, value in enumerate(reducible_values):
    if index == 0: reduced_value = value
    else: reduced_value = callback(reduced_value, value)

  return reduced_value