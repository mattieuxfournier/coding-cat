def Third_Largest(numbers):
  '''
    Returned the wrong index
  '''
  if len(numbers) < 4:
    return "This list is too short"

  return sorted(numbers)[-2]
