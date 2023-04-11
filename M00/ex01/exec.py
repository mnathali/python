import sys

s = ''

for i in range(len(sys.argv)):
    if i == 0:
        continue
    elif i != len(sys.argv) - 1:
        s += sys.argv[i] + ' '
    else:
        s += sys.argv[i]
l = list(s)
l.reverse()
s = ''.join(l).swapcase()
print(s)

# txt = s[::-1]
# print(txt)