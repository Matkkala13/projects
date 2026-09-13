from os import name
import sys
import re

#python version
print(sys.version)

#datatypes
string = "Hello"
integer = 18
float_ = 3.14
boolean = True

#obtaning data types
print(type(string))
print(type(integer))
print(type(float_))
print(type(boolean))

#converting data types
string_to_int = int("123")
int_to_float = float(456)
float_to_string = str(789.0)

#operators
addition = 5 + 3
subtraction = 10 - 4
multiplication = 6 * 7
division = 20 / 5
integer_division = 20 // 3 #returns the quotient without the remainder
modulus = 10 % 3
exponentiation = 2 ** 3

#string operations
concatenation = "Hello" + " " + "World"
repetition = "Ha" * 3
indexing = "Hello World"[0] #returns 'H'
indexing_backwards = "Hello World"[-1] #returns 'd'
slicing = "Hello World"[0:5] #returns 'Hello'
striding = "Hello World"[::2] #returns 'HloWrd'
slicing_and_striding = "Hello World"[1:10:2] #returns 'el ol'

#escape characters
newline = "Hello\nWorld"
tab = "Hello\tWorld"
backslash = "This is a backslash: \\"
raw_string = r"This is a raw string: \n\t\\"
single_quote = 'It\'s a nice day'

#string methods
upper_case = "hello".upper() #returns 'HELLO'
lower_case = "WORLD".lower() #returns 'world'
title_case = "hello world".title() #returns 'Hello World'
#replace(old, new)
replace = "Hello World".replace("World", "Python") #returns 'Hello Python'
#split(separator, maxsplit)
split = "Hello World".split() #returns list ['Hello', 'World']
join = " ".join(["Hello", "World"]) #returns 'Hello World'
strip = "   Hello World   ".strip() #returns 'Hello World'
find = "Hello World".find("World") #returns 6
count = "Hello World".count("o") #returns 2
startswith = "Hello World".startswith("Hello") #returns True
endswith = "Hello World".endswith("World") #returns True

#regular expressions (RegEx)
sentence = "Your are as fast, so fast like he is"
pattern= r"fast"
re.search(pattern, sentence) #returns a match object if found, otherwise returns None
re.findall(pattern, sentence) #returns a list of all matches found
re.sub(pattern, "good", sentence) #returns a new string with all occurrences of the pattern replaced by the replacement string

#special sequences in RegEx
#\d - matches any digit (0-9)
#\D - matches any non-digit character
#\w - matches any alphanumeric character (letters, digits, and underscores)
#\W - matches any non-alphanumeric character
#\s - matches any whitespace character (spaces, tabs, newlines)
#\S - matches any non-whitespace character

#example
pattern = r"\d\d\d\d" #matches 4 digits
pattern2 = r"\d+" #matches one or more digits
text = "My phone number is 1234 and my zip code is 56789"

#the search() function returns a match object if the pattern is found in the string, otherwise it returns None
print(re.search(pattern, text)) 
print(re.search(pattern2, text)) 
#the findall() function returns a list of all matches found in the string, or an empty list if no matches are found
print(re.findall(pattern, text)) 
print(re.findall(pattern2, text)) 
#the group() method returns the part of the string where there was a match
match = re.search(pattern, text)
print("Match object:", match.group( )) #returns a match object for '1234'

#the split() function splits the string at each occurrence of the pattern and returns a list of substrings
print(re.split(r"\s+", text)) #splits the text into words based on whitespace
#or
print(re.split(r"\s", text)) #splits the text at each sequence of digits

#the sub() function replaces all occurrences of the pattern in the string with a replacement string and returns the modified string
print(re.sub(r"\d", "X", text)) #replaces all digits with 'X'
print(re.sub(r"\d+", "X", text)) #replaces all sequences of digits with 'X'

#lists and tuples
my_list = [1, 2, 3, "Hello", True]
my_tuple = (1, 2, 3, "Hello", True)

