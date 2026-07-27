# string formatting
# 3 types 1 and 2 are old method but 3 is v.v.v.imp
# 1. formatting with placeholder (%)
# %s string
# %d integer
# %f float
# %.2f here we had written 2 because we only want 2 digit after decimal

s=" My name is %s and my age is %d"%("Aman", 22)
print(s)

#2. .format method{}
a="My name is {} and my age is {}".format("Don",23)
print(a)


b="My name is {1} and my age is {0}".format("Don",23)
print(b)

# 3. formatting with f-literals 
#{}
# inside the { } we have to pass variable name
# before the quotes we have to mention either F/f 

name="Joy"
age=25
msg=f" my name is {name} and my current age is {age}"
print(msg)



