'''
Recursion - 
Recursion is a programming technique where a function calls itself, 
breaking a problem into smaller instances. Each recursive call contributes to solving the overall problem.
'''

# simple program for recursion.
def fact(n):
    #terminating condition
    if n==0:
        return 1
    return n*fact(n-1)
    
res = fact(4)
print(res)

'''
remove(x)
This operation removes element  from the set.
If element  does not exist, it raises a KeyError.
The .remove(x) operation returns None.

Example

>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0
.discard(x)
This operation also removes element  from the set.
If element  does not exist, it does not raise a KeyError.
The .discard(x) operation returns None.

Example

>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
.pop()
This operation removes and return an arbitrary element from the set.
If there are no elements to remove, it raises a KeyError.

Example

>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set
Task
You have a non-empty set , and you have to execute  commands given in  lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer , the number of elements in the set .
The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer , the number of commands.
The next  lines contains either pop, remove and/or discard commands followed by their associated value.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
A = set(map(int, sorted(input().split(), reverse=True)))
nbrOfCommands = int(input())
for _ in range(nbrOfCommands):
    # print(A)
    command = input().split()
    if len(command)==1:
        A.pop()
    else:
        if command[0]=='remove':
            if int(command[1]) in A:
                A.remove(int(command[1]))
        elif command[0]=='discard':
            A.discard(int(command[1]))
            
print(sum(A))