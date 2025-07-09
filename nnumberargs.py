import sys
if len(sys.argv) < 2:
    print("Usage: python nnumberarge.py n1, n2, ......")
    sys.exit()
numbers = [int(arg) for arg in sys.argv[1:]]
total = sum(numbers)
print("Numbers: ", numbers)
print("Sum: ", total)