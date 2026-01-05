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
        return (f"Имя: {self.name}"
                f"Фамилия: {self.surname}"
                f"Средняя оценка за домашние задания: {self.average_grades}"
                f"Курсы в процессе изучения: {self.courses_in_progress}"
                f"Завершенные курсы:{self.finished_courses}"
                )

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
        self.grades ={}

    def average_grades(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        if not all_grades:
            return None
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        average_grades = self.average_grades
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades}'

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