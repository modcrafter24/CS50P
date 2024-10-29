vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

input_string = input("Input: ")
output_string = ''
for char in input_string:
    if char in vowel:
        pass
    else:
        output_string += char

print(f"Output: {output_string}")

