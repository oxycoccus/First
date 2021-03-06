import sys
import datetime


# форматирование с помощью %


s = 'Hello %s !!!' % 'Vasia'
print(s)

s = '%d-%s, %d-%s' % (1, 'banana', 6, 'apple')
print(s)


# Формат	Что получится
# '%d', '%i', '%u'	Десятичное число.
# '%o'	Число в восьмеричной системе счисления.
# '%x'	Число в шестнадцатеричной системе счисления (буквы в нижнем регистре).
# '%X'	Число в шестнадцатеричной системе счисления (буквы в верхнем регистре).
# '%e'	Число с плавающей точкой с экспонентой (экспонента в нижнем регистре).
# '%E'	Число с плавающей точкой с экспонентой (экспонента в верхнем регистре).
# '%f', '%F'	Число с плавающей точкой (обычный формат).
# '%g'	Число с плавающей точкой. с экспонентой (экспонента в нижнем регистре), если она меньше, чем -4 или точности, иначе обычный формат.
# '%G'	Число с плавающей точкой. с экспонентой (экспонента в верхнем регистре), если она меньше, чем -4 или точности, иначе обычный формат.
# '%c'	Символ (строка из одного символа или число - код символа).
# '%r'	Строка (литерал python).
# '%s'	Строка (как обычно воспринимается пользователем).
# '%%'	Знак '%'.

# Спецификаторы преобразования записываются в следующем порядке:
#
# %.
# Ключ (опционально), определяет, какой аргумент из значения будет подставляться.
# Флаги преобразования.
# Минимальная ширина поля. Если *, значение берётся из кортежа.
# Точность, начинается с '.', затем - желаемая точность.
# Модификатор длины (опционально).
# Тип (см. таблицу выше).


# Флаги преобразования:
#
# Флаг	Значение
# "#"	Значение будет использовать альтернативную форму.
# "0"	Свободное место будет заполнено нулями.
# "-"	Свободное место будет заполнено пробелами справа.
# " "	Свободное место будет заполнено пробелами слева.
# "+"	Свободное место будет заполнено пробелами слева.

s = '%(lan)s has %(count)05d quote types'
# обращение к элементам словаря , для второго параметра указывается заполнение свободного места нклями
# и длина
print(s % {'lan': 'Python', 'count': 2})


s = '%.3s' # указываем точность в этом случае длину
print(s % 'Hello')

s = '%.*s' # указываем точность в этом случае длину, которая берется из кортежа
print(s % (4, 'Hello!'))

s = '\\'+'%-10d'+'\\'
print(s % 25)
s = '\\'+'%+10d'+'\\' # обязательный знак для чисел
print(s % 25)
s = '\\'+'% 10d'+'\\'
print(s % 25)


s = '\\'+'%010d'+'\\'
print(s % 25)

s = '\\'+'%-10.4f'+'\\'
print(s % 25)
s = '\\'+'% 10.4f'+'\\'
print(s % 25)
s = '\\'+'%+10.4f'+'\\'  # обязательный знак для чисел
print(s % 25)



# форматирование с использованием fromat
s = 'Hello? {}!'
print(s.format('Vasya'))

s = '{}, {}, {}'
print(s.format('a', 'b', 'c'))

s = '{0}, {1}, {2}'
print(s.format('a', 'b', 'c'))
# при этом
s = '{2}, {0}, {1}'
print(s.format('a', 'b', 'c'))
# так же можно передавать параметры извлечением из строки
print(*'abc')
s = '{2}, {1}, {0}'
print(s.format(*'abc'))

s = '{0}{1}{0}'
print(s.format('abra', 'cad'))

# можно передавать присваиванием именованным параметрам
s = 'My age is {age}, my height is {height}'
print(s.format(age=str(35), height='175 cm'))

# извлечение из словаря
myparams = {'age': str(35), 'height': '175 cm'}
print(type(myparams))
print(s.format(**myparams))


# Однако метод format умеет большее. Вот его синтаксис:
#
# поле замены     ::=  "{" [имя поля] ["!" преобразование] [":" спецификация] "}"
# имя поля        ::=  arg_name ("." имя атрибута | "[" индекс "]")*
# преобразование  ::=  "r" (внутреннее представление) | "s" (человеческое представление)
# спецификация    ::=  см. ниже

# спецификация ::=  [[fill]align][sign][#][0][width][,][.precision][type]
# заполнитель  ::=  символ кроме '{' или '}'
# выравнивание ::=  "<" | ">" | "=" | "^"
# знак         ::=  "+" | "-" | " "
# ширина       ::=  integer
# точность     ::=  integer
# тип          ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" |
#                   "n" | "o" | "s" | "x" | "X" | "%"
# Выравнивание производится при помощи символа-заполнителя. Доступны следующие варианты выравнивания:
#
# Флаг	Значение
# '<'	Символы-заполнители будут справа (выравнивание объекта по левому краю) (по умолчанию).
# '>'	выравнивание объекта по правому краю.
# '='	Заполнитель будет после знака, но перед цифрами. Работает только с числовыми типами.
# '^'	Выравнивание по центру.
# Опция "знак" используется только для чисел и может принимать следующие значения:
#
# Флаг	Значение
# '+'	Знак должен быть использован для всех чисел.
# '-'	'-' для отрицательных, ничего для положительных.
# 'Пробел'	'-' для отрицательных, пробел для положительных.
# Поле "тип" может принимать следующие значения:
#
# Тип	Значение
# 'd', 'i', 'u'	Десятичное число.
# 'o'	Число в восьмеричной системе счисления.
# 'x'	Число в шестнадцатеричной системе счисления (буквы в нижнем регистре).
# 'X'	Число в шестнадцатеричной системе счисления (буквы в верхнем регистре).
# 'e'	Число с плавающей точкой с экспонентой (экспонента в нижнем регистре).
# 'E'	Число с плавающей точкой с экспонентой (экспонента в верхнем регистре).
# 'f', 'F'	Число с плавающей точкой (обычный формат).
# 'g'	Число с плавающей точкой. с экспонентой (экспонента в нижнем регистре), если она меньше, чем -4 или точности, иначе обычный формат.
# 'G'	Число с плавающей точкой. с экспонентой (экспонента в верхнем регистре), если она меньше, чем -4 или точности, иначе обычный формат.
# 'c'	Символ (строка из одного символа или число - код символа).
# 's'	Строка.
# '%'	Число умножается на 100, отображается число с плавающей точкой, а за ним знак %.


