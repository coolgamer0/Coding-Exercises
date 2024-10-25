days_in_month = {
    1: 31,   # January
    2: 28,   # February (not accounting for leap years)
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

month_number = int(input("Please enter the month number (1-12): "))
if month_number in days_in_month:
    print(f"There are {days_in_month[month_number]} days in month {month_number}.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
