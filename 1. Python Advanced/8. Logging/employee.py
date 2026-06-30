import logging

logging.basicConfig(filename='emp.log',level=logging.INFO,force=True,format='%(levelname)s:%(message)s')

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # print(f"Created Employee: {self.fullname} - {self.email}")
        logging.info(f"Created Employee: {self.fullname} - {self.email}")
    
    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@gmail.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

emp1 = Employee('Test', 'User')
emp2 = Employee('John', 'Doe')
emp3 = Employee('Jane', 'Doe')