# 10871
N, X = map(int, input().split())
asdf = list(map(int, input().split()))
asdff = []
for i in range(N):
    if asdf[i] < X:
        print(asdf[i], end = " ")