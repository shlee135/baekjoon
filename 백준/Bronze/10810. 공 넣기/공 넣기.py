# 10810
N, M = map(int, input().split())
asdf = [0] * (N)
for _ in range(M):
    i, j, k = map(int, input().split())
    for i in range(i, j+1):
        asdf[i-1] = k
for i in range(N):
    print(asdf[i], end = " ")