class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        if not all_grades:
            return None
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grades()}\n"
                f"Курсы в процессе изучения: {self.courses_in_progress}\n"
                f"Завершенные курсы: {self.finished_courses}\n")

    def __eq__(self, other):
        return self.average_grades() == other.average_grades()

    def __gt__(self, other):
        return self.average_grades() > other.average_grades()

    def __lt__(self, other):
        return self.average_grades() < other.average_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        if not all_grades:
            return None
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grades()}')

    def __eq__(self, other):
        return self.average_grades() == other.average_grades()

    def __gt__(self, other):
        return self.average_grades() > other.average_grades()

    def __lt__(self, other):
        return self.average_grades() < other.average_grades()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def students_average_grades(students, course):
    students_grades = []
    for student in students:
        grade = student.grades.get(course)
        if grade:
            students_grades += grade
    if students_grades:
        return round(sum(students_grades) / len(students_grades), 1)
    else:
        return None


def lecturers_average_grades(lecturers, course):
    lecturers_grades = []
    for lecturer in lecturers:
        grade = lecturer.grades.get(course)
        if grade:
            lecturers_grades += grade
    if lecturers_grades:
        return round(sum(lecturers_grades) / len(lecturers_grades), 1)
    else:
        return None


student1 = Student('Петр', 'Ефремов', 'Мужской')
student2 = Student('Екатерина', 'Соколова', 'Женский')

lecturer1 = Lecturer('Сергей', 'Семечков')
lecturer2 = Lecturer('Елена', 'Котик')

reviewer1 = Reviewer('Алексей', 'Егоров')
reviewer2 = Reviewer('Ольга', 'Иванова')


student1.courses_in_progress.append('Python')
student2.courses_in_progress.append('Java')


lecturer1.courses_attached.append('Python')
lecturer2.courses_attached.append('Java')

reviewer1.courses_attached.append('Python')
reviewer2.courses_attached.append('Java')


student1.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer2, 'Java', 8)

reviewer1.rate_hw(student1, 'Python', 7)
reviewer2.rate_hw(student2, 'Java', 6)


print(f'Средняя оценка Петра Ефремова: {student1.average_grades()}')
print(f'Средняя оценка Екатерины Соколовой: {student2.average_grades()}')

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)