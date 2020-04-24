"""ШИФРОВАНИЕ ТЕСКТА ИСПОЛЬЗУЯ АЛГОРИТМ ЦЕЗАРЯ, Шифровка/Дешифровка"""
beta = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alpha = 'abcdefghijklmnopqrstuvwxyz'
n = int(input('Введите ключ --> '))
s = input('Ввидете текст для шифрования --> ').strip()
l = input('Введите - alpha, если ваш текст состоит из английских букв или beta,если из русских --> ')
def CaesarCrypt(n,s,l):
    res = ''
    if l == 'alpha':
        for c in s:
            res += alpha[(alpha.index(c) + n) % len(alpha)]
    else:
        for c in s:
            res += beta[(beta.index(c) + n) % len(beta)]
    return res
def CaesarDecrypt(s):
    for i in range(33):
        print(i,CaesarCrypt(i,s,l))
print('Result: "' + CaesarCrypt(n,s,l) + '"')

