def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not(s[0:2].isalpha()):
        return False
    if len(s) > 6 or len(s) < 2:
        return False
    if not(s.isalnum()):
        return False
    num_str =''
    for c in s:
        if c.isdigit():
            num_str += c
        if len(num_str) > 0:
            if not(c.isdigit()):
                return False
    if len(num_str) > 0:
        if num_str[0] == '0':
            return False
    return True

main()

