# 15552
# sys.stdin.readline
# .rstrip()
import sys

T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)