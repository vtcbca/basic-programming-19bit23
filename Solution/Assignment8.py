def alphabet_pattern_string_multiplication(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i) * 2
        increasing = " ".join(chr(64 + x) for x in range(1, i + 1))
        decreasing = " ".join(chr(64 + x) for x in range(i - 1, 0, -1))
        print(spaces + increasing + " " + decreasing)

n = int(input("Enter the number of lines: "))
alphabet_pattern_string_multiplication(n)
