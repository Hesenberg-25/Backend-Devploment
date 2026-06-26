# Inheritance is a Functinallty when we want a Class to Inherit some data from Other class

class Employee:

    raise_amount=1.04
    num_of_emps=0

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@.gmailcom"

        self.num_of_emps+=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def applyRaise(self):
        self.pay=int(self.pay*self.raise_amount)

# Format when we want to Inherit some Class
# class {new-className}({name-className-fromwhomto-Inherit})

class Developer(Employee):
    raise_amount=1.10

# When we change the raise_amount value to 1.10 now the raise_amount of Employee is Overidden by the value given to Deveploer Class
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        # super(). is used when we want the Father-Class to handle the data
        self.prog_lang=prog_lang



dev_1=Developer('Test','User',50000,'Python')
dev_2=Developer('John','Doe',70000,'C++')

# print(dev_1.pay)
# dev_1.applyRaise()
# print(dev_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)

print(dev_2.email)
print(dev_2.prog_lang)

class Manager(Employee):

    def __init__(self,first,last,pay,employee=None):
        super().__init__(first,last,pay)
        if employee is None:
            self.employee=[]
        else:
            self.employee=employee

    def add_emp(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emp(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def show(self):
        for emp in self.employee:
            print(emp.fullname())

mgr_1=Manager('Jane','Doe',90000,[dev_1])

print(mgr_1.email)
print(mgr_1.show())
    
print(isinstance(mgr_1,Manager))
print(issubclass(Manager,Employee))