# Regular Method takes in the Instance (Object) as an Argument

# def fullname(self):
#     return '{} {}'.format(self.first,self.last)

# Here we have given self as an Argument which Points towards the Instance

# So when we Replace the Argument from Instance to being a Class this is called as ClassMethods

class Employee:

    raise_amount=1.04
    num_of_emps=0

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@.com"

        self.num_of_emps+=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def applyRaise(self):
        self.pay=int(self.pay*self.raise_amount)
    
    # Here wee are using @classmethod as Decorator
    # And as we give self as the Argument for Instance we give cls as Argument for Class

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
    
    # Here we are equating the value amount to raise_amount where amount is the Argument passed

emp_1=Employee
emp_2=Employee

Employee.set_raise_amount(1.05)
# Here we are setting the value for amount as 1.05
# And this is samee as :: Employee.raise_amount=1.05

# emp_1.set_raise_amount(1.06)
# In above syntax you can see that instead of providing the value for Class 
# We are providing for Instance but then too as the method is classmethod it will make class at class Level
# And changes will be appliedd to all Instance not just the Specific class

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# We can also use @classmethods as Constructor
# Now suppose we Pass a Str where the info is Seperated by '-' then we can do like

class Employee1:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_str1 = 'John-Doe-70000'
new_emp1 = Employee1.from_string(emp_str1)
print(new_emp1.email)
print(new_emp1.pay)


# So as in Regular Class method we give self as Argument and Class for ClassMethods
# In Static Methods we do not Pass any Argument Pointing towards Instnace or the Class

# We use this when we think that passing self or cls as first Argument is not needed 

import datetime
my_date = datetime.date(2026, 7, 10)

class Employee2:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6: 
            return False
        return True

print(Employee2.is_working(my_date))