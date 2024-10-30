month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        input_string = input("Date: ")
        try:
            if count_in_str(input_string, '/') == 2:
                month, day, year = input_string.split('/')
                month = int(month)
                day = int(day)
                year = int(year)
                if not(0 < day < 32) or not(0 < month < 13):
                    continue
                else:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

            elif count_in_str(input_string, ' ') == 2 and count_in_str(input_string, ',') == 1:
                #print("Here")
                month, day, year = input_string.split(' ')
                #print(month, day, year)
                try:
                    month = month_list.index(month) + 1
                    #print("Here")
                except ValueError:
                    #print("Here")
                    continue
                day = int(day[:-1])
                if not(0 < day < 32):
                    continue
                year = int(year)
                #print(month, day, year)
                print(f"{year:04}-{month:02}-{day:02}")
                break

        except:
            continue

def count_in_str(s, c):
    return ((len(s.split(c)) - 1))

main()
