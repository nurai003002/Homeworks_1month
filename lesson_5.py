# # Dict -> словарь

# student = {'name': 'Geeks', 'age':2}
# # # print(student)
# # # print(student['age'])
# # print(f"Привет, меня зовут {student['name']}. Мне {student['age']} года")


# student['surname'] = 'OSH' 
# print(student)
# keys = student.keys()
# print(keys)
# items = student.items()
# print(items)
# values = student.values()
# print(values)


# while True:
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     print(f"Результат после сложения: {num1+num2}")
#     print(f"Результат после вычитания: {num1-num2}")
#     print(f"Результат после умножения: {num1*num2}")
#     print(f"Результат после деления: {num1//num2}")
    
# n = 0 
# while True:
#     n += 100
#     print(n)

# count = 0 
# while count <5:
#     print(count)
#     count += 1
    

# д/з
# задание №1
# dictionary_1 = {'a': 300, 'b': 400} 
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

# задание №2
# numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' : 3, 'num_100' : 100} 
# print(numbers['num_1']*5,)
# print(numbers['num_2']*5,)
# print(numbers['num_3']*5,)
# print(numbers['num_100']*5,)

# задание №3
# student = {'name' : 'Askhat', 'age' : 17}
# print(student['age']*2)

# задание №4
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# print(student['age']-1)
# student['color'] = 'black'
# print(student['color'])


# задание №5
# student = {'name' : 'Askhat', 'age' : 17}
# del student['age']
# print(student)

# задание №6
# student = {'name' : 'Askht'}
# address = {'address': 'Западнй Анар'}
# student.update(address)
# print(student)

# задание №7
# students = {
#         1: "Кайрат", 
#         2: "Алексей",
#         3: "Ксения",
#         4: "Адил",
#         5: "Марал",
#         6: "Мерей",
#         7: "Саша",

#     }
# sorted_names = sorted(students.values())

# print("Имена студентов в алфавитном порядке: ")
# for name in sorted_names:
#     print(name)


# задание №8

# students = {
#     "Жаныш": 30,
#     "Нурай": 90,
#     "Сыймык": 89,
#     "Бексултан": 60,
# }

# max_score = max(students.values())
# top_student = [name for name, score in students.items() if score == max_score]

# for student in top_student:
#     print(top_student)
# print(f"Студент с наивысшей оценкой: {top_student} - {max_score} баллов")


#9 задание

# dict1 = {"a": 1, "b":2, "c":3}
# dict2 = {"d": 4, "b":6, "e":9}

# for key, values in dict2.items():
#     if key in dict1:
#         dict1[key] += values
#     else:
#         dict1[key] = values
    
# print("Объединенный словарь", dict1)

# 10 задание


# for student in students:

#     name = student["имя"]
#     grades = student["оценки"]

#     average_grade = sum(grades) // len(grades)
    
#     print(f"{name}: {average_grade:}")

# #11 задание

# numbers = {
#     "a": 10,
#     "b": 20,
#     "c": 30,
# }

# values = list(numbers.values())
# average = sum(values) // len(values)

# closest_key = min(numbers, key=lambda x: numbers[x] - average)

# print(f"Среднее значение: {average}")
# print(f"Ключ с числом наиближайшее к средн.нию: {closest_key}")

# #12 задание

# products = [
#     {"название": "Яблоко", "цена": 5},
#     {"название": "Груша", "цена": 10},
#     {"название": "Апельсин", "цена": 20}
# ]

# total_cost = 0

# for i in products:
#     total_cost += i["цена"]

# print(total_cost)

#13 задание

# countries_capitals = {
#     "Россия": "Москва",
#     "Кыргызстан": "Бишкек",
#     "Кахахстан": "Астана",
#     "США": "Вашингтон",
#     "Германия": "Берлин"
# }

# while True:
#     country = input("Введите страну: ")

#     capital = countries_capitals.get(country, "Столица не найдена")
#     print(f"Столица {country}: {capital}")


# 14 задание

# students = [
#     {"имя": "Нурай", "возраст": 15, "оценки": [85, 90, 40]},
#     {"имя": "Жаныш", "возраст": 18, "оценки": [85, 95, 50]},
#     {"имя": "Сыймык", "возраст": 20, "оценки": [93, 99, 90]}
# ]

# max_grade = max(max(student["оценки"]) for student in students)


# print("Студенты с максимальными оценками и возрастом больше 18 лет: ")
# for student in students:
#     if max(student["оценки"]) == max_grade and student["возраст"] > 18:
#         print(student["имя"])

