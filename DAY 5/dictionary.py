'''#How to create empty dictionary in normal way
a={ }
print(a)
#How to create empty dictionary by using object 
dict()
print(dict()) # here if we dont add inside() this will print class dict


#In dictionary data type in key part always we have to pass 
#single_value_datatype and immutable data type

# single_value data type —- int/float/complex/boolean
# immutable data type—-string/tuple 

#Note —-In key part if we pass mutable data type it will show unhashable type of error 

# Note 2—- In Value Part you can Pass any Python Data type

a={1:10,False:True,3.4:"abc",2+4j:100,"Hii":"Hello",(1,2,3):900}
print(a)
s={1:[1,2,3],5.5:{12,34,65},False:{13:90},1111:"HI",900:(1,2,87)}
print(s)

e={1:2,2:3,3:4,4:5} 
print(len(e)) # it will always conside in pair 
print(e[1]) # here 1 is key not any index no  # ans 2
# here print(e[0]) it will show erroe KeyError: 0
print(e[4]) # ans 5
print(e.get(4)) 
print(e.get(45678))
print(e.get(45678,"key is not present "))
print(e.setdefault(4))
print(e.setdefault(1234,"no such thing is here"))
print(e)


ee={1:1000,True:200,30:45,30:1000}
print(ee)
eee={1:1000,True:200,30:45,50:1000}
print(eee)
bb={1:2,1:3,1:0.5} # in kay part we have to pass unique element if we pass dulpicate it will consider lates one
print(bb)

bbb={10:100,20:100,30:100}
print(bbb)

a={1:100,2:200,3:300,4:400}
print(a[1])
#print(dir(dict))
#clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
a.update({5:500,6:600})
print(a)
a.popitem()
print(a)
a.pop(2)
print(a)
#// use all the methods of dictionary and try to understand how it works

a.values() # only values will be printed
print(a.values())
a.keys() # only keys will be printed
print(a.keys())
a.items() # only key-value pairs will be printed
print(a.items())
a.clear() # it will clear all the data from dictionary
print(a)
'''
a={1:100,2:200,3:300,4:400}
b=a.copy() # create a shallow copy of a
print(b)
print(a)
print(id(a))
print(id(b))
a.update({5:500,6:600})# update the original dictionary
print(a)
print(b)
aa={1:100,2:200,3:300,4:400}# create a new dictionary
bb=aa# create a reference to the original dictionary
print(bb)
print(id(bb))# print the id of the reference
print(id(aa))# print the id of the original dictionary
aa.update({5:500,6:600})# update the original dictionary
print(aa)
print(bb) # print the reference dictionary  
c={**a,**b} # merge two dictionaries
print(c)
s={1:100,2:200,3:300,4:400}
s1={5:500,6:600,7:700}
s3={**s,**s1} # update the original dictionary with the new dictionary
print(s3)
dict.fromkeys(s3) # create a new dictionary with the keys from the original dictionary  