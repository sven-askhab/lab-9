#!usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    school = {
        "1а": 23,
        "1б": 34,
        "1в": 32,
        "2а": 16,
        "2б": 51,
        "2в": 7,
        "3а": 37,
        "3б": 14,
        "3в": 24
    }

    class_name = input("Введите класс: ")
    stud_amount = int(input("Введите количество учеников: "))
    school[class_name] = stud_amount

    new_class = input("Введите название нового класса: ")
    new_class_stud = int(input("Введите количество учеников: "))
    school.setdefault(
        new_class,
        new_class_stud
    )

    delete_class = input(
        "Введите класс, который необходимо удалить: "
    )

    del school[delete_class]
    print(school)
    print("Общее количество учеников:", sum(school.values()))