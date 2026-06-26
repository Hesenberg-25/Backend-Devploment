# Dunder methods known as Double Underrscore Methods and Methods which are Surrounded by '__'
# i.e Surounded by Double Underscore
# __init__ , __call__ , __str__ , __repr__

# The main differnece between __str__ and __repr__ :
# 1. __str__ is meant for User and should be Understable and Readable for the User
# 2. __repr__ means the is used for the Deloper to know the Logic behind the Variable

# Always define __repr__ first befor __str__ 
# So that if __str__ is not present __repr__ will be called Defaultly

class Employee:

    raise_amount=1.04
    num_of_emps=0

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@gmail.com"

        self.num_of_emps+=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def applyRaise(self):
        self.pay=int(self.pay*self.raise_amount)

    def __repr__(self):
        return ("Employee ('{}','{}',{})".format(self.first,self.last,self.pay))

    def __str__(self):
        return ('{} - {}'.format(self.fullname(),self.email))
    
    def __add__(self,other):
        return self.pay+other.pay

emp_1=Employee('Test','User',50000)
emp_2=Employee('John','Doe',60000)

# print(emp_1)

print(repr(emp_1))
print(str(emp_1))

# Another Dunder Method is __add__  which perform the following task baseed on the Variable type Provided

print(int.__add__(1,2))
print(str.__add__('a','b'))

print(emp_1+emp_2)
