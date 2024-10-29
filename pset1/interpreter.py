expression = input("Please Enter an Arithmatic Expression: ")

x, y, z = expression.split(" ")

x = int(x)
z = int(z)

match y:
    case '+':
        print(float(x + z))
    case '-':
        print(float(x - z))
    case '*':
        print(float(x * z))
    case '/':
        print(float(x / z))    
