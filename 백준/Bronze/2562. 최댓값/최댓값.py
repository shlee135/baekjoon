# 2562
asdf = []
max_index = 0
for i in range(9):
    asdf.append(int(input()))
for i in range(9):
    if asdf[i] > asdf[max_index]:
        max_index = i
print(asdf[max_index])
print(max_index+1)