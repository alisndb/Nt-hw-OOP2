from statistics import mean
from itertools import chain


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in \
                self.courses_in_progress and grade in [i for i in range(11)]:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка, проверьте указанные данные'

    def __get_gpa(self):
        return mean(chain(*self.grades.values()))

    def __str__(self):
        return f'Имя: {self.name}\n'\
                f'Фамилия: {self.surname}\n'\
                f'Средняя оценка за домашние задания: {self.__get_gpa():.2f}\n'\
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'\
                f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __le__(self, student):
        if isinstance(student, Student):
            return self.__get_gpa() <= student.__get_gpa()
        else:
            return 'Ошибка, проверьте указанные данные'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __get_gpa(self):
        return mean(chain(*self.grades.values()))

    def __str__(self):
        return f'Имя: {self.name}\n'\
                f'Фамилия: {self.surname}\n'\
                f'Средняя оценка за лекции: {self.__get_gpa():.2f}'

    def __le__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.__get_gpa() <= lecturer.__get_gpa()
        else:
            return 'Ошибка, проверьте указанные данные'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка, проверьте указанные данные'

    def __str__(self):
        return f'Имя: {self.name}\n'\
                f'Фамилия: {self.surname}'


def get_mult_gpa(objects_list, course):
    print(f'Средняя оценка: {mean(chain(*[obj.grades[course] for obj in objects_list]))}')


# Демонстрация работы программы:
reviewer_1 = Reviewer('Sergey', 'Antonov')
reviewer_1.courses_attached += ['Python']

student_1 = Student('Andrey', 'Onegin')
student_2 = Student('Gleb', 'Tkachev')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['С++']
student_2.courses_in_progress += ['Python']

lecturer_1 = Lecturer('Vlad', 'Orlov')
lecturer_2 = Lecturer('Oleg', 'Mihalkov')
lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 92)
reviewer_1.rate_hw(student_2, 'Python', 84)

student_1.rate_lect(lecturer_1, 'Python', 10)
student_2.rate_lect(lecturer_2, 'Python', 9)

print(lecturer_1 >= lecturer_2, lecturer_1 <= lecturer_2, lecturer_1 == lecturer_2)
print(student_1 >= student_2, student_1 <= student_2, student_1 == student_2, '\n')

print(f'{student_1}\n\n{lecturer_1}\n\n{reviewer_1}\n')

students = [student_1, student_2]
lectors = [lecturer_1, lecturer_2]

get_mult_gpa(students, 'Python')
get_mult_gpa(lectors, 'Python')
