# Tuple is combination of homogenous and hetrogenous element
#Tuple is immutable
# tuple support duplicate char
# in tuple  () are not madatonay if you skip it will assume that it is butcomma is madatonay 
# how to print empty tuple
a=()
print(type(a))
tuple() #with object
print(tuple)
a=(100) # here if you dont add commait will act like a interger for make tuple its mad to add comma(,)
print(type(a))
a=(100,)
print(type(a))
a=('a','b','c')
print(type(a))

b=1,2,3,4,5,6 # homogenouse tuple
print(b)
c=1,2,3,'aman',"@","yo yo","$" # hetrogenouse tuple
print(c)
print(c.index("aman"))  # only two methods index
print(c.count("aman")) # count


# very very very important interview question
# we can not modify tuple directely because ther ei\are only two methods and they are justv to get index and count
# but we can modify it using indirect methods eg
s=(1,2,3,"Aman","@")
s[3]
print(s[3].upper())
s[4]
print(s[4].replace("@","$"))
print(s)
# this is just normal modofication

# now let me show you how to change permentanly
l=(1,2,3,"aman","rohit",[100,200,300],{25,50})
print(l)
l[5]
l[5][0]=69
print(l)

