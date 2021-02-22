# This is an example of inheritence in Python. We shall create a parent class Employee, followed by a sub class Developer
# and try to analyze the inheritence behaviour of the sub-class.

import datetime

class Employee(object):
    
    raise_amount = 1.15
    def __init__(self,first,last,pay):
        
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = self.first+"."+self.last+"@company.com"
        
    def fullname(self):
        return "{} {}".format(str.capitalize(self.first),str.capitalize(self.last))
    
    @classmethod
    def set_raise_amount(cls,amount):
        """
        classmethod set_raise_amount
        ----------------------------
        cls      : Is the class instance, just like instance methods refer to the instance as 'self'
                   a classmethod has a class object referred as 'cls'.
        amount   : amount """
        
        cls.raise_amount = amount
        
    def apply_raise(self):
        self.pay = self.pay*self.raise_amount # Every class variable is accessed using the class name
        return self.pay
    
    @classmethod
    def from_string(cls, emp_string):
        first,last,pay = emp_string.split("-")
        return cls(first,last,int(pay))
        
    
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    
    raise_amount=1.25
    def __init__(self,first,last,pay,language):
        
        # Here instead of rewriting the entire initialization code we can inherit most of the code from the parent Employee class
        # using the 'super' keyword
        
        super().__init__(first,last,pay) # Using super is advised when there is single inheritence.
        # For multiple inheritence it is advised to use the class name instead of super() to avoid errors.
        # Employee.__init__(self,first,last,pay)
        self.language = language
    
    @classmethod
    def from_string(cls,developer_string):
        
        first,last,pay,language = developer_string.split("-")
        return cls(first,last,int(pay),language) 
    
    
        

def main():
    print(".-"*55)
    print("*"*100)
    
    # To check all the objects that a child class has inherited from its parents use help
    print(help(Developer))
    # From the results of the above statement it can be verified that a child class inherits 
    # all objects from the parent including the classmethods and staticmethods
    
    dev1 = Developer("Sarvagya","Dubey",75000,"Java")
    print("************************************************")
    print("EMPLOYEE DETAILS :                             *")
    print("************************************************")
    print(f"Employee Name     : {dev1.fullname()}")
    print(f"Email             : {dev1.email}")
    print(f"Salary            : {dev1.pay}")
    print(f"Language          : {dev1.language}")
    print("Applying raise on developer salary using inherited method apply_raise")
    raised = dev1.apply_raise()
    print(f"Raised Salary     : {raised}")
    print("************************************************")
    print()
    
    print("Creating instance using \"from_string\" classmethod")
    dev2 = Developer.from_string("Anuj-Dubey-50000-Python")
    print("************************************************")
    print("EMPLOYEE DETAILS :                             *")
    print("************************************************")
    print(f"Employee Name     : {dev2.fullname()}")
    print(f"Email             : {dev2.email}")
    print(f"Salary            : {dev2.pay}")
    print(f"Language          : {dev2.language}")
    print("Applying raise on developer salary using inherited method apply_raise")
    raised2 = dev2.apply_raise()
    print(f"Raised Salary     : {raised2}")
    print("************************************************")
    print()
    print("Invoking the inherited static method \"is_weekday\" using child class instance")
    print(Developer.is_weekday(datetime.date.today()))
    print(".-"*55)
    print("*"*100)
    