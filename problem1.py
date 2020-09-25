def smallest_multiple(number):
  step = 1
  test = step

  for i in range(2, number + 1):
    while True:
      is_multiple = True
      # test if number is multiple of all incorporated numbers so far
      for j in range(1, i + 1):
        if test % j != 0:
          is_multiple = False
          break

      # if all numbers are multiple
      # incorporate test number as new step
      if is_multiple:
        step = test
        break

      test += step

  return test


print smallest_multiple(20)