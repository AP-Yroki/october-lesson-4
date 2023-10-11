def date(day, month, year):
    if year < 1:
        return False
    if month < 1 or month > 12:
        return False
    if month in[4, 6, 9, 11] and day > 30:
        return False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if day > 29:
            return False
        else:
            if day > 28:
                return False
    if day < 1 or day > 31:
        return False
    return True

print(date(11, 10, 2023))