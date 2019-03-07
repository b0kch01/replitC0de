def next_day(month, day):
  30_months = [4, 6, 9, 11]
  31_months = [1, 3, 5, 7, 8, 10, 12] 
  if month == 12 and day == 31:
    month = 1
    day = 1
  elif (month == 2 and day == 28) or (30_months and day == 30) or (31_months and day == 31):
    month = month + 1 
    day = 1
  return str(month) + "/" + str(day)

