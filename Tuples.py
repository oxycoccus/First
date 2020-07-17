import random

t = (1, 2, 'String')

l = [1, 2, 'String']

print(t)
print(t.__sizeof__())

print(l)
print(l.__sizeof__())


t = tuple()
print(t)

t = ('s')
print(type(t))
print(t)

t = ('s',)
print(type(t))
print(t)


t = (1)
print(type(t))
print(t)

t = (1,)
print(type(t))
print(t)

t = 's',
print(t)

t = tuple('MyString')
print(t)

t = tuple('My String'.split())
print(t)

print(t[0])

l = list(t)
print(l)
l.extend(['is', 'better'])
t = tuple(l)
print(t)

# Удобно использовать кортежи когда в функцию передается список, если не надо менять оригинал


def add_num(seq, num):
    newseq = list(seq)
    for _ in range(len(seq)):
        newseq[_] += str(num)
    return newseq


new_list = add_num(tuple(l), 10)
print(new_list)

# *********************************

tp = tuple([random.randrange(0, 5) for x in range(10)])
print(tp)

tp1 = tuple([random.randrange(-5, 0) for x in range(10)])
print(tp1)

tp2 = tp + tp1
print(tp2)
print(tp2.count(-1))
tp, tp1 = tp1, tp2