
# Creating a sample class Employee. 

# Unlike Java the class name and the file name .py can be different.

class Employee(object): # object is the super class of all classes in Python. Every class by default inherits the object class

    # The __init__ method acts as the default constructor and can be used to initialize instance variables.
    
    # The self object is just like the Java 'this' keyword used to access the class instance internally.
    
    def __init__(self,first,last,pay):
        print(f"Creating class instance ... {self}")
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = self.first+"."+self.last+"@company.com"
        print("Class instance created ...")
    
    # This is an example of an instance method, this method is accessible by class instances.
    # The first argument of any instance method is the self keyword, without this the function would not be accessible by the class instance.
    def fullname(self):
        return "{} {}".format(self.first,self.last)
def main():
    print(".-"*50)
    print("*"*28)
    print("Accessing the method fullname using the instance variable\n")
    emp = Employee("Sarvagya","Dubey",75000) # Note that the parameter self is not passed only the instance variables.
    print(f"Employee Name : {emp.fullname()}")
    print("-"*28)

    # Invoking emp.fullname() is equivalent to internally calling the below snippet, where the class accesses the instance method and passes the instance to it
    # to the self parameter.
    print("Accessing the method fullname using the Class Employee \n")
    emp = Employee("Sarvagya","Dubey",75000)
    print(f"Employee Name : {Employee.fullname(emp)}")
    print("-"*28)
    print(".-"*50)

# Python is an interpreted language, still it has a bytecode compiler .
# Upon running the script "python Sample_Class.py", the intepreter compiles the source code into bytecode(.pyc) and then the VM executes it line by line.
# Also, unlike Java it is not necessary to compile programs using first using the python command, they can automatically be imported and executed.
# To import this use from Sample_Class import main. This would automatically compile the file and generate its bytecode
# Then invoking the 'main' function main() would execute the code.