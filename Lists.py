from itertools import zip_longest
import copy

l = list('abcdefg')  # создание списка из итеррируемого объекта
print('List')
print(l)

l1 = []  # пустой список

l2 = ['s', 'p', ['isok'], 2]  # список созданный руками

print(l1)
print(l2)

# генератор списков
l = [_*5 for _ in 'list']
print(l)

# чуть сложнее c условием

l1 = [_*3 for _ in 'list' if _ != 'i']
print(l1)

# используем zip для распаковки двух списков
l2 = [a+b for a, b in zip('Start', 'Stop') if (a != 't') and (b != 't')]
print(l2)

# используем zip_longest из itertolls для формирования по длинному списку для распаковки двух списков
l2 = [str(a)+str(b) for a, b in zip_longest('Start', 'Stop')]
print(l2)


# но в более сложном случае воспользоваться просто циклом

l2 = []
for a in 'Start':
    for b in 'Stop':
        l2.append(a+b)
print(l2)


# формируем список проходом по всем элементам двух списков
l2 = [a+b for a in 'LISTIK' for b in '1234']
print(l2)


print('LIST'*5)
l = list('list')
print(l)


#Добавление в конец списка элемента
l.append('X')
print('Append X to the list:')
print(l)


#Расширение списка за счет другого списка
l.extend(l1)
print('Extend list by other iter:')
print(l)



# Вставка элемента на указанную позицию
l.insert(0, 'XXX')
l.insert(len(l), 'XXX')
print('Inserting elements in begin and end of list by index:')
print(l)

# удаление элемента по его значению иначе если нет такого тогда ошибка
l.remove('lll')
print('Delete element by value:')
print(l)

# Выборка элемента списка с его удалением из списка по индексу элемента (Режим очереди берется последний если не указан индекс)

print(l.pop(6))
print(l)

print(l.pop())
print(l)

l.append('s')
print(l)
# поиск индекса первого элемента со значением value
print('list.index(value): '+str(l.index('s', 0, len(l))))

# подсчет количества элементов в списке со значением value
print('list.count(value):', l.count('s'))


print('Sorting:')
a = [5, 9, 3, 1, 2, 7, 4, 8]
print(a)
# сортировка списка есть пара вариантов

# revers направление сортировки по возрастанию или по убыванию
a = sorted(a, reverse=0)
print(a)

a = [5, 9, 3, 1, 2, 7, 4, 8]
print(a)

a.sort(reverse=1)
print(a)


a = ['Duck', 'Apple', 'compare', 'CMD', 'dmx', 'apple']
print(a)

print(sorted(a, reverse=1))
print(sorted(a, reverse=0))
print('Сортировка не зависимо от регистра букв, используется указание функции сортировки через параметр key')
print(sorted(a, key=str.lower, reverse=1))
print(sorted(a, key=str.lower, reverse=0))

# Тоже самое применимо для встроеной функции sort списка, которая изменяет исходный список

a.sort(key=str.lower, reverse=1)
print(a)

a.sort(key=str.lower, reverse=0)
print(a)

print()
a = [5, 9, 3, 1, 2, 7, 4, 8]
print(a)

# разворот списка
a.sort()
a.reverse()
print(a)

#отчистка списка
a.clear()
a = [ _ for _ in range(10)]
a.reverse()
print(a)

# копирование списков


print('Copy lists')

a = [[1, 1, 1], [2, 2]]

b = a

print('a:', a)
print('b:', b)
a.append([3])
print('a:', a)
print('b:', b)
# Shadow copy
print('Shadow copy')
b = a.copy()
print('Add to a')
a.append([4])
print('a:', a)
print('b:', b)

print('Modify a[0][1]')
a[0][1] = 11
print('a:', a)
print('b:', b)

# Deep copy

print('Deep copy')
b = copy.deepcopy(a)

print('a:', a)
print('b:', b)
print('Modify a[0][1]')
a[0][1] = 0
print('a:', a)
print('b:', b)








