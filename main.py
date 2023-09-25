# hello_geeks = "Hello World"
# print(hello_geeks)

# num1 = 5
# num2 = 10
# print(num1 + num2)


# num1 = 20
# num2 = 10
# print(num1 - num2)

# num1 = 20
# num2 = 10
# print(num1 * num2)
# print(50 / 5)
# print(100 // 5)
# print(5 % 2)
# print(2**3)

# geeks = "Working"
# print(geeks)
# print("geeks")


# \n -  для разделения строки 

# info = 'my name is Nurai \n I am a student'
# print(info)

# способ №1
# name = "Нурай"
# print(f"Меня зовут {name}")
# >> Меня зовут Нурай

# способ №2
# name = "Нурай"
# print("Меня зовут", name)
# >> Меня зовут Нурай

#  str -> string - строка
# number = str(500)
# print(type(number))
# print(type(500))

# int -> integer - целое число

# print("Geeks" + "Osh")

# int -> integer - целое число
# num1 = 10
# num2 = 30

# number = int(5.6)
# print(number)


# float -> десятичные числа
# number = float(100)
# print(number)

# bool -> boolean - "true, false"
# num1 = 10
# num2 = 20
# print(num1 > num2)
# print(num2 > num1)




# Д/з

 # 1
# num1 = 5
# num2 = 10
# print(num1 + num2)

 # 2
# num1 = 10
# num2 = 5
# print(num1 - num2)

 # 3
# num1 = 20
# num2 = 5
# print((num1 * num2)//2)

# # 4
# x = 10
# y = 5
# z = 2
# print((x + y)*z)

 # дополнительное задание:
 # 5
# num1 = 5
# num2 = 10
# print(f"число: {num1} < {num2} :True")
# print(f"число: {num1} > {num2} :False")

 # второй вариант
# num1 = 5
# num2 = 10
# print(num1 < num2)
# print(num1 > num2)

# lesson2



# import random 

# user_health = 5
# bot_health =5 
# while True:
#     if user_health ==0 or bot_health ==0:
#         break
#     else:
#         bot = random.choice(["Камень", "Ножницы", "Бумага"])
#         user = input("Введите выбор:")
#         if user =="Камень":
#             if bot =="Камень":
#                 print(f"Ничья.У вас: {user_health}, у бота: {bot_health}")
#             elif bot =="Ножницы":
#                 bot_health-=1
#                 print(f"Вы выиграли.У вас: {user_health}, у бота: {bot_health}")
#             elif bot =="Бумага":
#                 user_health -=1
#                 print(f"Вы проиграли.У вас: {user_health}, у бота: {bot_health}")
#         elif user =="Ножницы":
#             if bot =="Камень":
#                 user_health -=1
#                 print(f"Вы проиграли.У вас: {user_health}, у бота: {bot_health}")
                
#             elif bot =="Ножницы":
#                 print(f"Ничья.У вас: {user_health}, у бота: {bot_health}")
#             elif bot =="Бумага":
#                 bot_health-=1
#                 print(f"Вы выиграли.У вас: {user_health}, у бота: {bot_health}")
                
                
#         elif user =="Бумага":
#             if bot =="Камень":
#                 bot_health-=1
#                 print(f"Вы выиграли.У вас: {user_health}, у бота: {bot_health}")
#             elif bot =="Ножницы":
#                 user_health -=1
#                 print(f"Вы проиграли.У вас: {user_health}, у бота: {bot_health}")
#             elif bot =="Бумага":
#                 print("Ничья")
#         else:
#             print("Неверный вариант")





