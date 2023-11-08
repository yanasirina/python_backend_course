from student import Student, StudentException
from teacher import Teacher


if __name__ == '__main__':
    main_teacher = Teacher(username='main_teacher', password='123')
    first_student = Student(username='ivan', password='VaNyA', teacher=main_teacher)
    second_student = Student(username='petr', password='PeTyA', teacher=main_teacher)
    print(main_teacher, first_student, second_student, sep=', ')    # Пользователь: main_teacher (учитель), Пользователь: ivan (студент), Пользователь: petr (студент)

    # попробуем залогиниться с верным и неверным паролем
    print(first_student('VaNyA'))    # Доступ разрешен
    print(first_student('Ne VaNyA'))    # Доступ запрещен

    # посмотрим текущих студентов учителя
    print([str(student) for student in main_teacher.get_students()])    # ['Пользователь: ivan (студент)', 'Пользователь: petr (студент)']

    # добавим нового учителя и студента, посмотрим студентов у обоих учителей после этого
    another_teacher = Teacher(username='another_teacher', password='123')
    third_student = Student(username='maria', password='some_password', teacher=another_teacher)
    print([str(student) for student in main_teacher.get_students()])    # ['Пользователь: ivan (студент)', 'Пользователь: petr (студент)']
    print([str(student) for student in another_teacher.get_students()])    # ['Пользователь: maria (студент)']

    # добавим оценки студентам
    first_student.add_grades([2, 1, 3, 5, 4, 3, 2])
    second_student.add_grades([5, 5, 4, 4, 5])
    third_student.add_grades([5, 3, 5, 3, 4, 4])

    # проверим, что оценки добавились
    print(first_student.get_grades())    # [2, 1, 3, 5, 4, 3, 2]
    print(second_student.get_grades())    # [5, 5, 4, 4, 5]
    print(third_student.get_grades())    # [5, 3, 5, 3, 4, 4]

    # попробуем добавить некорректные оценки
    try:
        third_student.add_grades([0, 18, 4])
    except StudentException as ex:
        print(ex)  # Оценки должны быть в диапазоне от 1 до 5

    # найдем лучшего и худшего студента
    print(max(first_student, second_student, third_student))    # Пользователь: petr (студент)
    print(min(first_student, second_student, third_student))    # Пользователь: ivan (студент)

    # добавим студента без оценок, убедимся, что он будет в конце рейтинга
    fourth_student = Student(username='yana', password='pass123', teacher=main_teacher)
    students = [first_student, second_student, third_student, fourth_student]
    sorted_students = sorted(students, reverse=True)
    print([str(student) for student in sorted_students])    # ['Пользователь: petr (студент)', 'Пользователь: maria (студент)', 'Пользователь: ivan (студент)', 'Пользователь: yana (студент)']
