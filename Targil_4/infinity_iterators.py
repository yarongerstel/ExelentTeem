# Infinite iterators
# Iterator in Python is any Python type that can be used with a ‘ for in loop’.
# Python lists, tuples, dictionaries, and sets are all examples of inbuilt iterators.
# But it is not necessary that an iterator object has to exhaust, sometimes it can be infinite.
# Such type of iterators are known as Infinite iterators.
#
# Python provided three types of infinite itertors:
# count(start, step): \
#     This iterator starts printing from the “start” number and prints infinitely.If steps are mentioned, the numbers are
#     skipped else step is 1 by default.See the below example for its use with for in loop.
# Example:

# Python program to demonstrate
# infinite iterators

import itertools

# for in loop
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")
# Output:
#
# 5
# 10
# 15
# 20
# 25
# 30
# cycle(iterable): This iterator prints all values in order from the passed container.
#  It restarts printing from the beginning again when all elements are printed in a cyclic manner.
# Example 1:


count = 0

# for in loop
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end=" ")
        count += 1
# Output:
#
# A
# B
# A
# B
# A
# B
# A
# B
# Example 2: Using next function.

l = ['Geeks', 'for', 'Geeks']

# defining iterator
iterators = itertools.cycle(l)

# for in loop
for i in range(6):
    # Using next function
    print(next(iterators), end=" ")
# Output:
# Geeks for Geeks Geeks for Geeks
#
# repeat(val, num): This iterator repeatedly prints the passed value infinite number of times.If the optional keyword
# num is mentioned, then it repeatedly prints num number of times.
# Example:

# using repeat() to repeatedly print number
print("Printing the numbers repeatedly : ")
print(list(itertools.repeat(25, 4)))
# Output:
#
# Printing the numbers repeatedly: [25, 25, 25, 25]
