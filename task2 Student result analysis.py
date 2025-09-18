import numpy as np

Student_data = {
    "st-1": {"Maths": 85, "Urdu": 70, "Sindhi": 40, "Chemistry": 90, "Physics": 60},
    "st-2": {"Maths": 70, "Urdu": 75, "Sindhi": 40, "Chemistry": 90, "Physics": 60},
    "st-3": {"Maths": 80, "Urdu": 70, "Sindhi": 95, "Chemistry": 90, "Physics": 60},
    "st-4": {"Maths": 80, "Urdu": 70, "Sindhi": 50, "Chemistry": 85, "Physics": 60},
    "st-5": {"Maths": 80, "Urdu": 75, "Sindhi": 40, "Chemistry": 90, "Physics": 60},
}

students = list(Student_data.keys())

subjects = list(next(iter(Student_data.values())).keys())

print("Students:", students)
print("Subjects:", subjects)

data_matrix = np.array([[Student_data[st][sub] for sub in subjects] for st in students])

print("\nData Matrix:\n", data_matrix)

for i in range(len(subjects)):
    subject = subjects[i]
    marks = data_matrix[:, i]

    max_marks = max(marks)
    min_marks = min(marks)

    for j in range(len(students)):
        if marks[j] == max_marks:
            max_student = students[j]
        if marks[j] == min_marks:
            min_student = students[j]

    print(f"\nSubject: {subject}")
    print("  Max:", max_marks, "Student:", max_student)
    print("  Min:", min_marks, "Student:", min_student)
