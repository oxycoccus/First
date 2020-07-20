try:
    k = 1/0
except:
    k = 0
print(k)


try:
    k = 1/0
except ZeroDivisionError:
    k = 0
print(k)

try:
    k = 1/0
except Exception:
    print(Exception)
    k = 0


try:
    k = 1/0
except ZeroDivisionError:
    print('Divicsion by zero - Error!!!!')
    k =0

try:
    k = 1/'0'
except ZeroDivisionError:
    print('Division by zero!')
    k = 0
except:
    print('Other Exception')
    k = 0

try:
    k = 1/'0'
except Exception as e:
    print('Exception:', e.__class__.__name__)
    k = 0
finally:
    print('It will run anyway')

try:
    k = 1/2
except Exception as e:
    print('Exception:', e.__class__.__name__)
    k = 0
else:
    print('Cong. no exceptions')
finally:
    print('It will run anyway')












