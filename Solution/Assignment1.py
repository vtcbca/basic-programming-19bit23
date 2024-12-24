def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursion(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial using recursion: {factorial_recursion(num)}")
