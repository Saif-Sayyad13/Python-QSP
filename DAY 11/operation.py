print("Good morning")
print("Hello, good morning")
print("How are you?")

print("Good morning", end = ' ')
print("Hello, good morning\n", end = ' ')
print("How are you?", end = '')

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep = "*")
print("Hello, good morning", sep = "#")
print(1, 4, 7, "hi", 56, sep = "%")
print(1, 4, 7, [1,2], 56, sep = "%")
print("hi", "Hello, good morning", sep = "#")



# Arithmetic Operators:
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Addition of two number is:", num1 + num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Subtraction of two number is:", num1 - num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Multiplication of two number is:", num1 * num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Division of two number is:", num1 / num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Floor Division of two number is:", num1 // num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Remainder of two number is:", num1 % num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Power of two number is:", num1 ** num2)





# Relational Operators:
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print(num1 == num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print(num1 != num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print(num1 > num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print(num1 < num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print(num1 >= num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print(num1 <= num2)






# Logical Operators
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Logical and:", num1 and num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Logical or:", num1 or num2)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Logical not:", not num1)
print("Logical not:", not num2)

num1 = int(input("Enter the number:"))
print(not num1)





# Assignment Operator
a = 10
print(a)
a = 10 + 10
print(a)
a += 20
print(a)
a *= 2
print(a)    
a /= 2
print(a)
a //= 2
print(a)
a %= 2
print(a)    
a **= 2
print(a)
a -= 10
print(a)





# Bitwise Operator
a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
print("Bitwise AND: ", a & b)

a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
print("Bitwise or: ", a | b)

a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
print("Bitwise xor: ", a ^ b)

a = int(input("Enter number:"))
print("Bitwise not: ", ~ a)

a = int(input("Enter the number:"))
b = int(input("Enter shift value:"))
print("Right shift: ", a >> b)

a = int(input("Enter the number:"))
b = int(input("Enter shift value:"))
print("Left shift: ", a << b)






# Membership Operator
a = int(input("Enter the value:"))
b = eval(input("Enter tuple data:"))
print(a in b)

a = int(input("Enter the value:"))
b = eval(input("Enter tuple data:"))
print(a not in b)





# Identity Operator
a = [10,20]
b = a
print(a is b)

a = [10,20]
b = a.copy()
print(a is b)