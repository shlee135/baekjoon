# 8393
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
# 1부터 n까지 합을 출력한다.

result = 0
n = int(input())
for i in range(1, n+1):
    result += i
print(result)