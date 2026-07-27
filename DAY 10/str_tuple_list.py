# Practice Data Types in Python
# default values of data types in python are:

print(int())
print(float())
print(complex())
print(bool())
print(str())
print(list())
print(tuple())
print(set())
print(dict())


# Integer conversion
num1=10
print(int(num1))
print(float(num1))
print(complex(num1))
print(bool(num1))
print(str(num1))

# Float conversion
num2=10.5
print(int(num2))
print(float(num2))
print(complex(num2))
print(bool(num2))
print(str(num2))

# Complex conversion
num3=10+5j
# print(int(num3)) this will give error because complex number cannot be converted to int but we can convert complex number to float by taking the real part of the complex number
#print(float(num3.real))
print(complex(num3))
print(bool(num3))
print(str(num3))

# Boolean conversion
num4=True
print(int(num4))
print(float(num4))
print(complex(num4))
print(bool(num4))
print(str(num4))

# String conversion
num5="10"  # here we can convert any number  string to int, float, complex, bool, list, tuple, set but we cannot convert string to dict because dict requires key-value pairs but we cant not convert any combination string into single value data type like int, float, complex, bool, list, tuple, set but we can convert string to dict if the string is in the format of key-value pairs like '{"key1": "value1", "key2": "value2"}' but we cannot convert string to dict if the string is in the format of single value like '10' or '10.5' or '10+5j' or 'True' or 'False' or 'None' or '[]' or '()' or '{}' or 'set()' or 'dict()' or any other combination of these.
print(int(num5))
print(float(num5))
print(complex(num5))
print(bool(num5))
print(str(num5))
print(list(num5))
print(tuple(num5))
print(set(num5))

#tuple conversion
num6=(1,2,3)
print(list(num6))
print(tuple(num6))
print(set(num6))

#list conversion
num7=[1,2,3]
print(list(num7))
print(tuple(num7))
print(set(num7))

#set conversion
num8={1,2,3}
print(list(num8))
print(tuple(num8))
print(set(num8))

#dict conversion
num9={"key1 10": "value1 100", "key2": "value2"} #  here in the key we have combined string and number in the output of dict conversion we will get the key as string and value as string because in python dict keys are always strings and values can be any data type but in this case we have combined string and number in the key so the output will be string and in the value we have combined string and number so the output will be string.
print(str(num9))
print(list(num9))
print(tuple(num9))
print(set(num9))
print(dict(num9))


#Sting all 30 methods in python with example
#1.upper() method is used to convert all the characters in the string to uppercase.
#syntax: string.upper()
str1="hello world"
print(str1.upper()) # output: HELLO WORLD

#2.lower() method is used to convert all the characters in the string to lowercase.
#syntax: string.lower()
print(str1.lower()) # output: hello world

#3.swapcase() method is used to convert all the uppercase characters in the string to lowercase and all the lowercase characters in the string to uppercase.
#syntax: string.swapcase()
str2="Hello World"
print(str2.swapcase()) # output: hELLO wORLD

#4.capitalize() method is used to convert the first character of the string to uppercase and all other characters to lowercase.
#syntax: string.capitalize()
str3="hello world"
print(str3.capitalize()) # output: Hello world

#5.title() method is used to convert the first character of each word in the string to uppercase and all other characters to lowercase.
#syntax: string.title()
str4="hello world"
print(str4.title()) # output: Hello World

#6.count() method is used to count the number of occurrences of a substring in the string.
#syntax: string.count(substring)
str5="hello world"
print(str5.count("o")) # output: 2

#7.find() method is used to find the index of the first occurrence of the substring in the string. If the substring is not found, it returns -1.
#syntax: string.find(substring)
str6="hello world"
print(str6.find("o")) # output: 4

#9.rfind() method is similar to find() method but it returns the highest index of the substring if found in the string otherwise it returns -1.
#syntax: string.rfind(substring)
str7="hello world"
print(str7.rfind("o")) # output: 7

#10.index() method is similar to find() method but it raises ValueError if the substring is not found in the string.
#syntax: string.index(substring)
str8="hello world"
print(str8.index("o")) # output: 4

#11.rindex() method is similar to rfind() method but it raises ValueError if the substring is not found in the string.
#syntax: string.rindex(substring)
str9="hello world"
print(str9.rindex("o")) # output: 7

