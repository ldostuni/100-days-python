student_scores = {
    "Gock" : 23,
    "Blorter" : 78,
    "Galactor" : 69,
    "Droidus" : 99,
    "Qwerto" : 85,
}

student_grades = {}

for key in student_scores:
    grade = ""
    score = student_scores[key]
    if score >= 91:
        grade = "Outstanding"
    elif score >= 81:
        grade = "Exceeds Expectations"
    elif score >= 71:
        grade = "Acceptable"
    elif score < 71:
        grade = "Fail"
    student_grades[key] = grade

print(student_grades)

