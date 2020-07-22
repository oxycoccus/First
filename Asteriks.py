from random import randint

# * для распаковки в аргументы функции

fruits = ['lemon', 'orange', 'apple']
print(fruits)
print(fruits[0], fruits[1], fruits[2], sep='-')
#################
print(*fruits, sep=' * ')


def transpose_list(list_of_lists):
    return [list(_) for _ in zip(*list_of_lists)]  # zip(*list_of_lists) возвращает кортежи


lOl = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(lOl)
print(transpose_list(lOl))


dy = {'year': "2020", 'month': "01", 'day': "05"}
filename = 'filename_{year}_{month}_{day}'.format(**dy)
print(filename)

# начиная с python 3.5 можно сделать несколько * в вызове одной функции
fruits = ['lemon', 'orange', 'apple']
numbers = [1, 5, 4]
print(*numbers, *fruits)

author = {'name': 'Alex', 'bookyear': 2005}
filename = 'filename_{year}_{month}_{day}--{name}--{bookyear}'.format(**dy, **author)
print(filename)



# * для упаковки аргументов, переданных в функцию к примеру в список или в словарь

# функция которая принимает любое количество элементов
def roll(*values):
    print(type(values))
    return sum(randint(1, v) for v in values)


print(roll(6))
print(roll(6, 6, 6))
print(roll(10, 5, 12))


def tag(tagname, **attrbs):
    print(type(attrbs))
    atrblist = [f'{name}="{value}"' for name, value in attrbs.items()]
    return f"<{tagname} {' '.join(atrblist)}>"


print(tag('a', en=45, str='tyu', r=89))

# Позиционные элементы с только именованными аргументами
# при определении функции все аргументы следующие за аргументом
# со звездочкой должны передаваться при вызове функции как именованные
# иначе будет ошибка

def multi(*keys, dictionary, default=None):
    return [dictionary.get(key, default) for key in keys]


fruit_color = {'lemon': 'yellow', 'apple': 'green', 'orange': 'orange'}

#print(multi('lemon', 'orange', 'tomato', fruit_color, 'no color')) # ошибка при таком вызове
print(multi('lemon', 'orange', 'tomato', dictionary=fruit_color, default='no color'))


# только именованные аргументы без позиционных

def print_values(value1, *, value2, default=None):
    print(value1)
    print(value2)
    print(default)


# можно вызывать только так
print_values(1, value2=4)
# или
print_values(1, value2=6, default='789')
# но так вызывать нельзя
#print_values(1, 4)
#print_values(1, 4, '8888')


# для указания явного что аргумент должен быть позиционным то
def print_values_pos(value1, /, *, value2, default=None):
    print(value1)
    print(value2)
    print(default)


# ошибка
#print_values_pos(value1=4, value2=5)

# правильно
print_values_pos(5, value2=8)


# РАСПАКОВКА ИТЕРИРУЕМЫХ ОБЪЕКТОВ

# какая-то хуйня но вроде можно где-то применить
print(fruits)
first, second, *r = fruits
print(first)
print(second)
print(r)

*r, last = fruits
print('******')
print(r)
print(last)


first, *r, last = fruits

print('***********')
print(first)
print(r)
print(last)


# Звездочки в литералах списков

print(fruits)
print([*fruits, *reversed(fruits)])
print(fruits+list(reversed(fruits)))


s = 'abcd'
print(*s, *reversed(s))
print([*s, *reversed(s)])
print([s+str(reversed(s))])


print(fruits)
tpl = (*fruits[1:], fruits[0])
print(tpl)
print((*fruits[1:], fruits[0]))

upper_fruits = [x.upper() for x in fruits]

new_set = {*fruits, *upper_fruits}
print(new_set)

new_set = set().union(fruits, upper_fruits)
print(new_set)


# Двойные звездочки в литералах словарей






# Звездочки в литералах словарей
print('***************')
print(dy)
print(author)
print({**dy, **author})
newdict = {**author, 'LiveIn': '1750'}
print(newdict)

newdict = {**dy, 'day': '14'}
print(newdict)


