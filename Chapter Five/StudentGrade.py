grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

for i in range(5):
    name = input("Enter student name: ")
    grade = input("Enter student letter grade (A, B, C, or D): ")
    grades[grade.upper()] += 1

print("\nNumber of students who received each grade:")
for grade, count in grades.items():
    print("{}: {}".format(grade, count))
