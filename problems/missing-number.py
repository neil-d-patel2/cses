import sys


n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

num_set = set(range(1, n + 1))


for x in numbers:
    num_set.remove(x)


print(num_set.pop())



