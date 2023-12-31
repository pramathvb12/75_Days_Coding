'''
Overloading - having same function name but different signetures like number of parameters, data types, Ploymorphism type - compile time
'''
def add(a, b, c=None):
    if c is not None:
        return a + b + c
    else:
        return a + b

s = add(4, 5)
p = add(6, 1, 2)

print(s, p, end=" ")

# 9 9

'''
Note :  In Python, the latest definition of a function with a given name overrides any previous definitions, and only the latest one will be used.
'''

'''
Overriding - Method overriding is a fundamental concept in object-oriented programming 
that allows for polymorphism, where objects of different classes can be treated as objects of a common base class.
'''
class A:
    def show(self):
        print("This is A")
        
class B(A):
    def show(self):
        print("This is B")

a1 = B()
a1.show()


'''
Error and exception
'''
def div(a, b):
    try:
            c = a / b
            return c
    except ZeroDivisionError:
        print("Error: Divide by zero")
        return None

d = div(5, 8)
print(d)
