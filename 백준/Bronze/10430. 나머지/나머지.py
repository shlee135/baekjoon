# 10430
# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

A, B, C = map(int, input().split())
print("%d\n%d\n%d\n%d\n"%((A+B)%C,((A%C) + (B%C))%C,(A*B)%C,((A%C) * (B%C))%C))