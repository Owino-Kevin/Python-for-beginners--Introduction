# We shall look at Python Strings.
print("Hellow, World...")
a = "Hellow, World"
print(a[0])  # to print the first character
print(a[1:9])  # to print the characters in the first to ninth position
print(len(a))  # to show the length of the string
print(a.upper())  # To print upper case
print(a.lower())  # To print lower case
print(a.replace("H", "J"))  # To replace H with J
print(a.split(","))  # To split the strings into substrings if it finds instances of the seperator
if "World" in a:
    print("Yes, 'World' is present..")

# Now let's have a look at Python Variables.
# These assign value as follows:
x = 5
y = "Kevin"
p, q, r = "Orange", "Banana", "Cherry"
m = 4
n = 11
print(x)
print(y)
print(p)
print(q)
print(r)
print(x, y, q, r)
print(p + y + r)
print(m + n)

# We can as well cast to specify datatype of a variable
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# Python accepts both single and double quotes
x = "Kevin"
# Python is also case-sensitive

# Lets look at Global Variables- variables created outside a function like examples above
t = "awesome"


def myfunc():
    print("Python is" + t)


myfunc()
# We can create a variable with the same name inside a function.
t = "awesome"


def myfunc():
    t = "fantastic"
    print("Python is" + t)


myfunc()

print("Python is" + t)


# Global Keyword-to create a global variable inside a function we use global keyword.
def myfunc():
    global t
    t = "fantastic"


myfunc()
print("Python is" + t)
c = 5
print(type(c))

# Boolean Values(TRUE or FALSE)
print(10 > 9)
print(10 == 9)
print(10 < 9)

s = 200
p = 33
if s > p:
    print("s is greater than p")
else:
    print("s is less than p")

print(bool("Hello"))  # To bool a string
print(bool(15))  # To bool an integer

# Lets have a look at LISTS
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]  # Changes the values of banana and cherry
print(thislist)
thislist.insert(2, "watermelon")  # Insert watermelon as a third term or second position
print(thislist)
thislist.append("avocado")  # Adds avocado at the end of the list
print(thislist)
thislist.insert(1, "jackfruit")  # This inserts jackfruit in the second position
print(thislist)
tropical = ["kales", "spinach", "cabbages"]
thislist.extend(tropical)  # Extends the list
print(thislist)
thislist.remove("kiwi")  # Removes Kiwi from the list
print(thislist)
thislist.pop(6)  # Removes item in the seventh position
print(thislist)
for x in thislist:  # Prints items in the list one by one
    print(x)

newlist = []

for x in thislist:
    if "a" in x:
        newlist.append(x)  # This code creates a new list with items with letter 'a' in them. This is quite long

print(newlist)

newlist = [x for x in thislist if "a" in x]  # This is a simple way
print(newlist)

thislist.sort()  # Arrange the list in alphabetical order
print(thislist)

# Next, lets have a look at TUPLES in Python.
# Like lists, they store multiple items in one variable. But unlike lists it is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "watermelon", "apple", 34, True)  # Allows duplicates
print(thistuple)
print(len(thistuple))  # to show the number of items in the tuple
print(thistuple[4])  # To print item in the fifth position in the tuple
print(thistuple[-3])  # to print item in the third position from the left
print(thistuple[-6:-4])  # to print items from the second to sixth position from left side

# Python SETS: a collection which is unordered and unchangeable
thisset = {"apple", "banana", "cherry", "orange", False, True, 0}
print(thisset)
for x in thisset:  # This loops through items in the set
    print(x)
thatset = {1, 3, 9}
set3 = thisset.union(thatset)  # This joins the two sets

# Python DICTIONARIES: Used to store data values in key:value pairs. Ordered, changeable and do not allow duplicates
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1994
}
print(thisdict)

# If and Else Statements in Python
a = 33
b = 100
if b > a:
    print("b is greater than a")  # This is an if statement

if b > a:
    print("b is greater than a")
elif a==b:
    print("a is equal to b")  # elif is used if previous condition is not true.

d = 200
e = 199
if e > d:
    print("e is greater than d")
elif e == d:
    print("e is equal to d")  #This is an If...Else statement
else:
    print("e is less than d")

f = 40
if f > 10:
    print("above ten")
    if f > 20:
        print("and also above 20!")  # This is a nested if statement.
    else:
        print("but not above 20.")
else:
    print("below ten")

# Python FUNCTIONS: defined using a def word
def my_function():
    print("Hellow from a function")
my_function()

# Arguments: Information is passed to functions through arguments.
def my_function(fname):
    print(fname + "Ref")
print("Kevin")
print("Oduor")
print("Owino")

# Python LAMBDA: a small anonymous function
x = lambda a : a + 10  # This is an addition argument
print(x(5))
x = lambda a, b : a * b
print(x(4,5))  # This is a multiplication argument

# Python ARRAYS: array is a special variable which can hold more than one value at a time.
cars = ["Ford", "Volvo", " BMW"]  # This is an array of cars
print(cars)
x = cars[0]  # index of the first car
print(x)
cars.append("Toyota")  # Adds Toyota to the array of cars.
cars.pop(1)  # Removes car indexed 1

# Python Classes/Objects: Almost everything is an object in python. A class is an object constructor.
class Myclass:
    x = 5  # The class name is Myclass and x is an object assigned the value 5. class is used to construct Myclass
p1 = Myclass
print(p1.x)  # Created an object called p1 and printed the value x

# Python Date
import datetime

x = datetime.datetime.now()  # datetime is a built-in library/module/package in python for date and time.
print(x)

# this is the introductory part of python for beginners. Check out for the next part of the tutorial.
