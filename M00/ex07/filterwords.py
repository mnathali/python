import sys

assert len(sys.argv) == 3, "ERROR"
assert sys.argv[2].isdigit(), "ERROR"

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

s = sys.argv[1].split()
result = []

for x in s:
    x = x.strip(punctuations)
    if len(x) > int(sys.argv[2]):
        result.append(x)

print(result)
