def pattern_string_multiplication(rows):
    for i in range(1, rows + 1):
        print("* " * i)

rows = int(input("Enter the number of rows: "))
pattern_string_multiplication(rows)
