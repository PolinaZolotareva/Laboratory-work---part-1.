print('Введите значение а')
a = int(input())
print('Введите значение b')
b = int(input())
print('Введите значение c')
c = int(input())
print('Введите значение d')
d = int(input())
print('Введите значение k')
k = int(input())

if a==0:
    print('Введите другое значение а')
    a = int(input())
elif b==0:
    print('Введите другое значение b')
    b = int(input())
print((abs((a**2-b**3 - c**3*a**2)*(b-c+c*(k-d/b**3)) - (k/b -k/a)*c)**2 - 20000))
