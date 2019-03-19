k = int(input()) #number of apples
n = int(input()) #number of people


# Print the result with print()
each = round(k/n)
remainder = k % n

print (each, "apples", "each")
print (remainder, "left", "over")
