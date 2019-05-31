
def exactlyOneOdd(a, b):
    odd = 0
    if (a % 2 == 1):
        odd += 1
    if (b % 2 == 1):
        odd += 1
    if (odd > 1 or odd == 0):
        return False
    return True