#list_methods
my_list.append("World") #adds an element to the end of the list
my_list.insert(0, "Start") #inserts an element at a specific index
my_list.remove(2) #removes the first occurrence of the specified value
my_list.pop() #removes and returns the last element of the list
my_list.pop(0) #removes and returns the element at the specified index
my_list.sort() #sorts the list in ascending order 
my_list.sort(reverse=True) #sorts the list in descending order  
my_list.extend([4, 5, 6]) #extends the list by appending elements from another iterable
my_list.append([7, 8, 9]) #adds a single element (which can be a list) to the end of the list
my_list.clear() #removes all elements from the list
my_list.index("Hello") #returns the index of the first occurrence of the specified value
my_list.count(1) #returns the number of occurrences of the specified value in the list
my_list.reverse() #reverses the order of the list
my_list.copy() #returns a shallow copy of the list
#another way to copy a list
my_list_copy = my_list[:] #creates a copy of the list using slicing, which doesn't affect the original list when modifications are made to the copy

#changing values in a list
my_list[0] = "New Value" #changes the value at index 0
my_list[1:3] = ["A", "B"] #changes the values at index 1 and 2 to "A" and "B"
#deleting values in a list
del my_list[0] #deletes the element at index 0
del my_list[1:3] #deletes the elements at index 1 and 2
my_list.clear() #deletes all elements from the list

#some functions that work with lists and tuples
len(my_list) #returns the number of elements in the list
len(my_tuple) #returns the number of elements in the tuple
min([1, 2, 3]) #returns the smallest element in the list
max([1, 2, 3]) #returns the largest element in the list
sum([1, 2, 3]) #returns the sum of all elements in the list/tuple
sorted([3, 1, 2]) #returns a new sorted list from the elements
sorted([3, 1, 2], reverse=True) #returns a new sorted list in descending order

#nested indexing and slicing
my_list = [1, 2, 3, 4, 5]
nested_list = [my_list, ["a", "b", "c"], (6, 7, 8)]
print(nested_list[0]) #returns [1, 2, 3, 4, 5]
print(nested_list[1]) #returns ['a', 'b', 'c']
print(nested_list[2]) #returns (6, 7, 8)
print(nested_list[0][1]) #returns 2
print(nested_list[1][0]) #returns 'a'
print(nested_list[2][2]) #returns 8 

#help function, you put any type of object as an argument and it will display the documentation for that object, including its methods and usage
help(str) #displays the documentation for the str class, including its methods and usage
help(re) #displays the documentation for the re module, including its functions and usage

#Dictionaries, formed by "key":value pairs, where each key is unique and maps to a specific value.

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"]) #returns 'Alice'
print(my_dict.get("age")) #returns 30
my_dict["age"] = 31 #updates the value for the key 'age'
my_dict["country"] = "USA" #adds a new key-value pair to the dictionary
print(my_dict) #returns {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}
my_dict.pop("city") #removes the key 'city' and its associated value from the dictionary
print(my_dict) #returns {'name': 'Alice', 'age': 31, 'country': 'USA'}
my_dict.keys() #returns a view object containing the keys of the dictionary
my_dict.values() #returns a view object containing the values of the dictionary
del my_dict["name"] #deletes the key 'name' and its associated value from the dictionary
my_dict.clear() #removes all key-value pairs from the dictionary
"age" in my_dict #returns False, since the key 'age' has been removed from the dictionary

#sets, an unordered collection of unique elements
my_set = {1, 2, 3, 4, 5}
print(my_set) #returns {1, 2, 3, 4, 5}
#you cant add two identical element to a set 
my_set.add(6) #adds an element to the set
my_set.remove(3) #removes an element from the set
1 in my_set #returns True, since 1 is an element of the set
my_set.clear() #removes all elements from the set

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2 #returns {1, 2, 3, 4, 5}
#or 
set1.union(set2) #returns {1, 2, 3, 4, 5}
intersection = set1 & set2 #returns {3}
difference = set1 - set2 #returns {1, 2}
symmetric_difference = set1 ^ set2 #returns {1, 2, 4, 5}
set1.difference(set2) #returns {1, 2}
set2.difference(set1) #returns {4, 5}
list1 = [ 1, 2,1, 5,6, 3, 4, 5]
set(list1) #turn a list to a set

set1.issubset(set2) #returns False, since set1 is not a subset of set2
set1.issuperset(set2) #returns False, since set1 is not a superset of set2
set1.isdisjoint(set2) #returns False, since set1 and set2 have a common element (3)

#conditional statements
x = 10
#if statement 
#== is the equality operator
#!= is the inequality operator
#> is the greater than operator
#< is the less than operator
#>= is the greater than or equal to operator
#<= is the less than or equal to operator
# and is the logical AND operator, which returns True if both conditions are true
# or is the logical OR operator, which returns True if at least one of the conditions is true
# not is the logical NOT operator, which returns True if the condition is false

