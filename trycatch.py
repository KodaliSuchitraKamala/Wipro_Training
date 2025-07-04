num = int(input("Enter the Numerator: "))
den = int(input("Enter the Denominator: "))
try:
    quo = num / den
    print("Quotient: ", quo)
except ZeroDivisionError:
    print("Denominator can't be Zero")