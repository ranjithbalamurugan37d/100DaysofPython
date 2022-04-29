age = input("What is your age ?")

WEEKS_IN_YEAR =52
DAYS_IN_YEAR = 365
MONTHS_IN_YEAR = 12

years_remaining = 90 - int(age)
months_remaining = years_remaining *MONTHS_IN_YEAR 
days_remaining = years_remaining * DAYS_IN_YEAR
weeks_remaining = years_remaining * WEEKS_IN_YEAR


print(f"you have {days_remaining} days {months_remaining} months {weeks_remaining} weeks left.")