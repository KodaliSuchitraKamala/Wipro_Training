"""
Write a Program to create a text filr access the text file data and use the
data to split the lines into series of words and use space to perform
split operation
sample.txt
Hello students
How are you today
Output
['Hello', 'students', 'how', 'are', 'you', 'today']
"""
with open('sample.txt', 'w') as file:
    file.write('Hello students\n')
    file.write('How are you today')
words = []
with open('sample.txt', 'r') as file:
    for line in file:
        words.extend(line.strip().split())
print([word.lower() for word in words])  