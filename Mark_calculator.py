# Marks Calculator - CSE AI ML Project by Akshaya KP
def calculate_grade():
    print("=== Student Marks Calculator ===")
    name = input("Enter student name: ")
    marks = []
    for i in range(5):
        m = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)
    
    total = sum(marks)
    avg = total / 5
    
    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "F"
    
    print(f"\nName: {name}")
    print(f"Total: {total}/500")
    print(f"Average: {avg}%")
    print(f"Grade: {grade}")

calculate_grade()
