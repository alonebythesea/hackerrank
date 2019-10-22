from datetime import date

actual_date = map(int, input().split())
expected_date = map(int, input().split())

actual_list = list(actual_date)
expected_list = list(expected_date)

actual = date(day=actual_list[0], month=actual_list[1], year=actual_list[2])
expected = date(day=expected_list[0], month=expected_list[1], year=expected_list[2])

result = 0

if actual > expected:
    if actual.year == expected.year:
        if actual.month == expected.month:
            result = 15 * (actual.day - expected.day)
        else:
            result = 500 * (actual.month - expected.month)
    else:
        result = 10000
print(result)
