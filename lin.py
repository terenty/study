import datetime
import sys

def read_date():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    year, month, day = next(reader)
    return datetime.datetime(year, month, day)

def main():
    date = read_date()
    print(date)
    days_add = datetime.timedelta(int(input()))
    print(days_add)
    result = date + days_add
    print(result.year, result.month, result.day)

if __name__ == "__main__":
    main()


