age = input('Enter your age: ')
defaultLifeInYears = 90
defaultMonths = 12
defaultWeeks = 52
defaultDays = 365
ageInInt = int(age)
remainingLifeInYears = defaultLifeInYears - ageInInt
remainingLifeInMonths = remainingLifeInYears * defaultMonths
remainingLifeInWeeks = remainingLifeInYears * defaultWeeks
remainingLifeInDays = remainingLifeInYears * defaultDays
message = f'You have {remainingLifeInYears} years, {remainingLifeInMonths} months, {remainingLifeInWeeks} weeks and {remainingLifeInDays} days left.'
print(message)
