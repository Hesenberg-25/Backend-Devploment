import logging

logger=logging.getLogger(__name__)
# So we use the Dunder method of '__name__' because if we import this code into another Module we will we be able to name the Logger to this Codes files name
# Other if the file is not Imported into another Module it will __main__
# And logger work in Herichey if there is not Logger defined by us it will move back to root Logger

logger.setLevel(logging.INFO)
# Now we have the Severity Level of the Logging to INFO using the logger.setLevel

formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
# Now we have created a Formatter so that we could only get those needed Information

file_handler=logging.FileHandler('emp.log')
# Now we have created a FileHandler so that we can tell the Custom Logger to Log in this file

file_handler.setFormatter(formatter)
# Now we told the file_handler to formatter the Log file according to us by giving the foramtter as input

logger.addHandler(file_handler)
# We have also use logger.addHandler to give input our fileHandler as for the Log file name

# So all the above Custom made Code just help us to make a Logger which does the same Work as the below one just not using the root as Logger
# logging.basicConfig(filename='emp.log',level=logging.INFO,format='%(levelname)s:%(name)s:%(message)s')

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        logger.info(f"Created Employee: {self.fullname} - {self.email}")
        # And we convert logging.info to logger.info for that Specific loggerr to be used as Logger for this logging
    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@gmail.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

emp1 = Employee('Test', 'User')
emp2 = Employee('John', 'Doe')
emp3 = Employee('Jane', 'Doe')