# как подставить из кортежа так чтоли
coord = (3, 5)
print(type(coord))
s = 'X: {0[0]}; Y: {0[1]}'
print(s.format(coord))


# здесь используется преобразование
s = 'repr() shows quotes: {!r}; str() doesn`t:{!s}'
print(s.format('test1', 'test2'))

print('{:<30}'.format('Left align')+'endrow') # использование спецификации (после двоеточия) выравнивание по левому краю(<) длиной 30

# то же самое с заполнителем символом '.'
print('{:.<15}'.format('Left align'))

print('{:-<30}'.format('Left align'))
print('{:->30}'.format('Right align'))
print('{:-^30}'.format('Center align'))

print('{:*<+10.2f}; {:*>+10.3f}'.format(-3.14555, 3.145555)) # добавляем знак в спецификацию

print('{:*<+10f}; {:*>+10f}'.format(-3.14, 3.14)) # добавляем знак в спецификацию и число
print('{:*^+30.2f}'.format(3.1456))
print('{:*<+10d}; {:*>+10d}'.format(-3, 3))  # добавляем знак в спецификацию и число

# если надо вставить в разные места одно и то же значение то надо писать в шаблоне {0}
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))


p = 19.5
r = 22
print('{:_^ 20.2%}'.format(p/r))

print('aaa_{0}_bbb_{1}_ccc'.format('bbb', 'ddd'))

print('--{0}-->{1}-->{2}'.format('X', 'Y', 'Z'))
print('--{0}-->{0}-->{0}'.format('X', 'Y', 'Z'))
print('--{2}-->{1}-->{0}'.format('X', 'Y', 'Z'))

#именованные параметры
print('{nums}__{dels}__{smile}'.format(dels='XXX', smile='Mysmile', nums=15))

# параметры могут быть и именованными и порядковыми

print('{x} + {1}+{Y}+ = {0}'.format(2, 3, x=10, Y=17))


# параметры могут быть разных типов
a = list(range(3))
d = ([[1, 'a'], [2, 'b']])
c = set('aaaabbcd')

print('{list}; {dict}; {set}'.format(list=a, dict=d, set=c))

#можно обращаться не только к параметрам как спискам но и к отдельным элементам списка

print('{0} - {1}'.format('XYZ', [1, 2, 3]))
print('XYZ'[1])
print([1, 2, 3][1])
print('{0[0]} - {1[1]}'.format('XYZ', [1, 2, 3]))
# так же и для именованных
print('{SYMBOLS[0]} **** {LIST[1]}'.format(SYMBOLS='XYZ', LIST=[1, 2, 3]))

# как будет обстоять дело со словарями

print('{0[x]}-{1[0]}'.format({'x': 'XXX', 'y': 'YYY'}, [1, 2, 3]))


# из шаблона для format можно непосредственно обратиться к атрибутам объектов, но не к их методам.....
print(sys.version)
print(sys.platform)
print('My Python version:{0.version}\nMy operation system:{0.platform}'.format(sys))

print('|{:_<20} выравнивание по левому краю|'.format(200))
print('|{:_>20} выравнивание по правому краю|'.format(200))
print('|{:_=+20} выравнивание со вставкой перед числом но после его знака|'.format(200))
print('|{:_^20} выравнивание по центру|'.format(200))

# про точность

print('{:.4}'.format(51.256))
print('{:.4f}'.format(51.256))
print('{:.2f}'.format(51.256)) # точность для указанного типа f означает количество знаков после запятой, иначе просто длина строки что ли
print('{:.4}'.format('LongString'))

# точность для int нельзя использовать....будет ошибка


s = '''Коды формата для целых чисел:
... код "b": до {0}, после {0:b}
... код "c": до {0}, после {0:c}
... код "d": до {0}, после {0:d}
... код "o": до {0}, после {0:o}
... код "x": до {0}, после {0:x}
... код "X": до {0}, после {0:X}
... код "n": до {0}, после {0:n}
... код не указан: до {0}, после {0:}'''

print(s.format(10696))


# форматирование с использованием f- строк
print('F strings')
name = 'vasya'
age = 35
s =  F'My name is {name}, my age is {age}'
print(s)

print(f'My name is {name.capitalize().swapcase()}')


def to_lowercase(input):
    return input.lower()

print(f'My name is {to_lowercase(name)}')

v = 51.256/100

print(f'{v:*^ 50.2%}X')

dt = datetime.date(2020, 10, 4)
print(f'{dt:%d.%m.%Y}')








