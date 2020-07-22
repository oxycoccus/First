from itertools import chain
a = {}
print('type of a {}', type(a))
print(a)

a = {1, }
print('type of a {1,}', type(a))
print(a)

a = {1}
print('type of a {1,}', type(a))
print(a)



a = {'hello', 'goodbye'}
print(a)


a = set('hello')
print(a)

ls = ['1', '2', '1', '3']

a = {x for x in ls}
print(a)

tpl = ('3', '2', '5', '3')

a = {x for x in tpl}
print(a)


ls = ['hello', 'word', 'hello', 'type', 'main']
a = {*ls}
print(a)

a = set(a)
print(a)

dct = {'hello' :'1', 'goodbye': '2', 'hello': '2'}
a = {**dct}
print(type(a))
print(a)


a = {k for k in chain(dct.keys(), dct.values())}
print(type(a))
print(a)

a = set(ls)
print(a)

print('len set', len(a))

print('Принадлежность множеству')
print('hello' in a)

b = set([1, 2, 3])
c = {x+1 for x in range(10)}
# принадлежность элементов другому множеству

print(a.isdisjoint(b)) # true если не имеют общих элементов

print(c)
print(b)
print('isdisjoint b and c', c.isdisjoint(b))
print('issubset b of c', b.issubset(c))
print('аналогия issubset b of c b <= c', b <= c)
print('b==c', b == c)
print('b == {1,2,3}', b == {1, 2, 3}, 'все элементы множества принадлежат элементам другого множества и наоборот')
print('issuperset c of b', c.issuperset(b))
print('аналогия issuperset c of  c >= b', c >= b)
print('union sets')
print(b.union(a))
print(a | c)
print('пересечение множеств')
print(c.intersection(b))
a.update([1, 3])
print(b & c & a)

print('различие между множествами')
print(c.difference(b, a))
print(a-c)
print('уникальные значения из обои множеств')
print(a.symmetric_difference(c))
print(a ^ c)
print(a ^ c ^ b)

print('операции с множествами')

print('update')
a.update((9, 10))
print(a)
print('a |= other | ...')
a |= {99, 100} | c
print(a)

a = set(ls)
print('a')
print(a)
print('b')
print(b)
print('c')
print(c)

print('обновление множества пересечением')
cc = c.copy()
cc.intersection_update(b)
print('c.intersection_update(b)')
print(cc)
cc = c.copy()
cc &= b
print('cc &= b &...&...')
print(cc)

print('обновление множества разностью(вычитанием)')
cc = c.copy()
cc.difference_update(b)
print('c.difference_update(b)')
print(cc)
cc = c.copy()
cc -= b
print('cc -= b |...|...')
print(cc)


print('обновление множества уникальными элементами из нескольких')
cc = c.copy()
cc.symmetric_difference_update(a)
print('c.symmetric_difference_update(a)')
print(cc)
cc = c.copy()
cc ^= a
print('cc -= b ^...^...')
print(cc)


print('добавление элемента add')
print(a)
a.add('mine')
print(a)

print('удаление элемнта remove, если элемента нет то выдает ошибку KeyError')
print(a)
a.remove('type')
print(a)

print('удаление элемнта discard, если элемента нет то ошибки не будет')
print(a)
a.discard('main')
a.discard('type')
print(a)

print('pop')
print(a.pop())
print(a)

print(a.pop())
print(a)

print('frozenset то же что и set но не изменяемое')

s = set('qwerty')
print(s)

fs = frozenset('qwerty')
print(fs)

print(s - fs)
print(s & fs)
print(s ^ fs)
print(b <= c)