# boolean methods in python it returns True or False (12 to 22)
#12.startswith() method is used to check if the string starts with the specified substring. It returns True if the string starts with the substring, otherwise it returns False.
#syntax: string.startswith(substring)
str10="hello world"
print(str10.startswith("hello")) # output: True

#13.endswith() method is used to check if the string ends with the specified substring. It returns True if the string ends with the substring, otherwise it returns False.
#syntax: string.endswith(substring)
str11="hello world"
print(str11.endswith("world")) # output: True

#14.isalpha() method is used to check if all the characters in the string are alphabetic. It returns True if all the characters are alphabetic, otherwise it returns False.
#syntax: string.isalpha()
str12="hello"
print(str12.isalpha()) # output: True

#15.isdigit() method is used to check if all the characters in the string are digits. It returns True if all the characters are digits, otherwise it returns False.
#syntax: string.isdigit()
str13="12345"
print(str13.isdigit()) # output: True

#16.isalnum() method is used to check if all the characters in the string are alphanumeric. It returns True if all the characters are alphanumeric, otherwise it returns False.
#syntax: string.isalnum()
str14="hello123"
print(str14.isalnum()) # output: True

#17.islower() method is used to check if all the characters in the string are lowercase. It returns True if all the characters are lowercase, otherwise it returns False.
#syntax: string.islower()
str15="hello"
print(str15.islower()) # output: True

#18.isupper() method is used to check if all the characters in the string are uppercase. It returns True if all the characters are uppercase, otherwise it returns False.
#syntax: string.isupper()
str16="HELLO"
print(str16.isupper()) # output: True

#19.isspace() method is used to check if all the characters in the string are whitespace. It returns True if all the characters are whitespace, otherwise it returns False.
#syntax: string.isspace()
str17="   "
print(str17.isspace()) # output: True

#20.isnumeric() method is used to check if all the characters in the string are numeric. It returns True if all the characters are numeric, otherwise it returns False.
#syntax: string.isnumeric()
str18="12345"
print(str18.isnumeric()) # output: True

#21.isidentifier() method is used to check if the string is a valid identifier. It returns True if the string is a valid identifier, otherwise it returns False.
#syntax: string.isidentifier()
str19="hello"
print(str19.isidentifier()) # output: True

#22.iskeyword() method is used to check if the string is a keyword. It returns True if the string is a keyword, otherwise it returns False.
#syntax: string.iskeyword()
'''import keyword
str20="if"
print(keyword.iskeyword(str20)) # output: True
# to get all the keywords in python we can use the keyword.kwlist method
print(keyword.kwlist) # output: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#to get keywords in group 
# syntax:(help("keywords"))
help("keywords") # output:'''

#23.join() method is used to join the elements of an iterable (list, tuple, set) into a single string. It returns a string that is the concatenation of the elements of the iterable, separated by the string on which the method is called.
#syntax: "joining character".join(string)
str21="aman"
print("-".join(str21)) # output: a-m-a-n

#24.replace() method is used to replace all occurrences of a substring in the string with another substring. It returns a new string with the replacements made.
#syntax: string.replace(old, new)
str22="hello world"
print(str22.replace("world", "python")) # output: hello python

#25.strip() method is used to remove all leading and trailing whitespace characters from the string. It returns a new string with the whitespace removed.
#syntax: string.strip()
str23="   hello world   "
print(str23.strip()) # output: hello world 

#26.lstrip() method is used to remove all leading whitespace characters from the string. It returns a new string with the leading whitespace removed.
#syntax: string.lstrip()
str24="   hello world   "
print(str24.lstrip()) # output: hello world

#27.rstrip() method is used to remove all trailing whitespace characters from the string. It returns a new string with the trailing whitespace removed.
#syntax: string.rstrip()
str25="   hello world   "
print(str25.rstrip()) # output:    hello world

#28.split() method is used to split the string into a list of substrings based on a specified delimiter. It returns a list of substrings.
#syntax: string.split(delimiter)
str26="hello world"
print(str26.split(" ")) # output: ['hello', 'world']

#29.removeprefix() method is used to remove a specified prefix from the string. It returns a new string with the prefix removed.
#syntax: string.removeprefix(prefix)
str27="Python is fun"
print(str27.removeprefix("Python ")) # output: is fun

#30.removesuffix() method is used to remove a specified suffix from the string. It returns a new string with the suffix removed.
#syntax: string.removesuffix(suffix)
str28="Python is fun"
print(str28.removesuffix(" fun")) # output: Python is

