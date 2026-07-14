# normal copy
a=[1,2,3]
b=a
print(a)
print(b)
print(id(a))
print(id(b))

# shallow copy
c=[10,20,30,[11,22,33]]
d=c
print(c)
print(d)
print(id(c))
print(id(d))
print(id(c[3]))
print(id(d[3]))

