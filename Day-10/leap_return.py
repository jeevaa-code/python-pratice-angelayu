def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(yearly, monthly):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_true = is_leap(yearly)
    if (not is_true):
        return (month_days[monthly - 1])
    elif (is_true):
        if monthly == 2:
            return (29)
        else:
            return (month_days[monthly - 1])


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)




