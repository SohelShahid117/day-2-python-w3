# start from--https://www.w3schools.com/python/python_casting.asp
#https://youtu.be/1mLmW0sTzjw?si=vNPM38zvKJ8hSlIi--2hr done
"""
9.Python Casting
10.Python Strings
11.Python Booleans
12.Python Operators
"""
print("hello world")
print("enjoy Python")
print("Python is awesome")

#9.Python Casting
"""
Casting in python is therefore done using constructor functions:

    int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
    float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
    str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

"""
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)


x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)


x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)


#Python Strings
#You can use double or single quotes:

print("Hello")
print('Hello')


print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


a = "Hello"
print(a)


a = """Lorem ipsum dolor sit amet,consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = '''Lorem ipsum dolor
 sit amet,
consectetur 
adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])
print(len(a))
print(a[len(a)-1])


for x in "banana":
  print(x) 

# check
txt = "The best things in life are free!"
print("free" in txt)
print("tree" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)
print("best" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])

b = "Hello, World!"
print(b[-5:-1])
print(b[-5:])
print(b[:-2])

a = "Hello, World!"
print(a.upper())
print(a.lower())

a = "      Hello,            World!           "
print(a.strip()) #remove white space from start & ending

a = "Hello, World!"
print(a)
print(a.replace("H", "J"))

a = "Hello, World!"
# b = a.split(",")
b = a.split(" ")
print(b)


a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)


age = 36
txt = "My name is John, I am " + str(age)
print(txt) 

"""
F-Strings

F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
"""

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


txt = f"The price is {20 * 59} dollars"
print(txt)

num1=10
num2=20
print(f"sum = {num1+num2}")

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = 'It\'s alright.'
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 

txt = "Hello\nWorld!"
print(txt) 

txt = "Hello\tWorld!"
print(txt) 

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#This example erases one character (backspace):
txt = "Hello\bWorld!"
print(txt) 

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by three integers will result in a octal value:
txt = "\110\111\112\113\114"
print(txt) 


#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
txt = "\x48\x49\x50\x51\x52"
print(txt) 




"""
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string

count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value

expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string

format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric

isalpha()	    Returns True if all characters in the string are in the alphabet
isascii()	    Returns True if all characters in the string are ascii characters
isdecimal()	    Returns True if all characters in the string are decimals

isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case

isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces

istitle() 	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Converts the elements of an iterable into a string

ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string

maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value

rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string

rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string

split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value

strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case

translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
"""


# capitalize()	Converts the first character to upper case
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "python is FUN!"
x = txt.capitalize()
print (x)

txt = "36 is my age."
x = txt.capitalize()
print (x)

# casefold()	Converts string into lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# center()	Returns a centered string
txt = "banana"
x = txt.center(20)
print(x)

x = txt.center(50)
print(x)


txt = "banana"
x = txt.center(10, "O")
print(x)


# count()	Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)


# encode()	Returns an encoded version of the stringendswith()	Returns true if the string ends with the specified value

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world")
print(x)


txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 1, 50)
print(x)

# expandtabs()	Sets the tab size of the string
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(5)
print(x)

# find()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)
print(txt.index("e"))

txt = "Hello, welcome to my world."
x = txt.find("e", 2, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.find("q"))
# print(txt.index("q"))


# format()	Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))\

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)


# index()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)


txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.find("q"))
# print(txt.index("q"))


# isalnum()	Returns True if all characters in the string are alphanumeric
# Check if all the characters in the text are alphanumeric:
txt = "Company12"
x = txt.isalnum()
print(x)


"""
The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

Example of characters that are not alphanumeric: (space)!#%&? etc.
"""


txt = "Company 12"
x = txt.isalnum()
print(x)


# isalpha()	Returns True if all characters in the string are in the alphabet

txt = "CompanyX"
x = txt.isalpha()
print(x)


txt = "Company10"
x = txt.isalpha()
print(x)


# isascii()	Returns True if all characters in the string are ascii characters
txt = "Company123"
x = txt.isascii()
print(x)



# isdecimal()	Returns True if all characters in the string are decimals
txt = "1234"
x = txt.isdecimal()
print(x)


# isdigit()	Returns True if all characters in the string are digits
txt = "50800"
x = txt.isdigit()
print(x)



# islower()	Returns True if all characters in the string are lower case
txt = "hello world!"
x = txt.islower()
print(x)

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())


# isnumeric()	Returns True if all characters in the string are numeric
txt = "565543"
x = txt.isnumeric()
print(x)

"""
The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.

Exponents, like ² and ¾ are also considered to be numeric values.

"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
"""


# istitle() 	Returns True if the string follows the rules of a title
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

"""
The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
"""


a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())


# isupper()	Returns True if all characters in the string are upper case
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)


a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())

#https://www.w3schools.com/python/ref_string_join.asp