import itertools
data = input("Enter Characters: ")
permute = list(itertools.permutations(data))
print("All permutations")
for p in permute:
    print(" ".join(p))