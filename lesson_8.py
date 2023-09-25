# Лямбда - анонимные функции
# summ = lambda num1,num2: num1+num2
# result = summ(5,6)
# print(f"Результат сложения: {result}")

# summ = lambda num1,num2: num1+num2
# nu1 = int(input("Введите первое число: "))
# nu2 = int(input("Введите второе число: "))
# result = summ(nu1,nu2)
# print(f"Результат сложения: {result}")

# summ = lambda num1,num2: num1+num2
# summ1 = lambda num1,num2: num1-num2
# summ2= lambda num1,num2: num1//num2
# summ3= lambda num1,num2: num1*num2
# nu1 = int(input("Введите первое число: "))
# nu2 = int(input("Введите второе число: "))
# result = summ(nu1,nu2)
# result1 = summ1(nu1,nu2)
# result2 = summ2(nu1,nu2)
# result3 = summ3(nu1,nu2)
# print(f"Результат сложения: {result}")
# print(f"Результат вычитания: {result1}")
# print(f"Результат деления: {result2}")
# print(f"Результат умножения: {result3}")


# lestter = [1,2,3,4,5,6,7,8,9,10]
# result = list(map(lambda i: i*2, lestter))
# print(result)

# names = ["Mergul","Erbol","Yryskeldi","Beishen","Omonboi","Nurai","Bakai"]
# names_len = list(map(lambda i: f"{i} - {len(i)} букв ",names ))
# print(f"Результат:{names_len}")

# Работа с файлами
# file_write = open('user.txt', 'w')
# file_write.write("Привет, меня зовут geeks и мне 2 года")
# file_write.close()

# file_read = open('user.txt', 'r')
# result = file_read.read()
# print(f"Результат: {result}")

# names = ["Mergul","Erbol","Yryskeldi","Beishen","Omonboi","Nurai","Bakai"]
# 1 способ
# file_write = open('names.txt', 'w')
# for i in names:
#     file_write.write(f"Name: {i}. \n")
    
# file_write.close()

# file_read = open('names.txt', 'r')
# result = file_read.read()
# print(result)

# 2 способ
# with open("names.txt", 'w') as file_write:
#     for i in names:
#         file_write.write(f"Name: {i}. \n")
# with open("names.txt", 'r') as file_read:
#     result = file_read.read()
#     print(result)

# with open('python.py', 'w') as write:
#     write.write("""names = ["Mergul","Erbol","Yryskeldi","Beishen","Omonboi","Nurai","Bakai"]
# with open("names.txt", 'w') as file_write:
#     for i in names:
#         file_write.write(f"Name: {i}. ")

# with open("names.txt", 'r') as file_read:
#     result = file_read.read()
#     print(result)""")


# д/з
# №1
# num_list = [1,2,3,4,5,6,7,8,9,10,100,11,15,77,79]
# max_num = max(num_list,key=lambda i:int(i))
# print(max_num)

# # №2
# 1 вариант
# print("Четные числа: ")
# print(list(filter(lambda x: x % 2 == 0, [23,4,32,23,14,7,6,5,7,8,43,23,23,13,5,6,3,6])))

# 2 вариант
# a = lambda num1: num1 % 2 == 0
# result = a(24)
# result1 = a(11)
# print(result)
# print(result1)

# №3
# names = ["Mergul","Erbol","Yryskeldi","Beishen","Omonboi","Nurai","Bakai"]
# names_filer = list(filter(lambda i: len(i) >5 ,names))
# print(names_filer)

# чтение содержимого файла
# №1
# with open("example.txt",'w') as file_write:
#     file_write.write("Hello Geeks")


# with open("example.txt", 'r') as file_read:
#     result = file_read.read()
#     print(result)

 #2
# user = input("Введите текст: ")
# with open("output.txt", 'w') as file_write:
#     file_write.write(user)



