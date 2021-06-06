# This example illustrates how to use class variables

""" Class variables are variables that are shared between all instances of a class.
While instance variables are unique to each instance of the class, class variables
are the same for each instance."""

class Employee(object):

    raise_amount = 1.05
    
    def __init__(self,first,last,pay):
        print(f"Creating class instance ... {self}")
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = self.first+"."+self.last+"@company.com"
    
    """This is an example of an instance method, this method is accessible by class instances.
    # The first argument of any instance method is the self keyword, without this the function would not be accessible by the class instance."""
    def fullname(self):
        return "{} {}".format(self.first,self.last)
        
    def apply_raise(self):
        self.pay = self.pay*Employee.raise_amount # Every class variable is accessed using the class name
        return self.pay
def main():
    print(".-"*55)
    print("*"*100)
    print()
    emp = Employee("Sarvagya","Dubey",75000)
    print()
    print("************************************************")
    print("Printing the instance's __dict__ attribute \n") # We find that the attribute raise_amount is by default not present in the instance emp.
    print(emp.__dict__) # Lists the attributes of the instance.
    print("************************************************")
    print("Printing the dir(instance) \n")
    print(dir(emp)) # Lists the inherited attributes and methods of the instance, here we find that the instance can access the class variable raise_amount
    print(f"Accessing class    variable raise_amount : {Employee.raise_amount}")
    print(f"Accessing instance variable raise_amount : {emp.raise_amount} \n")
    print("************************************************")
    # It can be verified that the instance variable raise_amount defaults to the class variable raise_amount,
    # The value of this instance variable can be changed dynamically during the runtime.
    print("************************************************")
    print("EMPLOYEE DETAILS :                             *")
    print("************************************************")
    print(f"Employee Name   : {emp.fullname()}")
    print(f"Email           : {emp.email}")
    print(f"Salary          : {emp.pay}")
    print("Applying raise on employee salary")
    raised = emp.apply_raise()
    print(f"Raised Salary   : {raised}")
    print("************************************************")
    #print("*"*100)
    print(".-"*55)

