def fibonacci_while_loop(max_value):
    sequence = []
    a, b = 0, 1
    while a < max_value:
        sequence.append(a)
        a, b = b, a + b
    return sequence

max_val = int(input("Enter the maximum value: "))
print(f"Fibonacci sequence (less than {max_val}): {fibonacci_while_loop(max_val)}")
