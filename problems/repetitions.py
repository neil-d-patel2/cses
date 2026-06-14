import sys



input = sys.stdin.readline()


s = set()
out = 0
curLen = 0

for _ in input:
    if _ in s:
        curLen += 1
    else:
        curLen = 1
        s.clear()
        s.add(_)

    if curLen > out:
        out = curLen

print(out)


