def point_location(x,y):
  output = ""
  if x == 0 and y == 0:
    output = "origin"
  elif (x == 0 and y != 0):
    output = "y-axis"
  elif (x != 0 and y == 0):
    output = "x-axis"
  elif x > 0:
    if y > 0:
      output = "I"
    else:
      output = "IV"
  else:
    if y > 0:
      output = "II"
    else:
      output = "III"
  return output
