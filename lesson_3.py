# 04.09.23
# name = "Kyrgyzstan"
# print(name[0:6])

# name_list = ["Nurbolot","Nurai","Aman","Erbol","Yryskeldi"]
# print(name_list)
# print(name_list[1])
# print(name_list[1:4])
# print(type(name_list))

# append-добавляет в список слово
# name_list.append("Geeks")
# print(name_list)

# extend-Добавляет в список еще список
# name = ["Beksultan","Ulan"]
# name_list.extend(name)
# print(name_list)

# insert-добавляет слово в начало списка
# name_list.insert(0,"Geeks")
# print(name_list)

# pop-удаляет по индексу.
# name_list.pop(5)
# print(name_list)

# index()-находит индекс слова из списка
# print(name_list.index("Aman"))

# remove()-второй способ удаления из списка
# name_list.remove("Ulan")
# print(name_list)


# УСЛОВИЕ # if,elif,else
# num1 = 20
# num2 = 100
# if num1 > num2:
#     print(num1)
# else:
#     print(num2)

# num1 = int(input("Введите число: "))
# if num1 % 2 == 0:
#     print(" Число четное")
# else:
#     print(" число не четное")


# age = int(input("Введите возрaст: "))
# if age < 12:
#     print("Ты ребенок!!")
# elif age > 12 and age < 18:
#     print("Вы подросток")

# elif age >= 18 and age < 30:
#     print("Вы мужик/женщина")
# else:
#     print("Вы старый")



# Д/З
# задание №1
# user_age = int(input("Введите ваш возрaст: "))
# if user_age < 18:
#     print("Вы являетесь несовершеннолетним.")
# elif user_age > 17 and user_age <= 65:
#     print("Вы являетесь взрослым")
# elif user_age > 65:
#     print("Вы являетесь пожилым")

# задание №2
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# if num1 > num2 < num3:
#     print(f"{num2} наименьшее число")
# elif num1 < num2 < num3:
#     print(f"{num1} наименьшее число")
# elif num1 > num2 > num3:
#     print(f"{num3} наименьшее число")


# задание №3
# words_list = ['cake','food','knif','spoon','sugar','salt','plate','freeze','shelves','egg','glass','chair','table','kittle','cooking','nuke']
# print(words_list[2:7])

# задание №4
# school_list = ['pen','pencil','copybook','notebook','bag','line','book','shelf','map','chair','table']
# print(school_list)
# school_list.pop(2)
# school_list.pop(8)
# print(school_list)

# school_list.append("общий тетрадь")
# school_list.append("Маркер")
# school_list.append("красная ручка")
# print(school_list)

# задание №5
# number_list = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
# print(number_list)
# number_list.remove("2")
# number_list.remove("16")
# print(number_list)
# number_list.insert(0,"5")
# number_list.insert(0,"9")
# print(number_list)

# задание №6
# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,89,0,9,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3]
# numbers.sort()
# print(numbers)


# задание №7
# numbers_list = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,89,0,9,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3]
# print(sorted(numbers_list, reverse=True))

# задание №8
# numbers_list = "23 152 568358 0987534 52144214568   5 31  2432585368 0212432574 3808 6542 356523 60986432456 236795423468452457313253214523"
# print(numbers_list.count("2"))
# print(numbers_list.count("5"))
# print(numbers_list.count("3"))

# задание №9

# number_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# sum = 0
# for num in number_list:
#      avg = len(number_list)
# print("Среднее арифметическое:", avg)




   



