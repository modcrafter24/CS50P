from emoji import emojize

input_string = input("Input: ")
output_string = emojize(input_string, language='alias')
print(f"Output: {output_string}")