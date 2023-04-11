import sys

assert len(sys.argv) < 3, "more than one argument provided"
if len(sys.argv) != 2:
    quit('')
assert sys.argv[1].isdigit(), "argument is not an integer"
l = int(sys.argv[1])
if l == 0:
    print("I'm Zero.")
elif l % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd")
