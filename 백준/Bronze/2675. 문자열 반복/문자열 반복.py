# 2675
T = int(input())
for _ in range(T):
    S = list(input())
    j = int(S[0])
    n = len(S)
    for i in range(2, n):
        for _ in range(j):
            print(f"{S[i]}", end = "")
    print()