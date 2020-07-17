from itertools import *

# создание словаря

d = {}
print(d)

d = {'dict': 1, 'dictionary': 2}
print(d)

d = dict(short='dict', long='dictionary')
print(d)

d = dict([(1, 2), (3, 4)])
print(d)

d = dict.fromkeys(['a', 'b', 'c'])
print(d)

d = dict.fromkeys(['a', 'b', 'c'], 100)
print(d)




# генератор словарей
print('generator')
d = {str(x): None for x in range(10)}
print(d)

lst = ['a', 'b', 'c', 'd']

print('Присвоение значений по новому ключу расширяет уже созданный словарь')
for _ in range(len(lst)):
    d[_+10] = lst[_]
print(d)

print('Генератором из списка')
d = {i: lst[i] for i in range(len(lst))}
print(d)

print('Из двух списков')

d = dict(zip(['1', '2', '3', '4'], ['a', 'b', 'c']))
print(d)

d = dict(zip_longest(['1', '2', '3', '4'], ['a', 'b', 'c']))
print(d)

print('Из списка и кортежа')

d = dict(zip((_ for _ in range(3)), list('abc')))
print(d)

print('Работа со словарями')

print('d[0] =', d[0])
d = dict(zip(list('abc'), (_ for _ in range(3))))
print(d)
print("d['a'] =", d['a'])

print("d['c'] =", d['c'])
d['c'] = d['c']**3
print(" **3 d['c'] =", d['c'])

print('Присвоение значения по новому ключу добавляет значение в словарь: d[''d''] = 16')
print(d)
d['d'] = 16
d[1] = 'reversevalue'
print(d)


print('Создание словаря из одного списка, где ключ и значение это следующие друг за другом элементы списка')
a = ['hello', 'world', '1', '2']
i = iter(a)
print(i)
dd = dict(zip(i, i))
print(dd)





