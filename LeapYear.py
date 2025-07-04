from calendar import *
year = int(input("Enter a year number: "))
if isleap(year):
    print(year, " is leap year")
else:
    print(year, " is not a leap year")