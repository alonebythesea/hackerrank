def is_leap(year):
    leap = False
    if year % 4 == 0 or year % 400 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year == 2000 or year == 2400:
                leap = True   
    return leap

year = int(input())
print(is_leap(year))