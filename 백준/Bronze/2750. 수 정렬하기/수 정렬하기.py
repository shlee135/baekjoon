# 2750
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))
for j in range(N - 1):
    for i in range(N - 1 - j):
        if array[i] > array[i + 1]:
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp
for i in range(N):
    print(array[i])