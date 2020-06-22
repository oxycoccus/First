
import math


x = 5
y = 2

i = x + y
print(i)

i = x - y
print(i)

i = x * y
print(i)

i = x / y
print(i)

i = x ** y # возвдение в степень
print(i)

i = x // y # целое от деления
print(i)

xx = x % y # остаток от деления
print(xx)


print(divmod(x, y))

print(' или ', x | y)
print(' исключающее или ', x ^ y)
print(' и ', x & y)
print('сдвиг << ', x << y)
print(' сдвиг >> ', x >> y)
print(' инверсия битов ', ~x)

n = -37
print(bin(n))
print(hex(n))
print(oct(n))
print(int.bit_length(n)) # длина необходимая для хранения цеолого числа без знака и лидирующих нулей

f = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
print(f)
f = 14.589
print(f.as_integer_ratio())
print(f.is_integer())
hexstr = f.hex()
print(hexstr)

print(float.fromhex(hexstr))

f = 16
print(math.sqrt(f))
print(math.pi)
f = 14.589
print(type(math.modf(f)))
print(math.modf(f))

n = 315

print(sum([ int(_) for _ in list(str(n)[:2])]))