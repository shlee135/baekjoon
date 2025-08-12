# 5622
list_dial = list(input())
time = 0
for dial in list_dial:
    if dial == "A" or dial == "B" or dial == "C":
        time += 3
    elif dial == "D" or dial == "E" or dial == "F":
        time += 4
    elif dial == "G" or dial == "H" or dial == "I":
        time += 5
    elif dial == "J" or dial == "K" or dial == "L":
        time += 6
    elif dial == "M" or dial == "N" or dial == "O":
        time += 7
    elif dial == "P" or dial == "Q" or dial == "R" or dial == "S":
        time += 8
    elif dial == "T" or dial == "U" or dial == "V":
        time += 9
    elif dial == "W" or dial == "X" or dial == "Y" or dial == "Z":
        time += 10
    else:
        time += 2
print(time)