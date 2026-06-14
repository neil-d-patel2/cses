import sys

arrLen = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

out = 0

for x in range(1,arrLen):
    if arr[x] < arr[x-1]:
        out += arr[x-1] - arr[x]
        arr[x] = arr[x-1]

print(out)
