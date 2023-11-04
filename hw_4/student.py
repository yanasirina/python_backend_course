from typing import Union, Iterable
from user import User
from teacher import Teacher


class StudentException(Exception):
    pass


class Student(User):
    def __init__(self, teacher: Teacher, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._grades = []
        self._teacher = teacher
        teacher.add_student(self)

    def __str__(self):
        str_parent = super().__str__()
        return f'{str_parent} (студент)'

    def __lt__(self, other: Union[int, float, 'Student']):
        other_grade = Student._get_other_average_garde(other)
        return self._get_average_grade() < other_grade

    def __gt__(self, other: Union[int, float, 'Student']):
        other_grade = Student._get_other_average_garde(other)
        return self._get_average_grade() > other_grade

    def __le__(self, other: Union[int, float, 'Student']):
        other_grade = Student._get_other_average_garde(other)
        return self._get_average_grade() <= other_grade

    def __ge__(self, other: Union[int, float, 'Student']):
        other_grade = Student._get_other_average_garde(other)
        return self._get_average_grade() >= other_grade

    def add_grades(self, grades: Iterable[int]):
        if not all([1 <= grade <= 5 for grade in grades]):
            raise StudentException('Оценки должны быть в диапазоне от 1 до 5')
        self._grades.extend(grades)

    def get_grades(self):
        return self._grades

    def _get_average_grade(self):
        try:
            average_garde = sum(self._grades) / len(self._grades)
        except ZeroDivisionError:
            average_garde = 0
        return average_garde

    @staticmethod
    def _get_other_average_garde(other: Union[int, float, 'Student']):
        if not isinstance(other, (int, Student)):
            raise TypeError("Сравнение Student возможно только со Student или int")
        other_average_grade = other if type(other) in [int, float] else other._get_average_grade()
        return other_average_grade
