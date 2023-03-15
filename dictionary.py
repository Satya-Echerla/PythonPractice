dict = {1:"srinu",2:"raj",3:'ravi',4:'ram'}
print(dict)

print(dict.keys())
print(dict.items())

k = dict.keys()
for i in k:
    print(i)

m = dict.values()
for i in m:
    print(i)

print(dict[2])

del dict[4]
print(dict)