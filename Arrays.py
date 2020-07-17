from array import *


myarray = array('i', [1, 2, 3, 4])

for i in myarray:
    print(i)

print(myarray[0])
myarray.append(89)
print(myarray)
myarray.insert(0, 89)
print(myarray)

narray = array('i', [100, 100])

myarray.extend(narray)
print(myarray)

l = [555, 555, 555]

myarray.fromlist(l)

print(myarray)

myarray.remove(555)
myarray.remove(555)

print(myarray)

print(myarray.pop())
print(myarray)

print(myarray.index(89))

myarray.reverse()
print(myarray)

print(myarray.buffer_info())

print(myarray.count(100))

print(myarray.tostring())

l = myarray.tolist()
print(l)