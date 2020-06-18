import keyword

print(keyword.kwlist)
print(keyword.iskeyword('True'))
assert keyword.iskeyword('True')

i = None
print('Result func bool(x): ', bool(i))

i = -5
print('Result func abs(x) модкль числа: ', abs(i))

lst = [1, 0, 0, 1]
zlst=[]
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







