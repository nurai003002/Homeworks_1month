# 07.09.2023

# car_list = ['tesla','nissan','mersedes','BMW','opel']
# car_list.insert(3,"lexus")
# car_list.pop(5)
# print(car_list)

# user = int(input("Напишите ваш текущий балл: "))
# if user >= 90 :
#     print("Отлично, вы получили 5")
# elif user >= 80 and user < 90:
#     print("Хорошо, вы получили 4")
# elif user >= 70 and user <80:
#     print("Не очень, вы получили 3")
# elif user >= 60 and user < 70:
#     print("Плохо, вы получили 2")
# else:
#     print("Ужас!")



# Tuple() -> Картеж(неизменяемый тип данных)
# name = (1,"one",1.4, [1,2,3,4], True)
# print(name)
# print(name[1:3])
# name_list = list(name)
# name_list.append(5)
# name = tuple(name_list)  
# print(name)

# name = ("name",)
# print(name)

# numbers = ('1','2','3','4','5')
# print(numbers)


# name = ["Geeks","Osh","Bishkek","Kyrgyzstan"]
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

# for element in name:
#     print(element)


# for num in range(1,101):
#     print(num)

# message = "Hello"
# for char in message:
#     print(char)

# Д/З
# задание №1
# it_company = ('Google', 'Amazon', 'Microsoft')
# it = list(it_company)
# it.append('Tesla')
# it_company = tuple(it)
# print(it_company)

# задание №2
# it_company = ('Google', 'Amazon', 'Microsoft')
# print(it_company[1])


# задание №3
# it_company = ('Apple', 'Amazon', 'Microsoft')
# print(it_company)

# задание №4
# it_company = ('Google', 'Amazon', 'Microsoft')
# print(it_company[0:2])

# задание №5
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3', 'overview') 
# print(text_tuple.count("Python"))

# задание №6
# text = ('Experienced','programmers','in','any','other','language','can','pick','up','Python','very','quickly,','and','beginners','find','the','clean','syntax','and','indentation')
# text1 = list(text)
# print(text)
# text1.pop(3)
# text1.pop(4)
# text1.pop(5)
# text1.pop(6)
# text1.pop(7)
# text1.pop(8)
# text = tuple(text1)
# for i in text:
#     print(i)

# text = ('Experienced', 'programmers', 'in', 'other', 'can', 'up', 'very', 'and', 'find', 'the', 'clean', 'syntax', 'and', 'indentation')
# text1 = list(text)
# name = ["do","this","over here","5","2"]
# text1.extend(name)
# text = tuple(text1)
# print(text)
# for i in text:
#     print(i)


# задание №7
# for i in range(1,100):
#     print(i)

# задание №8
# number_list = []
# for i in range(1,1001):
#     number_list.append(i)
# print(number_list)
# print(min(number_list))
# print(max(number_list))
# print(sum(number_list))



# задание №9
# number = []
# for i in range(1, 497):
#     number.append(i)
#     print(number)

# задание №10



# доп. занятие

# задание №1
# while True:
#     age = int(input("Введите ваш возраст: "))
#     if age >= 18:
#         print("Доступ разрешен!")
#         break
#     else:
#         print("Доступ запрешен!")

#доп.задание
# задание №1

# import random

# def start_game():
#     words = ['камень','ножницы','бумага']
#     bot = random.choice(words)
#     attempts = 5
#     bot =5 

#     print("Добро пожаловать в игру КАМЕНЬ, НОЖНИЦы, БУМАГА!")
#     print(f"У вас есть {attempts} попыток")

#     name = "ножницы"
#     name_2 = "камень"
#     name_3 = "бумага"
    
#     while attempts == 0:
#         user = input("Выберите (камень?,ножницы?,бумага?) ").lower()


            

#         bot = random.choice(words)
#         print(f"мой выбор {bot}")

    

#         if bot == name and user == name_3:
#              attempts -= 1
#              print(f" У вас есть {attempts} попыток")
        
        
#         if bot == name_2 and user == name:
#             attempts -= 1
#             print(f" У вас есть {attempts} попыток")
        
        
#         if bot == name_3 and user == name_2:
#             attempts -= 1
#             print(f" У вас есть {attempts} попыток")
        

#         if attempts == 0:
#              print("Игра окончина, у вас осталось 0 попыток!")
#              print("ТЫ ПРОИГРАЛ!!!")
             
        
       
          
# start_game()





