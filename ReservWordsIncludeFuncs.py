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


str = 'cat-кот'
print('Result func ascii(x) - ', ascii(str))


i = 248
print('Result func bin(x) - ', bin(i))
