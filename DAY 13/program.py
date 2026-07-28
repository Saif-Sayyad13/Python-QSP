'''
# wap to check the given data type is string
a='morning'
if type(a)==str:
    print("string data type ")
    
b=[1,2,3]
if type (b)==list:
    print(" it is a list data type")
# or
b1=[1,2,3]
if isinstance (b1, list):
    print(' its is a list data type')
    
# Syntax 
# isinstance(var_name,(data1,data2,data3,.....))
c=eval(input('Enter a data type'))
if isinstance(c,(str,tuple,list)):
    print("Sequence data type")

#or
d=eval(input('enter the data type'))
if type (d) in (str,tuple,list):
    print("sequence data type")

'''
# wap to check the given word is palindrome
# palindrome means from both side forward and backward its meaning should be same 

'''x="MOM"
if x ==x[::-1]:
    print("it is a palindrome")

y=eval(input("enter the data"))
if y==y[::-1]:
    print("it is a palindrome")'''
    
    
'''# To checl the number is palindrome or not 
x=121
y=str(x) # y=str(121)
if y==y[::-1]:
    print("Palidrome number")
    '''
    
'''# to check a number is palindrome without using type casting
# here we can only check for 3 number 
# to check firsrt no use //100
# to check last number use %10
# to check last 2 number use %100
x=121
if(x//100)==x%10:
    print("it is a palindrome")'''
    
'''# wap to check the number is divisibele by 2 and 6
X=12
if x%2==0 and x%6==0:
    print(' dividible by 2 and 6 number')
    '''
'''x=[11,12,13,14]
key=12
if key in x:
    print("key is part ")
    
q="python"
n="n"
if n in q:
    print("is a part")

'''
'''
y='good luck'
if y.endswith('k'):
    print("its endswith k char")
'''

# wap to check leap year
y=2024
if y%4==0:
    print("it is leap year")
    
