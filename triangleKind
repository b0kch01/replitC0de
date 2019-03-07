def triangle_kind(a, b, c):
    if (a == b and b == c):
        return "equilateral"
    elif not((a + b > c) and (b + c > a) and (c + a > b)):
        return "invalid triangle"
    elif (a == b) or (a == c) or (c == b):
        return "isosceles"
    return "scalene"
