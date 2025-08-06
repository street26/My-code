def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial (n-1)
F = int(input("Enter a Number: "))
print(Factorial(F))
