"""
ps:
data = [10, 'hi', 4.5, 'students', 3, 100]
from rhe list containing numbers and strings, extract only integers using lambda function and list comprehension
o/p: [10, 3, 100]

data = [10, 'hi', 4.5, 'students', 3, 100]
x = list(filter(lambda x: isinstance(x, int), data))
print(x)
i = [x for x in data if(lambda v: type(v) == int)(x)]
print(i)

Calculate the factorial of n using recursion of lambda function.
n = 4

n = int(input("Enter the number: "))
i = lambda fact: 1 if fact == 0 else fact * i(fact - 1)
print(f"Factorial of {n} is: {i(n)}")
fact = (lambda f : lambda n: 1 if n == 0 else n * f(f)(n - 1))(lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))
print(f"Factorial of {n} is: {fact(n)}")

sum of digits : 3426
o/p: 15

dsum = (lambda f: lambda n: 0 if n == 0 else n % 10 + f(f)(n // 10))(lambda f: lambda n: 0 if n == 0 else n % 10 + f(f)(n // 10))
print(dsum(3426))

Basic Lambda function
=======================================
pvar = lambda v1, v2 ...... : operatioon / condition / boolean expression

x = lambda num: num + 22
print(x(11))

add = lambda num1, num2: num1 + num2
print(add(11, 22))

big = lambda x, y: x if x > y else y
print(big(5, 2))

nums = [11, 22, 33, 44, 55, 77, 99]
e = list(filter(lambda num: num % 2 == 0, nums))
print(e)

nums = [11, 22, 33, 44, 55, 77, 99]
e = list(filter(lambda num: num % 2 != 0, nums))
print(e)

filter selects the values from the list based on the condition
map evaluvates the value in the condition to produce the boolean values

nums = [11, 22, 33, 44, 55, 77, 99]
e = list(map(lambda num: num % 2 != 0, nums))
print(e)

sort generalized data
sorted module evaluvation

packs = [(11, 99), (2, 11), (66, 66)]
result = sorted(packs, key = lambda x: x[1])
print(result)

def b(n):
    return lambda x: x * n 
a = b(2)
print(a(5))

def a(n):
    return n ** 3
b = lambda x: x ** 3
print(a(2))
print(b(2))

code to declare the longest string using lambda

long = lambda a, b: a if len(a) > len(b) else b
print(long("Suchitra", "Kamala"))
print(long("1234", "12"))

List Comprehension With Lambda Function
============================================
data = ['pen', 'cap', 'bat']
upper = [(lambda x: x.upper())(d) for d in data]
print(upper)

word = 'Suchitra'
o/p = 'artihcuS'

word = 'Suchitra'
reverse = " ".join(map(lambda w: w[::-1], word.split()))
print(reverse)

words = ['Kodali', 'Suchitra', 'Kamala']
rw = [(lambda w: w[::-1])(word) for word in words]
print(rw)

['hi', ' ', 'students', ' ', 'bye']

s = ['hi', ' ', 'students', ' ', 'bye']
i = [x for x in s if(lambda v: v != " ")(x)]
print(i)

Nested 
Recursive

(a + b) * c expression lambda evaluate and returns to another lambda

l2 = lambda a: lambda b, c: (a + b) * c  # l2 -> return b c 
num1 = int(input("Enter value of a: "))
num2 = int(input("Enter value of b: "))
num3 = int(input("Enter value of c: "))
l1 = l2(num1) 
value = l1(num2, num3)
print(value)

print((lambda a: lambda b, c: (a + b) * c)(5)(3,2))
# l2(5)
# l1(3, 2)

(a + b) * (c + d)

print((lambda a: lambda b: lambda c, d: (a + b) * (c + d))(2)(3)(4, 5))

(a - b) / (c - d)

print((lambda a: lambda b: lambda c, d: (a - b) / (c - d))(2)(3)(4, 5))

assign = op(num)
print(assign(numsq))

print((lambda a: lambda b: (a + b) ** 2)(int(input("a: ")))(int(input("b: "))))

print((lambda a: lambda b: (a + b) ** 3)(int(input("a: ")))(int(input("b: "))))

(a - b) / (c - d) expression with different modulations.

try:
    print((lambda a: lambda b: lambda c, d: (a - b) / (c - d))(10)(4)(8, 6))
except ZeroDivisionError:
    print("Division by Zero error!!!")
except TypeError:
    print("Invalid Data Type!!!")

try:
    print((lambda a: lambda b: lambda c, d: (a - b) / (c - d))(10)(4)(8, 8))
except ZeroDivisionError:
    print("Division by Zero error!!!")
except TypeError:
    print("Invalid Data Type!!!")

try:
    print((lambda a: lambda b: lambda c, d: (a - b) / (c - d))("10")(4)(8, 8))
except ZeroDivisionError:
    print("Division by Zero error!!!")
except TypeError:
    print("Invalid Data Type!!!")

simple nested lambda string combining with sperator operation for n attributes

print((lambda a: lambda b: lambda c, d: a + '-' + b + '-' + c + '-' + d)(input("a: "))(input("b: "))(input("c: "), input("d: ")))

given attributes a, b, c, d are hi, !, Students,!!!
write a nested lambda to concatnate the abcd, by converting a and c to uppercase
output: HI!STUDENTS!!!

print((lambda a: lambda b: lambda c, d: a.upper()+  b + c.upper() + d)(input("a: "))(input("b: "))(input("c: "), input("d: ")))

given attributes a, b, c, d are hi, hello, Students, teachers
write a nested lambda to concatnate the abcd, by reversing with sep ' '
output: ih olleh stnedutS srehcaet

print((lambda a: lambda b: lambda c, d: a[::-1] + ' ' + b[::-1] + ' ' + c[::-1] + ' ' + d[::-1])('hi')('hello')('Students', 'teachers'))

given attributes a, b, c, d are hi, hello, Students, teachers
write a nested lambda to concatnate the abcd, by reversing and do list comprehension on the reversed attributes
output: ['ih', 'olleh', 'stnedutS', 'srehcaet']

print((lambda a: lambda b: lambda c, d: [a[::-1], b[::-1], c[::-1], d[::-1]])('hi')('hello')('Students', 'teachers'))

num = [4, 6, 3, 8]
clist = [12, 12, 9, 16]
lambda : lambda if: 

num = [4, 6, 3, 8]
print((lambda a: [(x * 3 if x < 5 else x * 2) for x in a])(num))
"""
numbers =(lambda x: lambda a: a * 2 if a > x else a * 3)
above_5 = numbers(5)
num = [4, 6, 3, 8]
o = list(map(above_5, num))
print(o)