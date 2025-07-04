try:
    num = int(input("Enter number: "))
    print(num * 4)
except KeyboardInterrupt:
    print("Number Should be entered")
except ValueError:
    print("Please check before you enter the data type")
print("Bye")