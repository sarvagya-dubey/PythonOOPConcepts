# This example gives an example of closures and inner functions. Functions in python are first class objects.
# Any first class function has the following properties:
# (i)   First class functions are an instance of an Object type.
# (ii)  First class functions can be stored as variable.
# (iii) First class functions can be passed as arguments to other functions.
# (iv)  First class functions can be returned as objects from other functions.
# (v)   First class functions can be stored as objects inside data-structures like lists,tuples,dictionary etc.

# A function declared inside another function is called a nested-function. The nested function can access the variables of the enclosing outer function
def outer(msg): # This is the enclosing function
    
    def inner(): # This is the nested function.
        print (msg)
    return inner # Fist class functions can be returned from a function.

def main():
    global outer # Declaring this to set the scope of the outer function inside the main function as global. Not doing so would lead to UnboundLocalError
    a = outer("Hi")
    print(a.__name__)
    del(outer) # We deleted the outer function from the memory.
    a() # Observe that even when the outer function is no longer available the nested function can still access the data that was passed to the outer function.
    # The technique by which some data gets attached to the code is called closure in Python. Closure is an inner function that has access to the variables
    # of the enclosing scope in which it was created, even after the enclosing function has stopped its execution.
    # A closure closes over the free variables from their environment.