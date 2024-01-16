import datetime
import math


class newStudent():
    def __init__(self, student_id, first_name, middle_name, last_name, grades, average_grade):
        self.__student_id = student_id
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__grades = grades
        self.__average_grade = average_grade

    def print_details(self):
        print(
            f"Student ID: {self.__student_id}, First Name: {self.__first_name}, Middle Name : {self.__middle_name}, Last Name: {self.__last_name}, Grades: {self.__grades}, Average Grade: {self.__average_grade}")

    def return_average_grade(self):
        return self.__average_grade

    def return_name(self):
        return f"{self.__first_name}, {self.__middle_name}, {self.__last_name}"


def create_a_classroom(file_name):
    students_list = []
    with open(file_name, "r", encoding="utf-8") as reader:
        lines = reader.readlines()
        for line in lines:
            words = line.split(" ")
            id = int(words[0])
            first_name = words[1]
            middle_name = words[2]
            last_name = words[3]
            grades = []
            for grade in range(4, len(words)):
                grades.append(float(words[grade]))

            average_grade = 0

            for grade in grades:
                average_grade = average_grade + grade
            average_grade = average_grade / len(grades)

            students_list.append(newStudent(id, first_name, middle_name, last_name, grades, average_grade))

        # for student in students_list:
        #     print(student.print_details())
        with open("results.txt", "w", encoding="utf-8") as writer:
            # first part
            writer.write("Students with A: ")
            for student in students_list:
                if student.return_average_grade() >= 5.50:
                    writer.write(f"\n {student.return_name()} -> {student.return_average_grade():.2f}")

            # second part
            count_of_C = 0
            for student in students_list:
                if 3.50 <= student.return_average_grade() < 4.50:
                    count_of_C += 1
            writer.write(f"\nCount of students with C : {count_of_C}")

            # third part

            average_grade = 0.0
            for student in students_list:
                average_grade += student.return_average_grade()
                average_grade = average_grade / len(students_list)

            writer.write(f"\nAverage grade {average_grade: .2f}")

            # forth part
            if average_grade < 4.50:
                writer.write("\nThe exam was hard!")
            if average_grade > 4.50:
                writer.write("\nThe exam was easy!")

            writer.write("\n")
            date = datetime.datetime.now()
            writer.write(f"\n{date.day}/{date.month}/{date.year} (day/month/year); {date.hour}:{date.minute}")


file_name = "9a_class.txt"
create_a_classroom(file_name)
