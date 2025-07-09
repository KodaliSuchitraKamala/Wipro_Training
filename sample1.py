import sys
print("Script name: ", sys.argv[0])
print("All args: ", sys.argv[1:])
print("Number of items: ", len(sys.argv))
print("Including file name: ", sys.argv)
if len(sys.argv) > 1:
    print("First argv: ", sys.argv[1])
else:
    print("No agruments provided")