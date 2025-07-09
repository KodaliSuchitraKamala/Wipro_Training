# Calculator using Parse
import argparse 
parser = argparse.ArgumentParser(description = "Simple Calculator")
parser.add_argument('--x', type = int, required = True, help = "First number")
parser.add_argument('--y', type = int, required = True, help = "Second number")
parser.add_argument('--opt', type = str, required = True, choices = ['add', 'subtract', 'product', 'division'], help = "Operation")
args = parser.parse_args()
if args.opt == 'add':
    result = args.x + args.y
elif args.opt == 'subtract':
    result = args.x - args.y
elif args.opt == 'product':
    result = args.x * args.y
elif args.opt == 'division':
    result = args.x / args.y
print("Result is: ", result)