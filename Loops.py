i = int(input("Введите число: "))
j = i
while i > 0:
    print(i*2, " ")
    i -= 1

print("")

for i in range(j): # если используем range то берется от нуля до j
    print(i, end='')

print("")


for i in "Hello world":
    if i == "l":
        continue
    print(i, end='')

print('')

for i in "Mine world":
    if i == 'o':
        break
    print(i, end='')

print('')

for i in 'Mine world':
    if i == 'x':
        break
else:
    print("No letter X in string")  # выполняется если цикл пройден полностью и не прервался через break



