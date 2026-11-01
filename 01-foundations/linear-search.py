# Time Complexity: O(n)
# Space Complexity: O(1)

students = [12, 38, 2, 21, 24, 55]
found = False
comparisons = 0

target = int(input("Enter Student's Role Number : "))

for student in students:
    if student == target:
        found = True
        break
    comparisons += 1

if found:
    print("Student Found!")
else:
    print("Student Not Found.")

print("Number of Comparisons : ", comparisons)