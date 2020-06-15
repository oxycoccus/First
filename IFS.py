i = int(input("Введите число: "))
if i < 0:
    print("less zero")
elif i > 10:
    print("More ten")
else:
    print("More zero")


# short

print("More zero") if i > 0 else print("Less zero")
