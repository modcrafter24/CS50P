camel_case = input("Please enter camelCase: ")
snake_case = ''

for char in camel_case:
    if char.isupper():
        snake_case += ('_' + char.lower())
    else:
        snake_case += char

print("snake_case: " + snake_case)