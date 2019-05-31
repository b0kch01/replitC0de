number = int(input())
first = (number % 100) // 10
second = (number % 10) // 1

print(str(second) + str(first))