#tuple methods in python it returns tuple (31 to 32)
#31.count() method is used to count the number of occurrences of a specified element in the tuple. It returns an integer representing the count of the element.
#syntax: tuple.count(element)
tuple1=(1,2,3,4,5,1,2,3,4,5)
print(tuple1.count(1)) # output: 2

#32.index() method is used to find the index of the first occurrence of a specified element in the tuple. It returns an integer representing the index of the element.
#syntax: tuple.index(element)
tuple2=(1,2,3,4,5,1,2,3,4,5)
print(tuple2.index(1)) # output: 0

# we cant not modify the tuple because tuple is immutable but we can modify the tuple by converting it into list and then modifying the list and then converting it back to tuple.
tuple3=(1,2,3,4,5)
list1=list(tuple3)
list1[0]=10
tuple3=tuple(list1)
print(tuple3) # output: (10, 2, 3, 4, 5)

# list methods in python (33 to 45)

#33.append() method is used to add an element to the end of the list. It modifies the original list and returns None.
#syntax: list.append(element)
list1=[1,2,3,4,5]
list1.append(6)
print(list1) # output: [1, 2, 3, 4, 5, 6]

#34.extend() method is used to add multiple elements to the end of the list. It modifies the original list and returns None.
#syntax: list.extend(iterable)
list2=[1,2,3]
list2.extend([4,5,6])
print(list2) # output: [1, 2, 3, 4, 5, 6]

#35.insert() method is used to insert an element at a specified position in the list. It modifies the original list and returns None.
#syntax: list.insert(index, element)
list3=[1,2,3,4,5]
list3.insert(2, 10)
print(list3) # output: [1, 2, 10, 3, 4, 5]

#36.remove() method is used to remove the first occurrence of a specified element from the list. It modifies the original list and returns None.
#syntax: list.remove(element)
list4=[1,2,3,4,5]
list4.remove(3)
print(list4) # output: [1, 2, 4, 5]

#37.pop() method is used to remove and return the element at a specified position in the list. If no index is specified, it removes and returns the last element. It modifies the original list and returns the removed element.
#syntax: list.pop(index)
list5=[1,2,3,4,5]
print(list5.pop(2)) # output: 3
print(list5) # output: [1, 2, 4, 5]

#38.clear() method is used to remove all elements from the list. It modifies the original list and returns None.
#syntax: list.clear()
list6=[1,2,3,4,5]
list6.clear()
print(list6) # output: []

#39.index() method is used to find the index of the first occurrence of a specified element in the list. It returns an integer representing the index of the element.
#syntax: list.index(element)
list7=[1,2,3,4,5,1,2,3,4,5]
print(list7.index(1)) # output: 0

#40.count() method is used to count the number of occurrences of a specified element in the list. It returns an integer representing the count of the element.
#syntax: list.count(element)
list8=[1,2,3,4,5,1,2,3,4,5]
print(list8.count(1)) # output: 2

#41.sort() method is used to sort the elements of the list in ascending order. It modifies the original list and returns None.
#syntax: list.sort()
list9=[5,2,3,1,4]
list9.sort()
print(list9) # output: [1, 2, 3, 4, 5]

#42.reverse() method is used to reverse the order of the elements in the list. It modifies the original list and returns None.
#syntax: list.reverse()
list10=[1,2,3,4,5]
list10.reverse()
print(list10) # output: [5, 4, 3, 2, 1]

#43.copy() method is used to create a shallow copy of the list. It returns a new list that is a copy of the original list.
#syntax: list.copy()
list11=[1,2,3,4,5]
list12=list11.copy()
print(list12) # output: [1, 2, 3, 4, 5]
print(id(list11)) # both id same
print(id(list12)) # same id as list 11

#44.shallow copy() here the nested list id is same but the first list id is different
list13=[1,2,3,[1,2]]
list14=list13.copy()
print(list14) # output [1, 2, 3, [1, 2]]
print(id(list13)) ##4372968320
print(id(list14)) ##4372968448
print(id(list13[1])) ##4394328680
print(id(list14[1])) ##4394328680

#45.deep copy () in this both nested list and orignial id is dirrerent 
#Syntax:-new_var_name=deepcopy(old_var_name)
#It will copy from one variable to another variable same it is
#For this madatonary step to do
# step1
#From copy import deep copy
