import decimal

print(decimal.getcontext())

myd = decimal.Decimal("1.65")
myfloat = 2.675
my1d = decimal.Decimal(myfloat)
my1d = decimal.Decimal("2.675")


print(myd)
print(my1d)


myd = myd.quantize(decimal.Decimal("1.0"))
my1d = my1d.quantize(decimal.Decimal("1.00"))

print("Rounding")
print(myd)
print(my1d)


decimal.getcontext().prec = 2
print(decimal.getcontext())
myd = decimal.Decimal("1.23")+decimal.Decimal("2.32")
print(myd)
decimal.getcontext().rounding = decimal.ROUND_05UP
myd = decimal.Decimal("1.23")+decimal.Decimal("2.32")
print(myd)


