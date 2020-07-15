from itertools import zip_longest

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







