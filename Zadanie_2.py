import random
a=random.randint(0,100)
print('Введите число')
b=int(input())
while b != a:
    if b>a:
        print('Ваше число больше.Введите другое число!')
        b=int(input())
    else:
        print ('Ваше число меньше.Введите другое число!')
        b=int(input())
print('Вы угадали число.Поздравляю!')