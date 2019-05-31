#Method 1:   sumToNumber(n)
def sumToNumber(n):
    sum = 0
    for x in range(n + 1):
        sum += x
    return sum

#Method 2:   sumBetween(a,b)
def sumBetween(a, b):
    sum = 0
    for x in range(a, b + 1):
        sum += x
    return sum

#Method 3:   sumOddsBetween(a,b)
def sumOddsBetween(a, b):
    sum = 0
    for x in range(a, b + 1):
        if x % 2 == 1:
            sum += x
    return sum
  
#Method 4:   power(a,n)
def power(a, n):
    sum = 1
    for i in range(n):
        sum *= a
    return sum


#Method 5:   factorial(n)
def factorial(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a

#Method 6:   arithmeticMean(dataList)
def arithmeticMean(a):
    return sum(a)/len(a)
    
