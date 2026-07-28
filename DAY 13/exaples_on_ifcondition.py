'''#1. Check Positive Number
a=eval(input("Enter a posititve number"))
if a >0:
    print("Number is Positive")
    
#2. Check Negative Numbe
a=eval(input("Enter a Negative number"))
if a <0:
    print("Number is Negatiive")
    
#3. Check Zero
a=eval(input("Enter Zero number"))
if a==0:
    print('Number is Zero')
    
#4. Eligible to Vote
a=eval(input("Enter you age"))
if a>=18:
    print("You are eliglible for voting")
    
#5. Driving License
a=eval(input('enter your age'))
if a>=18:
    print("You can have your driving license")
    
#6. Pass Student
a=eval(input('Enter your marks'))
if a>=35:
    print("you are pass in the exam")
    
#7. Salary Eligible
a=eval(input('Enter your age '))
b=eval(input('enter your salary'))
if a>=21 and b>=10000:
    print("you are eligible for salary")
    
#8. Adult Person
a=eval(input("enter you age"))
if a>=18:
    print('You are good Aduult Person')
   ''' 
'''#9. Temperature Check
a=eval(input("enter Temperature in only digit form if its above 24 then only good"))
if a>=24:
    print("good Day")
    '''
'''#10. ATM Balance
a=eval(input('enter a amount '))
if a>0:
    print("You have paisa")
    '''
'''#11. Even Number
a=eval(input("Enter a even number"))
if a%2==0:
    print(f'Number is even {a}')
    
# another method - using floor division
a=eval(input("Enter a no"))
if (a//2)*2 == a:
    print("a")
    
# another method - using bitwise and (&)
a = eval(input("Enter number: "))
if a & 1 == 0:
    print("Evan Number!")
'''
#12. Odd Number
a=eval(input("Enter a odd number"))
