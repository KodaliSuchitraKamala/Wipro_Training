c = int(input("Enter temperature in c: "))
f = (c * 9 / 5) + 32
assert(f <= 32), "It's Cold"
print("Fahrenheit: ", f)