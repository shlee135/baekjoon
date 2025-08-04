# 3052
# 42로 나눈 나머지의 종류 개수 구하기
div_42 = [-1] * 10
j = 0
for _ in range(10):
    remainder = int(input())%42
    for i in range(10):
        if div_42[i] == remainder:
            is_remainder = True
            break
        is_remainder = False
    if not is_remainder:
        div_42[j] = remainder
        j += 1
while True:
    try:
        div_42.remove(-1)
    except:
        break
print(len(div_42))