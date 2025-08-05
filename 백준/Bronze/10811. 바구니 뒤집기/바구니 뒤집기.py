# 10811
N, M = map(int, input().split())
basket = []

for ball in range(1, N + 1):
    basket.append(ball)

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]
            
for k in range(N):
    print(basket[k], end = " ")