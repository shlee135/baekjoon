# 5597
students = [i for i in range (1, 31)]

for i in range (28):
    attendance = int(input())
    students.remove(attendance)

print(min(students))
print(max(students))