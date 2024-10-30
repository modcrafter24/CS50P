while True:
    expression = input("Fraction: ")
    try:
        x, y = expression.split("/")
        if x.isdecimal() and y.isdecimal():
            x, y = int(x), int(y)
            if x <= y and y != 0:
                break
    except ValueError:
        pass

percentage = round((x/y)*100)

if percentage <= 1:
    print('E')
elif percentage >= 99:
    print('F')
else:
    print(f"{percentage}%")
