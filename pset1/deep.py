input_string = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

input_string = (input_string.strip()).lower()

if input_string == "42" or input_string == "forty-two" or input_string == "forty two":
    print('Yes')
else:
    print('No')
