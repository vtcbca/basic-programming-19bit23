def reverse_string_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

input_str = input("Enter a string: ")
print(f"Reversed string (using for loop): {reverse_string_loop(input_str)}")
