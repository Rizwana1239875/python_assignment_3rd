# list:
# list are created using square brackets[].
thislist = ["apple", "banana", "grapes"]
print(thislist)

# list items
# list items are ordered,changeable,and allow duplicate values.list items are indexed [o],the second
#  item has index [1] etc.Allow Dublicates.

thislist = ["apple", "banana", "orange", "cherry", "apple", "orange"]
print(len(thislist))

# List Length
# To determine how many items a list has, use the len() function:
# List items-Data types
# List items can be a any data types:

# string, int and boolean data types:
list1 = ["apple", "banana", "orange"]
list2 = [1,4,7,9,8,3]
list3 = [True,False,False]

# A list with strings integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

# Create a Tuple:it is created using parentheses() and immutable(unchangeable).

thistuple = ("apple", "banana", "orange")
print(thistuple)

#Tuple items:
# Tuples allows dublicate values:
thistuple = ("apple", "banana", "orange", "cherry", "apple", "orange")
print(thistuple)

# Create Tuple with one item:

thistuple = ("apple",)
print(type(thistuple))

# Not a tuple
thistuple = ("apple")
print(type(thistuple))