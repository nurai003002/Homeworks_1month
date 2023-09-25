# 14.09.2023
# Функции

# def hello():
#     print("Привет")

# hello()

# def sum(фрукт):
#     print(f"Привет {фрукт}")
# sum(= )

# def sum(months, months_2):
#     sum1 = (months + months_2)
#     print(f"Результат сложения {sum1}")
# months = int(input("Введите первое число: "))
# months_2 = int(input("Введите второе число: "))
# sum(months, months_2)

# def sub(months, months_2):
#     sum1 = (months - months_2)
#     print(f"Результат вычитания: {sum1}")
# months = int(input("Введите первое число: "))
# months_2 = int(input("Введите второе число: "))
# sum(months, months_2)

# def multi(months, months_2):
#     sum1 = (months * months_2)
#     print(f"Результат умножения: {sum1}")
# months = int(input("Введите первое число: "))
# months_2 = int(input("Введите второе число: "))
# sum(months, months_2)

# def divition(months, months_2):
#     sum1 = (months // months_2)
#     print(f"Результат деление: {sum1}")
# months = int(input("Введите первое число: "))
# months_2 = int(input("Введите второе число: "))
# sum(months, months_2)


# def sum(number,year):
#     print(f"Результат: {number + year}")

# def subraction(number,year):
#     print(f"Результат: {number - year}")

# def divsion(number,year):
#     print(f"Результат: {number // year}")

# def multi(number,year):
#     print(f"Результат: {number * year}")

# def main():
#     while True:
#         number = int(input("Введите первое число: "))
#         year = int(input("Введите второе число: "))
#         a = input(" 1 - Сложение, 2 - Вычитание, 3 - Деление, 4 - Умножение: ")
#         if a == "1":
#           sum(number,year)
#         elif a == "2":
#             subraction(number,year)
#         elif a == "3":
#             divsion(number,year)
#         elif a == "4":
#             multi(number,year)
# main()       

# def sound(title, animal_sound):
#     print(f"Я {title}. {animal_sound}")
# sound("Корова", "муууу мумумууууму")
# sound("Кошка", "мяу мяу мяу")
# sound("Собака", "гав гав гав")
# sound("Петух", "кукарекууу")
# sound("Жаба", "кваг кваг")

# def monthss(*months):
#     for i in months:
#         print(f"Здравствуйте {i}")
# monthss("я Нурай")

# def monthss(**data):
#     for key,value in data.items():
#         print(f"{key}: {value}")
# monthss(фрукт = "Alina", age = "18", city = "Osh", language = "English")

# def math(*nums):
#     print(f"Среднее арифметическое число: {sum(nums) // len(nums)}")
# math(1,2,3,4,5,6,7,8,9,10)
# 1
# def summ(*nums):
#      print(f"Сумма чисел: {sum(nums)}")
# summ(1,2,3,4,5,6,7,8,9,10)

# # 2
# def summ1(*nums):
#     n = 0
#     for i in nums:
#          n+=i
#     print(f"Сумма чисел: {n}")
# summ1(23,45,56,44,3,2,34)

# 3
# def lend(*nums):
#     print(f"Длина чисел: {len(nums)}")
# lend(2,3,5,6,4,3,5,6,5,3)

# 4
# def min1(*nums):
#     print(f"минимальное число: {min(nums)}")
# min1(2,4,2,34,656,32,21,0,7,55,434)

# def max1(*nums):
#     print(f"максимальное число: {max(nums)}")
# max1(2,4,2,34,656,32,21,0,7,55,434)

# д/з
# задание №1
# def season():
#     while True:
#         user = int(input("Введите номер месяца: "))
#         if user <= 2 or user == 12:
#             print("Зима")
#         elif user <= 5:
#             print("Весна")
#         elif user <= 8:
#             print("Лето")
#         elif user <= 11:
#             print("Осень")
#         else:
#             print("Ошибка!")
       
# season()

# задание №2

# def bank():

#  while True:
#     number = int(input("Введите вклад: "))
#     year = int(input("На сколько лет: "))
#     print(f"Вклад {number} рублей на {year} год под 10% годовых")
#     sum1 = float(10 / 100)
#     user = float(sum1 + 1)
#     print(f"каждый год ваш вклад увеличится на {user}%")
#     num = float(number / 10)
#     print(f"Через {year} года  ваш вклад увеличиться на {num} рублей" )
#     a = float(number + num)
#     print(f"итог суммы: {a} рублей ")
#     break
# bank()

# # задание №3


# def list(list1,list2):
#     a = list1 + list2
#     print(sum(a))
#     print(sum(a) / 10)
# list1 = [2,3,1,4,5]
# list2 = [3,2,4,2,4]
# list(list1,list2)

# задание №4

# def number():
#      for i in range(1,101):
#             print(f"{i}: 0")
# number()

# задание №5

# def fruit(list):
#    list_1 = []
#    for i in list:
#       if 'A' not in i and 'a' not in i  and 'I' not in i and 'i' not in i:
#          list_1.append(i)
#    return list_1
# list_fruit = ['Apple','Banana','Orange','Cherry','Pear']
# a = fruit(list_fruit)
# print(a)
   

# доп.задание
# задание №1
# вариант №1
# def word():
#     while True:
#         print("1 - бренд,2 - салома, 3 - салома.")
#         user = input("Выберите уникальное  слово: ")
#         if user == "1":
#             print("True")
#         else:
#             print("False")

#         break
# word()
# вариант №2
# def words(word):
#     unique_letters = set()
#     for letter in word:
#         if letter in unique_letters:
#             return False
#         unique_letters.add(letter)
#     return True
# word_1 = "Phone"
# word_2 = "Fridge"
# word_3 = "Mushroom"
# print(words(word_1))
# print(words(word_2))
# print(words(word_3))
   
# задание №2
# def num():
#      n = 56
#      num_1 = ""
#      for i in str(n):
#          num_1 = i + num_1
#      num_1 = int(num_1)
#      print(f"n = {num_1}")
# num()

# задание №3

# def chat_bot():
#     while True:
#         user = input("задайте вопрос: ")
#         print(user)
#         if user.find("?") >0:
#          print("Конечно!")
#         elif user.find("!")>0:
#            print("Успокойся!")
#         elif user == "" :
#            print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#            print("Ну и что!")
       
# chat_bot()


    

 


