# Time Complexity: O(log n)
# Space Complexity: O(1)

students = [3, 7, 11, 15, 19, 23, 27, 31]

target = int(input("Enter roll number: "))

low = 0
high = len(students) - 1

found = False
while (low <= high):
    mid = (low+high)//2
    if(target == students[mid]):
        found = True
        break
    elif(target < students[mid]):
        high = mid - 1
    elif(target > students[mid]):
        low = mid + 1

if found :
    print("Student Found.")
else :
    print("Student not Found.")