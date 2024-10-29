def main():

    time = input("What time is it? ")

    if time.endswith('a.m.'):
        time = time[:-5]
    elif time.endswith('p.m.'):
        time = time[:-5]
        hours, minutes = time.split(":")
        time = str(int(hours) + 12) + ':' + str(minutes)
        
    converted_time = convert(time)

    if converted_time >= 7.0 and converted_time <= 8.0:
        print("breakfast time")
    elif converted_time >= 12.0 and converted_time <= 13.0:
        print("lunch time")
    elif converted_time >= 18.0 and converted_time <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return (float(hours) + (float(minutes)/60.0))

if __name__ == "__main__":
    main()
