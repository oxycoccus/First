import random
import math
import statistics



def trunc(v):
    return int(v * 1000) / 1000


def trunc_II(v, upp):
    upp = 10 ** upp
    return int(v*upp) / upp


def round_up(v, upp=0):
    upp = 10 ** upp
    return math.ceil(v*upp)/upp


def round_down(v, upp=0):
    upp = 10 ** upp
    return math.floor(v*upp) / upp


def round_half_up(v, upp=0):
    upp = 10 ** upp
    return math.floor(v*upp + 0.5) / upp


def round_half_down(v, upp=0):
    upp = 10 ** upp
    return math.ceil(v * upp - 0.5) / upp


def round_half_away_from_zero(v, upp=0):
    vabs = round_half_up(abs(v), upp)
    return math.copysign(vabs, v)



actual_money, truncated_money = 100, 100

random.seed()

for _ in range(100000):
    rmvalue = random.uniform(-0.05, 0.05)
    actual_money = actual_money + rmvalue
    truncated_money = trunc(truncated_money + rmvalue)

print('Actual money ', actual_money)
print('Truncated money ', truncated_money)


print('in --- int  ---  ceil --- floor --- half_up --- half_down')
print('12.5 ---', trunc_II(12.5, 0), '---', round_up(12.5, 0), '---', round_down(12.5, 0), '---', round_half_up(12.5, 0), '---', round_half_down(12.5, 0), '---', round_half_away_from_zero(12.5, 0))
print('-5.87 ---', trunc_II(-5.87, 1), '---', round_up(-5.87, 1), '---', round_down(-5.87, 1), '---', round_half_up(-5.87, 1), '---', round_half_down(-5.87, 1), '---', round_half_away_from_zero(-5.87, 1))
print('1.625---', trunc_II(1.625, 2), '---', round_up(1.625, 2), '---', round_down(1.625, 2), '---', round_half_up(1.625, 2), '---', round_half_down(1.625, 2), '---', round_half_away_from_zero(1.625, 2))
print('-127.4 ---', trunc_II(-127.4, -1), '---', round_up(-127.4, -1), '---', round_down(-127.4, -1), '---', round_half_up(-127.4, -1), '---', round_half_down(-127.4, -1), '---', round_half_away_from_zero(-127.4, -1))
print('127.9 ---', trunc_II(127.9, -1), '---', round_up(127.9, -1), '---', round_down(127.9, -1), '---', round_half_up(127.9, -1), '---', round_half_down(127.9, -1), '---', round_half_away_from_zero(127.9, -1))

data = [1.25, -2.67, 0.43, -1.79, 4.32, -8.19]

avg_income = statistics.mean(data)
print(avg_income)

ru_data = [round_up(v, 1) for v in data]
rd_data = [round_down(v, 1) for v in data]
tr_data = [trunc_II(v, 1) for v in data]
half_up_data = [round_half_up(v, 1) for v in data]
half_down_data = [round_down(v, 1) for v in data]
half_az = [round_half_away_from_zero(v, 1) for v in data]

print(data)
print(ru_data)
avg_ru = statistics.mean(ru_data)
print(avg_ru)

print(rd_data)
avg_rd = statistics.mean(rd_data)
print(avg_rd)

print(tr_data)
avg_tr = statistics.mean(tr_data)
print(avg_tr)

print(half_up_data)
avg_half_up = statistics.mean(half_up_data)
print(avg_half_up)

print(half_down_data)
avg_half_down = statistics.mean(half_down_data)
print(avg_half_down)

print(half_az)
avg_az = statistics.mean(half_az)
print(avg_az)

print('up ', avg_income-avg_ru)
print('down ', avg_income-avg_rd)
print('trunc ', avg_income-avg_tr)
print('half_up ', avg_income-avg_half_up)
print('half_down ', avg_income-avg_half_down)
print('half_az ', avg_income-avg_half_down)

data = [-2.15, 1.45, 4.35, -12.75]

print(data)
print(statistics.mean(data))

rhudata = [round_half_up(v, 1) for v in data]
print(rhudata)
print(statistics.mean(rhudata))

rhddata = [round_half_down(v, 1) for v in data]
print(rhddata)
print(statistics.mean(rhddata))

rhazdata = [round_half_away_from_zero(v, 1) for v in data]
print(rhazdata)
print(statistics.mean(rhazdata))

