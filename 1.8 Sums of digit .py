input = int(input())
a = (input % 10) // 1
b = (input % 100) // 10
c = (input % 1000) // 100
print(a + b + c)
