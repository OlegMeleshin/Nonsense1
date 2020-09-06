

########    TWO DIGITS COMPARISON    ########

#a = 5345543
#b = 646523

#if (a > b):
#    print(f"Наибольшее: {a}")
#else:
#    print(f"Наибольшее: {b}")



#a = int(input("Parameter 1: "))
#b = int(input("Parameter 2: "))

#if (a > b):
#    print("Parameter 1 is bigger")
#elif (b > a):
#    print("Parameter 2 is bigger")
#else:
#    print("They`re equal")



#######    SUPER GAME    ########
#print("Супер игра по непонятным правилам")
#a = int(input("Введите число: "))
#if (a % 10 == 0):
#    print("Вы выйграли")
#elif (a % 5 == 0):
#    print("Вы проиграли")
#elif (a % 2 == 0):
#    print("Ничья. Сыграем еще?")


####### CHET/NECHET ######
#count_chet = 0
#count_nechet = 0

#a = int(input("Введите 1 число: "))
#if (a % 2 == 0):
#    count_chet += 1
#else:
#    count_nechet +=1

#a = int(input("Введите 2 число: "))
#if (a % 2 == 0):
#    count_chet += 1
#else:
#    count_nechet +=1

#a = int(input("Введите 3 число: "))
#if (a % 2 == 0):
#    count_chet += 1
#else:
#    count_nechet +=1

#a = int(input("Введите 4 число: "))
#if (a % 2 == 0):
#    count_chet += 1
#else:
#    count_nechet +=1

#print(f"Четных: {count_chet}, Нечетных: {count_nechet}")


######    УГАДАЙКА    ######
#import random
#
#comp = random.randint(1,3)
#human = int(input("Угадайте число? (от 1 до 3): "))
#
#if (human == comp):
#    print("Вы угадали!")
#else:
#    human = int(input("Вторая попытка. Введите число от 1 до 3: "))
#    if (human == comp):
#        print(f"Вы угадали! Компьютер загадал {comp}")
#    else:
#        print(f"Неправильно! Компьютер загадал {comp}")


###### УГАДАЙКА НЕДОДЕЛАННАЯ  ########
#import random

#comp = random.randint(0,100)
#human = int(input("Введите число от 0 до 100: "))
#if (human >= comp - 15 and human <= comp + 15):
#    print(f"Число находится в диапазоне 30")

#    human = int(input("Продолжим. Введите число: "))
#    if (human >= comp - 5 and human <= + 5):
#        print(f"Число в диапазоне 10.")
#                
#        human = int(input("Продолжим. Введите число: "))
#        if (human >= comp - 1 and human <= + 1):
#            print(f"Число в диапазоне 3.")
#        else:
#                
#            human = int(input("Последний шаг. Введите число: "))
#            if (human == comp):
#                print(f"Победа! Компьютер загадал {comp}")
#else:
#    print(f"Число не в диапазоне. Спасибо за игру.")
    
#print(f"Диапазон: {comp - 15}...{comp + 15}")
###########################################



#a = int(input("Значение 1: "))
#b = int(input("Значение 2: "))
#c = int(input("Значение 3: "))

#if (a < b):
#    if (a < c):
#        print(a)
#if (b < a):
#    if (b < c):
#        print (b)
#if (c < b):
#    if (c < a):
#        print(c)
#if (a == b):
#    if (b == c):
#        print(a)




##### СУММА НАИМЕНЬШИХ, ПРОИЗВЕДЕНИЕ НАИБОЛЬШИХ ########
#a = int(input("Значение 1: "))
#b = int(input("Значение 2: "))
#c = int(input("Значение 3: "))
#
#summa = 0
#proizv = 0
#
#if a <= b:
#    if b <= c:
#        summa += a + b
#    else:
#        summa += a + c
#    proizv = b * c
#elif b <= c:
#    if c <= a:
#        summa += b + c
#    else:
#        summa += b + a
#    proizv = c * a
#elif c <= a:
#    if a <= b:
#        summa += c + a
#    else:
#        summa += c + b
#    proizv = a * b
#print(f"Сумма наименьших: {summa}")
#print(f"Произведение наибольших {proizv}")






#a = int(input("Значение 1: "))
#b = int(input("Значение 2: "))
#
#if a > 0 and b > 0:
#    print("Обе положительные")
#elif a < 0 and b < 0:
#    print("Обе отрицательные")
#elif a == 0 and b == 0:
#    print("Обе равны нулю")
#elif a < 0 and b >= 0 or a >= 0 and b < 0:
#    print("Переменные с разными знаками")




##########   КРАТНО - НЕКРАТНО  ##########
#a = int(input("1: "))
#b = int(input("2: "))
#
#if a > b and a % b == 0 or b > a and b % a == 0:
#    print("Кратно")
#else:
#    print("Не кратно")





#a = int(input("1: "))
#b = int(input("2: "))
#c = int(input("3: "))
#
#mult = a * b * c
#if mult % (a + b) == 0 or mult % (a + c) == 0 or mult % (b + c) == 0:
#    print("Кратно")
#else:
#    print("Борода")





#############
#import random
#
#comp = random.randint(1,1000)
#comp2 = random.randint(1,1000)
#
#print(f"{comp}, {comp2}")
#if comp % comp2 == 0 or comp2 % comp == 0:
#    print("Ok")
#else:
#    print("Boroda")



