'''# how to create an empyt list in normalway
a=[]
print(a)
# how to create empty list by using object 
b=list()
print(list())
type(a)
print(type)

# list data type is order data type
s=[1,2,3,4,5]
print(s)
len(s)
print(len(s))

# list support duplicate elements 
x=[1,2,3,1,2,3,1,2,3,'a','b','a']
print(x)

# in list data we can do indexing and slicing 
e=[100,89.4,True,"welcome","walmart","goodluck",12]
print(e[-4])
print(e[-6])
print(e[6])
e[3]=100
print(e)
e[2]=False
print(e)
print(dir(list))

# first methods append()
# first we will add single value data type
x=[]
print(x)
x.append(10)
print(x)
x.append(13.13)
print(x)
x.append(1+2j)
print(x)
x.append(False)
print(x)
x.append("Python")
print(x)
x.append((23,234))
print(x)
x.append([1,2,3])
print(x)
x.append({500,9000})
print(x)
x.append({23:45})
print(x)
'''
# in append methods error
'''x.append()
x.append(12,12,1345)'''


# extend()













# insert()
# syntax var_name.insert(position/location,value)
ss=[1,2,3,4]
ss.insert(0,100)
print(ss)
ss.insert(4,"Python")
print(ss)




# pop()
# in pop amd remove we cant delete multipe methods it will delete oone by one 
ss.pop()
print(ss)
ss.pop(1)
print(ss)



#remove()
ss.remove(2)
print(ss)

#clear
ss.clear
print(ss)

print(ss)


#del 
del ss
print(ss)
# here it will show erro because it will delete complete from memory location also