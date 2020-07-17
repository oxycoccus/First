s = "MyString"
print(s[0])
print(s[-1])
print(s[2:])
print(s[2:-1])
print(s[2::2])
print(s[::-1])
print(s[2:6:-1])

l = list(s)
l.reverse()
s = ''.join(l)

print(s)

s = s[::-1]
print(s)



l.reverse()
print(l)

print(l[5])
print(l[-1])
print(l[2:])
print(l[2:-1])
print(l[2::2])
print(l[::-1])
print(l[2:6:-1])

print(l)
print('Изменение изменяемых последовательностей используя срез')

#так изменяются элементы
l[:2] = ['X', 'X']

# а вот так изменется и добавляется еще один

l[:1] = ['Y', 'Y', 'Y']
print(l)

# удаление из последовательности посредством среза
del l[:4]
print(l)

# здесь выдаст ошибку ибо строка не изменяемая последовательность
# del s[:2]
# print(s)