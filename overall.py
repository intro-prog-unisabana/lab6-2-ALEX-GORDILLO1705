def student_averages(students):
    result = {}

    for student, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        result[student] = round(avg)

    return result


def assignment_averages(students):
    result = {}
    assignments = {}

    for grades in students.values():
        for assignment, grade in grades.items():
            if assignment not in assignments:
                assignments[assignment] = []
            assignments[assignment].append(grade)

    for assignment, grades in assignments.items():
        avg = sum(grades) / len(grades)
        result[assignment] = round(avg)

    return result