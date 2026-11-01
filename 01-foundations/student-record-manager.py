students = [12, 38, 2, 21, 24, 55]
found = False

target = int(input("Enter Student's Role Number : "))

for student in students:
    if student == target:
        found = True
        break 

if found:
    print("Student Found!")
else:
    print("Student Not Found.")