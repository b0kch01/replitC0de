def isPositive(x):
    if x > 0:
        return True
    else:
        if x == 0:
            return "zero"
        else: 
            return False

def point_location(x, y):
    # Check for non-quadrants
    if (isPositive(x) == "zero") or (isPositive(y) == "zero"):
        if (isPositive(x) == "zero") and (isPositive(y) == "zero"):
            return "origin"
        elif isPositive(x) == "zero":
            return "y-axis"
        return "x-axis"
            
    # Check for quadrants
    if isPositive(x) == True:
        if isPositive(y) == True:
            return "I"
        return "IV"
    else:
        if isPositive(y) == True:
            return "II"
        return "III"
