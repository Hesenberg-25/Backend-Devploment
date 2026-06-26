# Property Method is used when we want a Method for to used as an Attribute

class Employee:

    def __init__(self,first,last):
        self.first=first
        self.last=last
    # @property is smae as @property.getter
    @property
    def email(self):
        return ('{}{}@gmail.com'.format(self.first,self.last))
    
    @property
    def fullname(self):
        return ('{} {}'.format(self.first,self.last))
    
    # Sometime you need to change the Content inside the __init__ from some other Methods Input
    # This can be done by using Property Setter

    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print('Deleter is called!')
        self.first=None
        self.last=None

emp_1=Employee('Test','User')
print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)
print("\n")

emp_1.first='Jane'
print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)
print("\n")

emp_1.fullname='John Doe'

print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)
print("\n")

del emp_1.fullname
print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)
print("\n")
