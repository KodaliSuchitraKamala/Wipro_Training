try:
    num = int(input("Enter number: "))
    print(num * 4)
except (KeyboardInterrupt, ValueError, TypeError):
    print("Number Should be entered......Program Terminated!!!")
print("Bye")