
s = 'Strin"g'
s1 = "strin'g"

s2 = s1 + '\n' + s # перевод на новую строку
print(s2)

s2 = s1 + '\a' + s # звонок какой-то на принтере
print(s2)

s2 = s1 + '\b' + s # backspace
print(s2)


s2 = s1 + '\f' + s # перевод страницы
print(s2)

s2 = s1 + '\r' + s # возврат каретки
print(s2)


s2 = s1 + '\t' + s # горизонтальная табуляция
print(s2)

s2 = s1 + '\v' + s # вертикальная табуляция
print(s2)

s = r"C:\nex.txt" # символ r в любом регистре отключает экранирование
print(s)


# s = r"C:\n\" сырая строка подавляющая экранирование не может заканчиваться на \
# print(s)  поэтому

s = r"C:\new.txt\\"[:-1]
print(s)

s = r"c:\new.txt"+"\\"
print(s)

s = "C:\\new.txt\\"


slong = '''это очень большой 
......многострочный текст
прям много строк, используй тройные кавычки!'''
print(slong)

print('concat: '+s1 +' ' + s)

print('дублирование строки: '+s1 * 3)

print('длина строки: '+str(len(slong)))

print('доступ к эелентам строки по индексу:', s[1])
print('доступ к эелентам строки по индексу:', s[-1])

print('срез строки:', s[3:-1])
print('срез строки:', s[2:])
print('срез строки:', s[:])

print('срез строки с шагом:', s[3:-1:2])


# начало и конец диапазона можно указывать числом со знаком минус,
# но не всегда попадает в диапазон при поиске одного символа

print('поиск подстроки (первое вхождение):', slong.find('!', 0, len(
    slong)))

print('поиск подстроки (последнее вхождение):', slong.rfind('тр', 0, len(slong)))

print(slong)
# поиск подстроки , но возвращаемое значение не -1 в случае если не найдено
k = slong.index('много', 0, len(slong))
print(k)

print('Результат str.index:', print(slong.index('много', 0, len(slong)))) # какой-то странный вывод получается

k = slong.rindex('тр', 0, len(slong))
print(k)

print('Результат str.index:', print(slong.rindex('тр', 0, len(slong)))) # какой-то странный вывод получается

print('Результат replace:', slong.replace('о', 'А'))

# разбитие строки по символу(ам)
print('Рузельтат split:', slong.split(','))
print('Рузельтат split:', type(slong.split(',')))

print(slong.split('р'))
print(slong.split())# здесь получилось разбитие по словам

print(list(s)) #разбитие по буквам


def stringanalize(s: str):
    print()
    print('Analize ', s)
    print('isdigit:', s.isdigit())
    print('isalpha:', s.isalpha())
    print('isalnum:', s.isalnum())
    print('islower:', s.islower())
    print('isupper:', s.isupper())
    print('isspace', s.isspace())
    print('isascii', s.isascii())
    print('isdecimal', s.isdecimal())
    print('istitle', s.istitle())
    print('isnumeric', s.isnumeric())
    print('isprintable', s.isprintable())
    print('startwith', s.startswith('12'))
    print('endwith', s.endswith('5'))
    print('count', s.count('s', 0, len(s)))


s = '12.5555'
stringanalize(s)

s = 'ASDA'
stringanalize(s)

s = 'asds'

stringanalize(s)


def stringmodify(s: str):
    print();
    print('String modify :', s)
    print('Upper: ', s.upper())
    print('Lower: ', s.lower())
    print('Capitalize:', s.strip().capitalize())
    print('SwapCase:', s.swapcase())
    print('Title:', s.upper().title()) # каждое слово с большой буквы остальные буквы маленькие
    print(s.center(20, '*')+s.center(20, '*'))
    print('ljust:', s.strip().ljust(10, '-'))
    print('rjust', s.strip().rjust(10, '-'))
    print('lstrip:' + '\\'+s.lstrip()+'\\')
    print('rstrip:', '\\'+s.rstrip()+'\\')
    print('strip:', '\\'+s.strip()+'\\')
    print('zfill:', s.zfill(20)) # строка длиной не менее заданной и начало заполняется нулями




s = '   asDF   '

stringmodify(s)


s = 'Мой шаблон новый шаблон'
print('s.partition')
print(type(s.partition('шаблон')))
print(s.partition('шаблон'))

print(s.partition('шблон'))
print('s.rpartition')
print(s.rpartition('шаблон'))




