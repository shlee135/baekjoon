# 10813
N, M = map(int, input().split())
asdf = [0] * N
for i in range(N):
    asdf[i] = i + 1
for _ in range(M):
    i, j = map(int, input().split())
    temp = asdf[i - 1]
    asdf[i - 1] = asdf[j - 1]
    asdf[j - 1] = temp
for i in asdf:
    print(i, end = " ")