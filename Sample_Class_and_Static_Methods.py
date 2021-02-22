# This script illustrates the use of classmethods and staticmethods in Python.

import datetime
class Employee(object):
    
    raise_amount=1.05
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = self.first+"."+self.last+"@company.com"
    
    def fullname(self):
        return "{} {}".format(self.first,self.last)
        
    def apply_raise(self):
        self.pay = self.pay*Employee.raise_amount # Every class variable is accessed using the class name
        return self.pay
    
    # To convert a method into a classmethod we use the decorator @classmethod to tell the interpreter
    # that the method is a class method. Class methods can modify the state of the class and can be accessed by instances as well.
    @classmethod
    def set_raise_amount(cls,amount):
        """
        classmethod set_raise_amount
        ----------------------------
        cls      : Is the class instance, just like instance methods refer to the instance as 'self'
                   a classmethod has a class object referred as 'cls'.
        amount   : amount """
        
        cls.raise_amount = amount
        
    # Class methods can also be used as alternative constructors or factory methods to instantiate objects of the class
    @classmethod
    def from_string(cls, emp_string):
        first,last,pay = emp_string.split("-")
        return cls(first,last,int(pay)) # This statements creates instances of the class, here the class is referred as 'cls'
        # we can use any other class name to create instance of the other class as well.
        # Hence, we can say that a class method also acts as an alternative constructor or a factory method.
        
        
    # Static methods do not have access to the class object 'cls' or the instance 'self'.
    # They are kept in the class because they are logically related to the class. They are defined using "@staticmethod" decorator.
    
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    

def main():
    print(".-"*55)
    print("*"*100)
    emp = Employee("Sarvagya","Dubey",75000)
    print("Invoking the classmethod \"set_raise_amount\" ")
    Employee.set_raise_amount(1.15) # The class reference is used to invoke class methods.
    print(emp.raise_amount)
    print(Employee.raise_amount)
    print("---------------------------------------------------------------\n")
    print("Invoking classmethod \"from_string\" and creating class instance \n")
    print("---------------------------------------------------------------")
    print()
    emp2 = Employee.from_string("Anuj-Dubey-50000")
    print("************************************************")
    print("EMPLOYEE DETAILS :                             *")
    print("************************************************")
    print(f"Employee Name   : {emp2.fullname()}")
    print(f"Email           : {emp2.email}")
    print(f"Salary          : {emp2.pay}")
    print("************************************************")
    print()
    print("---------------------------------------------------------------\n")
    print(f"Class variable \"set_raise_amount \"    : {Employee.raise_amount} ")
    print(f"Instance variable \"set_raise_amount\" : {emp2.raise_amount} ")
    print("Invoking class method \"set_raise_amount through an instance \" \n")
    print("---------------------------------------------------------------")
    emp2.set_raise_amount(1.25)
    print("After invoking class method using instance : ")
    print(f"Class variable \"set_raise_amount \"    : {Employee.raise_amount} ") # It can be verified that the instance changes the class variables
    print(f"Instance variable \"set_raise_amount\" : {emp2.raise_amount} ")
    print()
    print("---------------------------------------------------------------\n")
    print("Invoking staticmethod \"is_weekday \" \n")
    print("---------------------------------------------------------------")
    print()
    today = datetime.date.today()
    is_a_weekday = Employee.is_weekday(today)
    print(f"Is today a weekday ? : {is_a_weekday} \n")
    print("---------------------------------------------------------------")
    print("*"*100)
    print(".-"*55)

