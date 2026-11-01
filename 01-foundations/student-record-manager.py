students = [12, 38, 2, 21, 24, 55]
found = False

for student in students:
    if student == 100:
        found = True

if found:
    print("Student Found!")
else:
    print("Student Not Found.")