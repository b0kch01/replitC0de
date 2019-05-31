def next_day(month, day):
  months_30 = [4, 6, 9, 11]
  months_31 = [1, 3, 5, 7, 8, 10, 12] 
  if month == 12 and day == 31:
    month = 1
    day = 1
  elif (month == 2 and day == 28) or (month in months_30 and day == 30) or (month in months_31 and day == 31):
    month = month + 1 
    day = 1
  else:
      day = day + 1
  return str(month) + "/" + str(day)
