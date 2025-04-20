# Frozen set is just an immutable version of a python set.
# while elements of a set can be modified at any time,elements 
# of the frozen set remain the same # after creation.
# how to create frozen set?
# by using frozenset() in built function.
# syntax: frozenset iterable(optional)

# Frozen set:

# list1 = ["apple","banana","apple","orange","banana","cherry"]
# fset1 = frozenset(list1)
# print(type(fset1))
# print(fset1)

# what are the operations that we can perform on the frozen set.
# fset2 = fset1.copy()
# rint(fset2)

fset1 = frozenset([4,5,6,7,8,9])
fset2 = frozenset([1,2,3,4,5])
fset3 = fset1.union(fset2)
print(fset3)