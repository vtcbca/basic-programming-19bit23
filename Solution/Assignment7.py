def triangle_pattern_string_multiplication(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i) * 2
        numbers = " ".join(str(x) for x in range(1, 2 * i))
        print(spaces + numbers)

n = int(input("Enter the number of lines: "))
triangle_pattern_string_multiplication(n)
