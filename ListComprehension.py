"""
[expression for any item in iteration / with a condition]
code to take user input of random 10 numbers using list comprehension and print them
constraint: take input with space seperated
input must read 10 numbers if the user give more than 10 numbers space separated 

n = [int(x) for x in input("Enter 10 space separated numbers: ").split()[:5]]
print(n)

List Comprehension

colors = ['red', 'green', 'blue', 'violet']
print([color.upper() for color in colors])
print([x for x in range(11)])
print([x for x in range(11) if x % 2 == 0])
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(m[2][1])
m = [[1, 2, 3], [4, 5, [11, 22]], [7, 8, 9]]
print(m[1][2][0])


code to take user input with space seperated and convert the 9 inputs in to 
3x3 martix form on display uisng list comprehension

n = [int(x) for x in input("Enter 9 inputs numbers: ").split()[:9]]
m = [[n[i * 3 + j] for j in range(3)] for i in range(3)]
print("3x3 matrix")
for x in m:
    print(x)


code to convert decimal to binary matrix by considering even and odd manipulations for user
defined variables of an nxn matrix 
where n = 3
list = [[1, 2, 3], [3, 3, 3], [4, 5, 6]]
output:
1 0 1
1 1 1
0 1 0
"""
n = input("Enter 9 numbers: ").split()
num = [int(x) for x in n]
m = [[num[i * 3 + j] for j in range(3)] for i in range(3)]
bm = [[0 if m[i][j] % 2 == 0 else 1 for j in range(3)] for i in range(3)]
for r in m:
    print(r)
for r in bm:
    print(r)
