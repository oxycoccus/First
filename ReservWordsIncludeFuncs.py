import keyword
from builtins import print

print(keyword.kwlist)
print(keyword.iskeyword('True'))
assert keyword.iskeyword('True')

i = None
print('Result func bool(x): ', bool(i))

i = -5
print('Result func abs(x) модуль числа: ', abs(i))

lst = [1, 0, 0, 1]
zlst = []
print('Result func all(x) - ', all(lst))  # если все true или пусто
print('Result func all(x) - ', all(zlst))
print('Result func any(x) - ', any(lst))  # хоть один true, если пусто то false
print('Result func any(x) - ', any(zlst))


st = 'cat-кот'
print('Result func ascii(x) - ', ascii(st))


i = 248
print('Result func bin(x) - ', bin(i))


print('Result func callable(x) - ', callable(i))  # возвращает true если объект поддерживает вызов типа функции

print('Result func chr(x) - ', chr(55))

print('Result func dir() - ', dir(st))

print('Result func divmod() - ', divmod(5, 3))

print('Result func enumerate() - ', enumerate(lst, 0))

for idx, item in enumerate(lst, 0):  # можно вытащить из иттерируемого объекта индексы элементов и значения
    print(idx, ' - ', item)


print('Result func globals()', globals())

print('Result func hash(x)', hash('lst'))   # не все объекты могут получить хэш через эту функцию

print('Result func hex(x)', hex(20))
# перевод числа в 16-ричную систему
for i in range(100):
    print(hex(i), end='; ')
print('')
print('Result func id(x)', id(lst))   # уникальный адрес объекта

# st = input('You need to input the string: ')
# print(st)


print('Result func isinstance(x,y)', isinstance(st, str)) # проверка принадлжености классу или подклассу
# print('Result func issubclass(x,y)', issubclass(st, str)) # проверка объекта класса принадлжености  подклассу


print('Result func iter(x)', iter(st))    # возвращает иттератор

print('Result func len(x)', len(lst))

print('Result func iter(x)', iter(st))

print('Result func locals()', locals())
print('Result func type(Locals(x)', type(locals()))

# map применяет функцию к каждому элементу последовательности

slist = ['one', 'two', 'three', 'doc', 'five']
slist = list(map(str.upper, slist))     # в map передается функци без скобок
print(slist)


def addsymbol(s):
    return s + '_1'


slist = list(map(addsymbol, slist))  # в map передается функци без скобок
print(slist)

# если функции нужны два аргумента то передаются две последовательности,
# при этом map останавливается когда заканчивается самая короткая последовательность


def addsymbol2(s1, s2):
    return s1 + str(s2)


slist = list(map(addsymbol2, slist, lst))
print(slist)



# то же самое через list comprehension

slist = ['one', 'two', 'three', 'doc', 'five']
print(slist)
slist = [str.upper(part) for part in slist]
print(slist)
slist = [addsymbol(part) for part in slist]
print(slist)
slist = [addsymbol2(part1, part2) for part1 in slist for part2 in lst]  # здесь проход по всем циклам.....
print(slist)
slist = ['one', 'two', 'three', 'doc', 'five']
# отрабатывает для пар элементов и так же останавливается по самой короткой последовательности
slist = [part1+str(part2) for part1, part2 in zip(slist, lst)]
print(slist)

lst1 = [5, 10, 15, 12]
print('Result func max()', max(lst1))
print('Result func min()', min(lst1))

slist = ['one', 'two', 'three', 'doc', 'five']
print('Result func max()', max(slist))
print('Result func min()', min(slist))

print('исполльзование функции Next() для иттератора')
itr = iter(slist)
print(next(itr))
print(next(itr))
print(next(itr))

for i in range(20):
    print('Result func oct()', oct(i), end=';')
print('')


print('Result func ord()', ord('A'))

print('Result func reversed()', list(reversed(slist)))
print(slist)
slist.reverse()
print(slist)

x = 2
y = 3

print('возведение в степень')
print(x ** y)
print(pow(x, y, 10))

print('Result func repr(obj)', repr(lst1))
print('Result func repr(obj)', repr(st))
print('Result func repr(obj)', repr(itr))


print('Round')
r = 3.75635

print(round(r, 4))
print(round(r, 3))
print(round(r, 2))
print(round(r, 1))
print(round(r))

r = 56789

print(round(r))
print(round(r, 3))