###letters are compared based on their ASCII values, where 'a' has a value of 97 and 'b' has a value of 98, so 'a' < 'b' is True

range(0, 10) #returns a range object representing the sequence of numbers from 0 to 9

#loops
#for loop is used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code for each item in the sequence
for i in range(5):
    print(i) #prints numbers from 0 to 4

list_of_numbers = [1, 2, 3, 4, 5]   
for i, number in enumerate(list_of_numbers):
    print(f"Index: {i}, Number: {number}") #prints the index and the number for each element in the list    

#while loop is used to execute a block of code repeatedly as long as a certain condition is true
count = 0
while count < 5:    
    print(count) #prints numbers from 0 to 4
    count += 1 #increments the count by 1 in each iteration

#break statement is used to exit a loop prematurely when a certain condition is met
for i in range(10):
    if i == 5:
        break #exits the loop when i is equal to 5
    print(i) #prints numbers from 0 to 4
#continue statement is used to skip the current iteration of a loop and move on to the next iteration when a certain condition is met
for i in range(10):
    if i % 2 == 0:
        continue #skips the current iteration when i is even
    print(i) #prints odd numbers from 1 to 9

#pass statement is a placeholder that does nothing and is used when a statement is syntactically required but no action is needed
for i in range(5):
    pass #this loop does nothing and is just a placeholder


#functions 
def greet(name, age):
    return f"Hello, {name}! You are {age} years old." #returns a greeting message with the provided name and age
print(greet("Alice", 25)) #prints 'Hello, Alice! You are 25 years old.'

def add(*a):
    return sum(a) #returns the sum of all the arguments passed to the function
print(add(1, 2, 3)) #prints 6

x = 10 #declares a variable x with the value 10
def modify_global():
    global x #indicates that we want to modify the global variable x
    x = 20 #modifies the value of the global variable x to 20
modify_global() #calls the function to modify the global variable
print(x) #prints 20, which is the modified value of the global variable x

#python built in functions
abs(-5) #returns the absolute value of -5, which is 5
round(3.14159, 2) #returns 3.14, which is the value of 3.14159 rounded to 2 decimal places
len("Hello") #returns 5, which is the number of characters in the string "Hello"
len([1, 2, 3, 4, 5]) #returns 5, which is the number of elements in the list [1, 2, 3, 4, 5]
sorted([1,5,3,5,2]) #returns a new sorted list [1, 2, 3, 5, 5], but does not modify the original list

#exceptions and error handling
try:
    result = 10 / 0 #this will raise a ZeroDivisionError since division by zero is not allowed
except ZeroDivisionError:
    print("Error: You cannot divide by zero!") #this block will be executed if a ZeroDivisionError occurs
except Exception as e:
    print(f"An unexpected error occurred: {e}") #this block will be executed if any other type of exception occurs
else:
    print(f"The result is: {result}") #this block will be executed if no exceptions occur
finally:
    print("This block will always be executed, regardless of whether an exception occurred or not.") #this block will always be executed, even if an exception was raised and handled in the except blocks

#types of errors
#SyntaxError - occurs when there is a syntax error in the code, such as a missing parenthesis or a misspelled keyword
#IndentationError - occurs when there is an indentation error in the code, such as inconsistent indentation or missing indentation
#NameError - occurs when a variable or function name is not defined
#TypeError - occurs when an operation or function is applied to an object of inappropriate type
#ValueError - occurs when a function receives an argument of the correct type but an inappropriate value
#IndexError - occurs when trying to access an index that is out of range in a list
#KeyError - occurs when trying to access a key that does not exist in a dictionary
#FileNotFoundError - occurs when trying to open a file that does not exist
#ZeroDivisionError - occurs when trying to divide a number by zero
#AttributeError - occurs when trying to access an attribute that does not exist for an object
#ImportError - occurs when trying to import a module that does not exist or cannot be found
#Exception - the base class for all exceptions, which can be used to catch any type of exception that is not handled by more specific except blocks

try:
    x = int("abc") #this will raise a ValueError since "abc" cannot be converted to an integer
except (ValueError, TypeError) as e:
    print(f"An error occurred: {e}") #this block will be executed if a ValueError or TypeError occurs   




                                                                                        