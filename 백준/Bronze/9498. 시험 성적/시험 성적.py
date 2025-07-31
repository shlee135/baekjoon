# 9498
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 시험 성적을 출력한다.

score = int(input())

if score >= 90 : result = "A"
elif score >= 80 : result = "B"
elif score >= 70 : result = "C"
elif score >= 60 : result = "D"
else : result = "F"

print(result)