#import random
#comp2 = random.randint(100, 300)
#comp1 = random.randint(1, 99)
#
#if comp1 % 2 == 0:
#    print(f"{comp1} - even")
#else:
#    print(f"{comp1} - odd")
#
#if comp2 % 2 == 0:
#    print(f"{comp2} - even")
#else:
#    print(f"{comp2} - odd")



#import random
#a = random.randint(0,100)
#print(a)
#if a % 2 == 0:
#    print("Кратно 2")
#if a % 3 == 0:
#    print("Кратно 3")
#if a % 5 == 0:
#    print("Кратно 5")
#if a % 7 == 0:
#    print("Кратно 7")
#if a % 11 == 0:
#    print("Кратно 11")

######## 3 в УБЫВАЮЩЕМ порядке ########

#a = int(input("1: "))
#b = int(input("2: "))
#c = int(input("3: "))

#if a >= b and b >= c:
#    print(a, b, c)
#elif a >= c and c >= b:
#    print(a, c, b)

#if b >= a and a >= c:
#    print(b, a, c)
#elif b >= c and c >= a:
#    print(b, c, a)

#if c >= a and a >= b:
#    print(c, a, b)
#elif c >= b and b >= a:
#    print(c, b, a)

######   3 в ВОЗРАСТАЮЩЕМ порядке #######

#a = int(input("1: "))
#b = int(input("2: "))
#c = int(input("3: "))

#if a >= b and b >= c:
#    print(c, b, a)
#elif a >= c and c >= b:
#    print(b, c, a)

#if b >= a and a >= c:
#    print(c, a, b)
#elif b >= c and c >= a:
#    print(a, c, b)

#if c >= a and a >= b:
#    print(b, a, c)
#elif c >= b and b >= a:
#    print(a, b, c)



#a = int(input("1: "))
#b = int(input("2: "))
#c = a * b
#
#if c % 2 == 0 or \
#   c % 3 == 0 or \
#   c % 5 == 0 or \
#   c % 7 == 0 or\
#   c % 11 ==0:
#    print("Кратно 2, 3, 5, 7 или 11")



#x = int(input("1: "))
#if x % 2 == 0:
#    print(f"Число четное, квадрат равен {x * x}")
#    if (x * x) % 3 == 0:
#        print(f"Квадрат {x * x} кратен 3")
#    else:
#       print(f"Не кратно 3, возводим в куб, получаем {x * x * x}")
#if x % 2 != 0:
#    print(f"Число нечетное, умножаем на 2, получаем {x * 2}")
#    if (x * 2) % 5 == 0:
#        print("Кратно 5")
#    else:
#        print(f"Не кратно 5, возводим в 3-ю степень, получаем {x * x * x}")



#a = int(input("Введите двузначное число: "))
#
#if a < 10 or a > 99:
#    print("Число не двузначное")
#else:
#    print(f"{a % 10}")




#a = int(input("Введите двузначное число: ")) 
#x = a % 10
#if a < 10 or a > 99:
#    print("Число не двузначное")
#else:
#    print(f"{(a - x) // 10}")
#    if ((a - x) // 10) % 2 == 0:
#        print("Четное")




#a = int(input("Введите 3х значное число: "))
#
#if a < 100 or a > 999:
#    print("Число не 3х значное")
#x = a % 10
#y = ((a % 100) - x) // 10 
#z = a // 100
#
#print(f"{z} сотен, {y} десятков, {x} единиц")
#
#if z % 2 == 0:
#    print(f"{z} Четное")
#elif z % 2 != 0:
#    print(f"{z} нечетное")
#
#if y % 2 == 0:
#    print(f"{y} Четное")
#elif y % 2 != 0:
#    print(f"{y} нечетное")
#
#if x % 2 == 0:
#    print(f"{x} Четное")
#elif x % 2 != 0:
#    print(f"{x} нечетное")



#№№№№№№№№№№№№№№№№№№№  НЕПРАВИЛЬНО №№№№№№№№№№№№№№№№№№
#x = int(input("Введите 4х значное число: "))
#
#if x < 1000 or x > 9999:
#    print("Число не 4х значное")
#a = x % 10
#b = ((x % 100) - a) // 10 
#d = x // 1000 
#c = (x - (d * 1000) - a - (b * 10)) // 100
#print(f"{d} тысяч, {c} сотен, {b} десятков, {a} единиц")
#
#if d % 2 == 0:
#    print(f"{d} четное")
#elif d % 2 != 0:
#    print(f"{d} не четное")
#if c % 2 == 0:
#    print(f"{c} Четное")
#elif c % 2 != 0:
#    print(f"{c} нечетное")
#
#if b % 2 == 0:
#    print(f"{b} Четное")
#elif b % 2 != 0:
#    print(f"{b} нечетное")
#
#if a % 2 == 0:
#    print(f"{a} Четное")
#elif a % 2 != 0:
#    print(f"{a} нечетное")
#
#newdigit = 
#print("Новое число, составленное из четных: ")



###  Из    Решебника  #######
#x = int(input("Введите 4х значное число: "))
#
#if x < 1000 or x > 9999:
#    print("Число не 4х значное")
#
#else:
#    newDigit = 0
#    power = 0
#    for i in range(4):
#        if (x % 10) % 2 == 0:
#            print (x % 10)
#            newDigit += (x % 10) * 10 ** power
#            power += 1
#        x //= 10
#print(f"Число из четных цифр {newDigit}")



#s = input("Insert string: ")
#if len(s) % 3 == 0:
#    print("Кол-во символов кратно 3")
#    print(s) \
#    print(s) \
#    print(s) \
#elif len(s) % 3 != 0:
#    print(s * 4)
























    









