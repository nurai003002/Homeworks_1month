# Исключение -> try, except

# num1 = 9
# num2 = 0 
# print(num1/num2)
# try:
#     num1 = 10
#     num2 = 0
#     print(num1/num2)
# except ZeroDivisionError:
#     print("На 0 делать нельзя!")

# while True:
#     try:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#         print(f"Результат вычитания: {num1-num2}")
#         print(f"Результат сложения: {num1+num2}")
#         print(f"Результат умножения: {num1*num2}")
#         try:
#             print(f"Результат деления: {num1/num2}")
#         except ZeroDivisionError:
#             print("На 0 нельзя делить!")
#     except ValueError:
#         print("Ошибка.Введите только числа!")


# try:
#     user = input("Введите ваш возраст:")
#     if user <= 18:
#         print("Вход запрещен!")
# except TypeError:
#     print("Добавьте тип данных int ")


#  тема  №2
# Множества -> set, fronzenset
# list -> []
# tuple -> ()
# dict -> {}
#  set -> {}

# создается {} скобками
# не имеет структуру или определенного порядка
# не можем использовать индекс и срезы
# не имеет дубликатов имеет уникальные элементы(данные)
# set() изменяемый тип данных
# frozenset() неизменяемый тип данных

# dicti = {"name": "Amina"}
# num = {"Amina","Nurkeldi","Nurber","Aibek"}
# print(type(dicti))
# print(type(num))
# print(num)

# users = {"Amina","Nurkeldi","Nurber","Aibek","Amina"}      
# print(users)   

 

# num = [223333,434,2,4,34,2312,3,343,44,32,34,333,233,23,3,444444,3,3,233] 
# print(num)  
# duble_num = set(num)     
# num = list(duble_num)
# print(num)              

# try:
#     users = {"Amina","Nurkeldi","Nurber","Aibek","Amina"} 
#     print(users[1:5]) 
# except:
#     print("set() не может выполнять срезы")

# users = {"Amina",1,"Nurkeldi","Nurber","Aibek","Amina"} 
# users.add("Yryskeldi")
# print(users)
# users.add("Nurbek")
# print(users)
# users.add("1")
# print(users)

# users_set = {"Amina",1,"Nurkeldi","Nurber","Aibek","Amina"}
# print(users_set)
# users_frozenset = frozenset({"Amina",1,"Nurkeldi","Nurber","Aibek","Amina"})
# print(users_frozenset)
# print(type(users_set))
# print(type(users_frozenset))


# д/з 
# №1
# while True:
#     try:
#         user_1 = int(input("Введите первое число: "))
#         user_2 = int(input("Введите второе число: "))
#         print(user_1 / user_2)
#     except:
#         print(f"Число {user_1} на 0 невозможен!")
#         print("Введите другие числа")

# №2
# while True:
#     try:
#         user = input("Введите число: ")
#         int_user = int(user)
#         print(type(int_user))
#         print(int_user)
#     except:
#         print("строка не является числом!")




# №3
# try:
#     text = input('введите текст:')
#     set_text = set(text.split())
#     frozenset_text = frozenset(set_text)
#     len_words  = len(set_text)
#     print("Количество уникальных слов:", len_words)
# except:
#     print('ошибка')


 # доп задание
# list1 = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [1, 2, 3, 4, 5, 11, 12, 13, 14, 15]

# set1 = set(list1)
# set2 = set(list2)

# set1 = frozenset(list1)
# set2 = frozenset(list2)

# a = set1.intersection(set2)
# print(a)


