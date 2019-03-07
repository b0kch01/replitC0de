def next_day(month, day):
  months_with_30_days = [4, 6, 9, 11]
  months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
  day = day + 1
  if month == 12 and day == 32:
    month = 1
    day = 1
  elif (month == 2 and day == 29) or (month in months_with_30_days and day == 31) or (month in months_with_31_days and day == 32):
    month = month + 1 
    day = 1
  return str(month) + "/" + str(day)

