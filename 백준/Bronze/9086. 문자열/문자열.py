# 9086
T = int(input())
for i in range(T):
    word = list(input())
    length = len(word)
    print(f"{word[0]}{word[length - 1]}")