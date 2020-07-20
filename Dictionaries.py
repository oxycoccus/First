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

getvalue = 'home' #input('Enter key to find: ')

try:
    print('dd["home"]', dd.get(getvalue, 'Value not found'))
except Exception as e:
    print("Exception to get dd['home']:", e.__class__.__name__)

dd.clear()
print(dd)
dd = dict.fromkeys(list('abcde'), None)
print(dd)
print(type(dd.items()))
print(dd.items())


for n in dd.items():
    print(type(n))
    print(n)

print(dd.keys())

for n in dd.keys():
    dd[n] = '5'

print(dd)

print(type(dd.values()))
print(dd.values())


# не работает а просто перебирает значения
for n in dd.values():
    n = 6

print(dd)

dd.update({'f':5})
dd.update(dict(zip(list('abcdefg'), (_+1 for _ in range(7)))))
print(dd)

print(dd.setdefault('h', 8))
print(dd)

# for n in range(len(dd)):
#     print(dd.popitem())
print(dd)

print(dir({}))

for key in dd:
    print(key, " - ", dd[key])

for item in dd.items():
    print(item)

# распаковка ключей и значений из словаря

for key, value in dd.items():
    print('key', repr(str(key)), 'has value:', value)

#перебор по keys
for key in dd.keys():
    print('Key:', key, '=',dd[key])

#перебор по values
for value in dd.values():
    print(value)

# keys() и values() очень полезны для поиска ключа или значения в словаре

if 'x' in dd.keys():
    print('In dictionary')
else:
    print('NOT in dictionary')

if 8 in dd.values():
    print('value in dictionary')
else:
    print('value NOT in dictionary')

for key in dd:
    dd[key] = round(dd[key]*0.9, 2)

print(dd)

for key in list(dd.keys()):
    if key == 'b':
        del dd[key]
del dd['c']
print(dd)

d = dict(zip('one,two,three,for,five'.split(','), (_+1 for _ in range(5))))
print(d)

#перемена мест ключей и значений в словаре
dnew = {}
for key, value in d.items():
    dnew[value] = key
print(dnew)


total = 0
for value in dd.values():
    total += value
print(total)

l1 = ['fruit', 'color', 'pet']
l2 = ['apple', 'blue', 'dog']

dcomp = {key: value for key, value in zip(l1, l2)}
print(dcomp)

dcomp = {value: key for key, value in dcomp.items()}
print(dcomp)

dcomp = {key: value for key, value in dd.items() if value>1 and value<6}
print(dcomp)

def upp(s):
    return s*10-1

# смысла нет гонять через map .....
dcomp = {key: value for key, value in zip(dcomp.keys(),list(map(upp,dcomp.values())))}

dcomp = {key: upp(value) for key, value in dcomp.items()}

print(dcomp)

total = sum([value for value in dcomp.values()])
print(total)
#подсчитать total можно гораздо проще

total = sum(dcomp.values())
print(total)

# удаление элементов словаря....
print(dcomp)
dcompn = {key: dcomp[key] for key in dcomp.keys()-{'e'}}
print(dcompn)

dcompn = {k: v for k, v in zip(l1, l2)}
print(dcompn)
#
# dcompn = {k: dcompn[k] for k in sorted(dcompn)}
# print(dcompn)



# перебор словаря с предварительной сортировкой по ключу

for k in sorted(dcompn):
    print(k, '-', dcompn[k])

# перебор словаря с предварительной сортировкой по значению


def sortbyvalue(item):
    return item[1]


for k, v in sorted(dcompn.items(), key=sortbyvalue):
    print(k, '-', v)
# получается одно и то же
for k in sorted(dcompn, key=sortbyvalue, reverse=True):
    print(k, '-', dcompn[k])

for v in sorted(dcompn.values()):
    print(v)

#popitem

print(dcompn)
while True:
    try:
        print(f'Dict len: {len(dcompn)}')
        item = dcompn.popitem()
        print(f'{item} removed')
    except Exception as e:
        print('End of the dict:', e.__class__.__name__)
        break
print(dcompn)

dcompn = {k: v for k, v in zip(l1, l2)}

print(dcompn)




















