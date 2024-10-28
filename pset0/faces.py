def convert(string):
    return (string.replace(':)', '🙂')).replace(':(', '🙁')

def main():
    input_string = input("Please Enter a String: ")
    print(convert(input_string))

main()


