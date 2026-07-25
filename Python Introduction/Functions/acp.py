# Program to print Fibonacci series up to n terms

n = int(input("Enter the number of terms: "))

a = 0
b = 1

if n <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c