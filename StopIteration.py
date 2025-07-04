''' Write a program which infinitly prints natural numbers. 
Raise a StopIteration exception after displaying first 20 numbers to exceed the program
'''
def display(n):
    while True:
        try:
            n += 1
            if n == 21:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n, end = ' ')
i = 0
display(i)