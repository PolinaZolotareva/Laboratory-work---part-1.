string = 'Привет, Лимон, как, твое, Лицо'
string = string.split(', ')
for i in range(0, len(string)):
    if string[i][0]== "Л" and string[i][1]=='и':
        print(string[i])


