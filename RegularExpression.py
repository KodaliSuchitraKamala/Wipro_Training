"""
Regular Expressions
import re
functions
 1. re.findall()
 2. re.match() - 0 - (n - 1)(str1) (0 - (n -1)(str2))
 hello Hello
 3. re.search()
 4. re. sub()
 5. re.compile()
 6. re.split()
 7. re.finditer()

Cases in Regular Expressions:
 1. re.IGNORECASE / re.I
 2. re.MULTILINE / re.M
 3. re.DOTALL / re.D
 4. re.VERBOSE / re.V

metachars-
 1. ^ - start of string
 2. $ - end of " "
 3. * - occurences
 4. + - occurences
 5. ? - combination of *, +
 6. [] - set of characters
 7. () - grouping
 8. \ - escape
 9. . - newline

 syntax - re.match(searchedelements, tex)
code to take a text data and fetch to match the given data 

import re
text = 'hi students how are you!!!'
se = r'how'
output = re.match(se, text)
if output:
    print("Match found for: ", output)
else:
    print("No Match ......")

group, if you have a match in data. group will extract    

import re
text = 'hi students how are you!!!'
se = r'hi'
output = re.match(se, text)
if output:
    print("Match found for: ", output.group())
else:
    print("No Match ......")

import re
text = 'My number is 229'
match = re.search(r'\d+', text)
print(match.group())

import re
text = 'My number is 229'
match = re.search(r'\d+', text)
print(match)

import re
text = input("Enter a sentence with a number: ")
match = re.search(r'\d+', text)
if match:
    print("Number found", match.group())
else:
    print("no match")

import re
text = input("Enter a sentence with a number: ")
matches = list(re.finditer(r'\d+', text))
if len(matches) >= 2:
    print("Second number found ", matches[1].group())
elif len(matches) == 1:
    print("Only one number found ", matches[0].group())
else:
    print("No Match")

import re
text = input("Enter a sentence with a number: ")
matches = list(re.finditer(r'\d+', text))
if len(matches) >= 2:
    print("Third number found ", matches[2].group())
elif len(matches) == 1:
    print("Only one number found ", matches[0].group())
else:
    print("No Match")

import re
text = input("Enter a sentence with a number: ")
n = int(input("Which number you want to extract: "))
matches = list(re.findall(r'\d+', text))
if len(matches) >= n:
    print(f"{n}th number is: ", matches[n - 1])
else:
    print("Not found")

import re
email = input("Enter your email: ")
pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z]{2,}$'
if re.match(pattern, email):
    print("valid")
else:
    print("Not Valid")
"""
import re
phone = input("Enter your number: ")
pattern = r'^[6-9]\d{9}$'
if re.match(pattern, phone):
    print("valid")
else:
    print("Not Valid")