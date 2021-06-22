import re


def find_dates(dates):
    date_regex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
    return date_regex.findall(dates)


def validate_dates(dates):
    for date in found_dates:

        def is_leap_year(date):
            leap_year = False
            if int(date[2]) % 400 == 0:
                leap_year = True
            elif int(date[2]) % 100 == 0:
                leap_year = False
            elif int(date[2]) % 4 == 0:
                leap_year = True
            else:
                leap_year = False
            return leap_year

        if date[1] in ['02'] and 0 < int(date[0]) > 28 and is_leap_year(date) == False and 999 < int(date[2]) < 3000:
            print(date[0] + '/' + date[1] + '/' + date[2], "is an invalid date.")

        elif date[1] in ['02'] and 0 < int(date[0]) < 30 and is_leap_year(date) == True and 999 < int(date[2]) < 3000:
            print(date[0] + '/' + date[1] + '/' + date[2], "is a valid date.")

        elif date[1] in ['4', '6', '9', '11'] and 0 < int(date[0]) < 31 and 999 < int(date[2]) < 3000:
            print(date[0] + '/' + date[1] + '/' + date[2], "is a valid date.")

        elif int(date[1]) < 13 and 0 < int(date[0]) < 32 and 999 < int(date[2]) < 3000:
            print(date[0] + '/' + date[1] + '/' + date[2], "is a valid date.")
    return ""


a_string = "Today's date is 22/06/2021. Tomorrow's date is 23/06/2021. A fake date is 31/02/2021. " \
           "This date is in a leap year, 29/02/2024. This date is a leap year, 29/02/2000. " \
           "This is not a leap year, 29/02/2500. This is not in valid format, 22-06-2021."

found_dates = find_dates(a_string)  # Replace a_string to search different text for dates.

print(validate_dates(found_dates))
