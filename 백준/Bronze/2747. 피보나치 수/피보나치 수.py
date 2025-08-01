# 2747
# 첫째 줄에 n이 주어진다. n은 45보다 작거나 같은 자연수이다.
# 첫째 줄에 n번째 피보나치 수를 출력한다.

def f(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    if n < 2 :
        return dp[n]
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp [i - 1]
    return dp[n]
n = int(input())
print(f(n))