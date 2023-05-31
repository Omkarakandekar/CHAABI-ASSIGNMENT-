factorial = lambda n: 1 if n == 0 or n == 1 else n * factorial(n - 1)

number = int(input("Enter a number: "))
result = factorial(number)

print("Factorial of", number, "is:", result)
