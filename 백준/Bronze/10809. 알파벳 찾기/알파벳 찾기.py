# 10809
S = list(input())
for alphabet in range(26):
    is_inlist = False
    place = 0
    for value in S:
        if value == chr(alphabet+97):
            print(place, end = " ")
            is_inlist = True
            break
        else:
            place += 1
    if not is_inlist:
        print(-1, end = " ")