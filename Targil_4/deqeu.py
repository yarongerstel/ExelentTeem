# # deque objects
# Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”)
# Deques support thread-safe, memory efficient appends and pops from either side of the deque with
#     approximately the same O(1) performance in either direction.
#
# Though list objects support similar operations, they are optimized for fast fixed-length operations and
# incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and
# position of the underlying data representation.

from collections import deque

d = deque('ghi')  # make a new deque with three items
for elem in d:  # iterate over the deque's elements
    print(elem.upper())
# G
# H
# I

d.append('j')  # add a new entry to the right side
d.appendleft('f')  # add a new entry to the left side
print(d)  # show the representation of the deque
# deque(['f', 'g', 'h', 'i', 'j'])

d.pop()  # return and remove the rightmost item
# 'j'
d.popleft()  # return and remove the leftmost item
# 'f'
print(list(d))  # list the contents of the deque
# ['g', 'h', 'i']

list(reversed(d))  # list the contents of a deque in reverse
# ['i', 'h', 'g']
print('h' in d)  # search the deque
# True
d.extend('jkl')  # add multiple elements at once
print(d)
# deque(['g', 'h', 'i', 'j', 'k', 'l'])
d.rotate(1)  # right rotation
print(d)
# deque(['l', 'g', 'h', 'i', 'j', 'k'])
d.rotate(-1)  # left rotation
print(d)
# deque(['g', 'h', 'i', 'j', 'k', 'l'])

deque(reversed(d))  # make a new deque in reverse order
# deque(['l', 'k', 'j', 'i', 'h', 'g'])
d.clear()  # empty the deque
d.pop()  # cannot pop from an empty deque
# Traceback (most recent call last):
#     File "<pyshell#6>", line 1, in -toplevel-
#         d.pop()
# IndexError: pop from an empty deque

d.extendleft('abc')  # extendleft() reverses the input order
print(d)
# deque(['c', 'b', 'a'])
