# Class is a Blueprint which have us create Instancese of Class i.e Objects

# At Instance-Level the parameter is only Applicable for that Specific Object
# Means modifying anything in Instance of specific object will not have any effect on other Objects

# Wheras at Class-Level the parameter is common for all the objects as they share it commonly
# As it belongs to class and changing it just once will affect all the classes

# Methods are the Function inside the CLasses 

class Employee:

    # Here we are using {__init__} to like Intialize Instance variable inside the Class 
    # It works like a Constructor

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+"."+last+"@.com"
        self.pay=pay
    
    # Methods inside class are the Function which peform some Specific Functionality
    # Here we only provide 'self' as an Instance during Method Formation

    def fullname(self):
        return '{} {}'.format(self.first,self.last)


emp_1=Employee('Durvesh','Patil',26)
emp_2=Employee('Test','User',9)

print(emp_1)
print(emp_2)

print(emp_1.first, emp_1.last, emp_1.email, emp_1.pay)
print(emp_2.first, emp_2.last, emp_2.email, emp_2.pay)

# Calling the method can done in two ways :
 
print(emp_1.fullname())
print(Employee.fullname(emp_1))