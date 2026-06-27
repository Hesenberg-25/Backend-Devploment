# Class Variable are the Parameters which are shared by all the Instances of the Class Commonly
# Class Variable stays same for all the Objects unless we make Specific change for Each one of them
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
        # Always try to call the Class Function through the Object and not through Class
        # Because sometimes we need to Hardcode the value of the Class Variable for some Specific condition
    

emp_1=Employee('Durvesh','Patil',50000)
emp_2=Employee('Test','User',60000)


emp_1.applyRaise()
emp_2.applyRaise()

print(emp_1.pay)
print(emp_2.pay)

print(Employee.num_of_emps)

# When we try to check the Class Variable for the Object first we find it in Object 
# If not found in object we try to find in Class 

# When we want to change the value of Class where the Condition will be Appiled for all the Objects unless it is Hardcoded
Employee.raise_amount=1.05

# When we try to change the Specific Class Variable for some Object
emp_1.raise_amount=1.06

