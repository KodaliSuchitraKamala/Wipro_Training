import sys
if len(sys.argv) != 3:
    print("Usage: python sample.py 1 b")
else:
    l = float(sys.argv[1])
    b = float(sys.argv[2])
    print("Calculated area: ", l * b)