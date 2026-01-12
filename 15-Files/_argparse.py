import argparse

print('hello world')

parser = argparse.ArgumentParser(description="Calculator")

parser.add_argument("num1", type=float, help="First Number")
parser.add_argument("num2", type=float, help="Second Number")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to be performed")

args = parser.parse_args()
# print(args)

if(args.operation == "add"):
    print(f"The result is {args.num1 + args.num2}")

elif(args.operation == "sub"):
    print(f"The result is {args.num1 - args.num2}")

elif(args.operation == "mul"):
    print(f"The result is {args.num1 * args.num2}")

elif(args.operation == "div"):
    print(f"The result is {args.num1 / args.num2}")

else:
    print("some error occured !")   