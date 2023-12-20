import datetime


def check_grades(file_name):
    with open(file_name, "r", encoding="utf-8") as reader:
        lines = reader.readlines()
        students_grade = {}
        for line in lines:
            student = ""
            grade = ""
            check = False
            for char in line:
                if char.isalpha():
                    check = True
                if check:
                    if char.isnumeric() or char == ".":
                        grade += char
                    else:
                        student += char

            students_grade[student] = float(grade)

    for student in students_grade.keys():
        for char in student:
            if char == "\n":
                student.replace(char, "")

    with open("results.txt", "w", encoding="utf-8") as writer:
        # first part
        writer.write("Students with A: ")
        for student, grade in students_grade.items():
            if grade >= 5.50:
                writer.write(f"\n {student} -> {grade:.2f}")

        # second part
        count_of_C = 0
        for grade in students_grade.values():
            if grade >= 3.50 or grade < 4.50:
                count_of_C += 1
        writer.write(f"\nCount of students with C : {count_of_C}")

        # third part

        average_grade = 0.0
        for grade in students_grade.values():
            average_grade += grade
            average_grade = average_grade / len(students_grade)

        writer.write(f"\nAverage grade {average_grade: .2f}")

        # forth part
        if average_grade < 4.50:
            writer.write("\nThe exam was hard!")
        if average_grade > 4.50:
            writer.write("\nThe exam was easy!")

        writer.write("\n")
        date = datetime.datetime.now()
        writer.write(f"\n{date.day}/{date.month}/{date.year} (day/month/year); {date.hour}:{date.minute}")


name = "9a_class.txt"
check_grades(name)
