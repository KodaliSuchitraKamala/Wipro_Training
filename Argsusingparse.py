# Arguments using Parse
import argparse 
parser = argparse.ArgumentParser(description = "Add 2 Numbers")
parser.add_argument('--x', type = int, required = True, help = "First number")
parser.add_argument('--y', type = int, required = True, help = "Second number")
args = parser.parse_args()
result = args.x + args.y
print("Sum is: ", result)