
# Creating a sample class Employee. 

# Unlike Java the class name and the file name .py can be different.

class Employee(object): # object is the parent class of all classes in Python. Every class by default inherits the object class

    # The __init__ method acts as the default constructor and can be used to initialize instance variables.
    
    # The self object is just like the Java 'this' keyword used to access the class instance internally.
    
    def __init__(self,first,last,pay):
        print(f"Creating class instance ... {self}")
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = self.first+"."+self.last+"@company.com"
        print("Class instance created ...")
    
    """This is an example of an instance method, this method is accessible by class instances.
    # The first argument of any instance method is the self keyword, without this the function would not be accessible by the class instance."""
    def fullname(self):
        return "{} {}".format(self.first,self.last)
def main():
    print(".-"*55)
    print("*"*100)
    emp = Employee("Sarvagya","Dubey",75000) # Note that the parameter self is not passed only the instance variables.
    
    # List of instance variables in an instances can be viewed using __dict__
    print()
    print("*"*100)
    print()
    print("Instance variables for the instance : ")
    print(emp.__dict__)
    print()
    
    
    # Instance variables can dynamically be added to the instance during runtime.
    # For example, the emp instance has 4 variables first,last,pay and email, 
    # we can dynamically initialize a variable after creation of an instance as well.
    
    print("--------------------------------------------------------")
    print("Adding instance variable phone after instance creation .")
    print("--------------------------------------------------------")
    emp.phone = "+919999999991"
    print("Instance variables for the instance : ")
    print(emp.__dict__)
    print()
    print("*"*100)
    print("                   *")
    print("EMPLOYEE DETAILS : *")
    print("********************")
    print(f"Employee Name    : {emp.fullname()}")
    print(f"Email            : {emp.email}")
    print(f"Salary           : {emp.pay}")
    print(f"Phone            : {emp.phone}")
    print()
    print("*"*100)

    # Invoking emp.fullname() is equivalent to internally calling the below snippet, where the class accesses the instance method and passes the instance to it
    # to the self parameter.
    print()
    print("Accessing the method fullname using the Class Employee \n")
    emp = Employee("Sarvagya","Dubey",75000)
    print(f"Employee Name : {Employee.fullname(emp)} \n")
    print("*"*100)
    print(".-"*55)

""" Python is an interpreted language, still it has a bytecode compiler .
# Upon running the script "python Sample_Class.py", the intepreter compiles the source code into bytecode(.pyc) and then the VM executes it line by line.
# Also, unlike Java it is not necessary to compile programs using first using the python command, they can automatically be imported and executed.
# To import this use from Sample_Class import main. This would automatically compile the file and generate its bytecode
# Then invoking the 'main' function main() would execute the code."""