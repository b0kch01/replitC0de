def arithmeticSequence(initialTerm, commonDifference, numTerms):
    string = str(initialTerm)
    slope = commonDifference
    number = initialTerm
    for i in range(numTerms - 1):
        number += slope
        string += ", " + str(number)
    return string
    
def multiplesList(n, startingNum, endingNum):
    n1 = startingNum
    divisor = n
    string = ""
    for i in range(n1, endingNum + 1):
        if i % divisor == 0:
            if string == "":
                string += str(i)
            else:
                string += ", " + str(i)
    return string
    
def fizzBuzz(n):
  output = ""
  if n % 3 == 0:
    output += "Fizz"
  if n % 5 == 0:
    output += "Buzz"
  if output == "":
    output = str(n)
  return output
    
def fizzBuzzUpTo(n):
    output = ""
    for i in range(1, n + 1):
        if i == n:
            output += fizzBuzz(i)
            break
        else:
            output += fizzBuzz(i) + "\n"
    return output
