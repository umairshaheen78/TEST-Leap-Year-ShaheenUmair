# Prompt the user to input a year
year=int(input('Please enter a random year:'))

# Using if statements, output whether the inputted year is or is not a leap year
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")