# in set data type we cant create normal way to show emppty set beacuse if we create it will act like a dict
a=set()
a={1,2}
print(type(a))

e={1,2.2,3+4j,False,"hi",(1,2)} # immutable ,unorderd, 
print(e)
print(len(e))

t={0,False,True,1,8,8,12}
print(t) 
print(len(t)) # here the output will be 4 because it wont support duplicates so 0 is false ,true is 1 2 time 8 consider 1

