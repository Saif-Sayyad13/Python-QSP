# check the given no is positiove or negative (by user input)

'''num=eval(input("enter a number"))
if num>0:
    print(f"{num} is positive number")
'''
# wite a program to check the given no is negative  by using user input

'''num1 = eval(input(" enter a number"))
if num1<0:
    print(f"{num1} is negative no")'''
    
# if the reminder is 0 as a even number
# if the reminder is 1 we can call it as a odd number 

# write a program to check the given number is even
# regular method is with using % modules

'''a=4
if a%2==0:
    print(f' the given num {a} is even')

'''
# without using moduls % check the given no is even 
'''a=10
if(a//2)*2==a:
    print(f' the given num {a} is even')
'''
# write a program to checkthe given number is even  without using % and // symbols
'''a=10
if(a&1)==0:
    print(f'the given no {a} is even ')
'''
'''c=23
if(c&1)==1:
    print(f' The given number {c} is odd')
    
d=7
if d%2==1:
    print(f' the given num{d} is odd')
    
d1=13
if d%2!=0:
    print(f' the number {d1} is odd')'''
    
# want to check the given word is even length 
a="python"
if len(a)%2==0:
    print(f' The given words is {a} even length')
    
# write a program to check the given no is even convert to complex
x=100
if x%2==0:
    print(complex(x))
    
# wap to check given number is even store into the list

y=4
k=[]
if y%2==0:
    k.append(y)
    print(k)
# wap to check the given number is even store into the list (without using inbuild function)
s=40   #[40]
a=[]
if s%2==0:
    a=a+[s]   #----->[]=[]+[40]
    print(a)
