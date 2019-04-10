k = int(input('Введите какое количество элементов ...!'))
if k < 10:
    print('введи больше 10 придурок')
    k = int(input())

s=[]
for i in range(0,k):
    s.append(int(input('Введите' + '   ' + str(i+1)+ '   ' + "элемент списка")))
print(s)
s = [x for x in s if x % 2 != 0]
for i in range (0,2):
    s.append(int(input('Введите новый ' + '   ' + str(i+1)+ '   ' + "элемент списка")))
print(s)





