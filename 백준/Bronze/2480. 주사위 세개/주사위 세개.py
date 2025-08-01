# 2480
# 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
# 첫째 줄에 게임의 상금을 출력 한다.

d1, d2, d3 = map(int,input().split())
if d1 == d2 == d3:
    reward = 10000+(d1)*1000
elif d1 == d2 or d2 == d3 or d3 == d1:
    if d1 == d2:
        reward = 1000 + (d1)*100
    elif d2 == d3:
        reward = 1000 + (d2)*100
    else :
        reward = 1000 + (d3)*100
else :
    if d1 >= d2 and d1 >= d3:
        reward = d1*100
    elif d2 >= d1 and d2 >= d3:
        reward = d2*100
    else :
        reward = d3*100
print(reward)