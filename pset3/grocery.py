grocery_list = {}
while True:
    try:
        item = input().upper()
    except EOFError:
        print('')
        break

    if item in grocery_list:
        grocery_list[item] += 1
    else:
        grocery_list[item] = 1

for item in sorted(grocery_list):
    print(str(grocery_list[item]) + ' ' + item)
