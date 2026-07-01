# A logger is a named object provided by Python’s built-in logging module that acts as the direct interface for recording messages from your application.
# Instead of printing raw text to the screen like print(), a logger categorizes events by importance (severity levels) and routes them to specified destinations—like the console, a local text file, or an external server.


import logging
import employee

# logging.basicConfig(filename='sample.log',level=logging.DEBUG,format='%(asctime)s:%(filename)s:%(levelname)s:%(message)s')

# def addition(x:int,y:int):
#     return x+y
# def subtraction(x:int,y:int):
#     return x-y
# def multiplication(x:int,y:int):
#     return x*y
# def divide(x:int,y:int):
#     return x/y

# num1=10
# num2=5

# add_res=addition(num1,num2)
# logging.debug("Addition of {} and {} is {}".format(num1,num2,add_res))
# sub_res=subtraction(num1,num2)
# logging.debug("Subtraction of {} and {} is {}".format(num1,num2,sub_res))
# mul_res=multiplication(num1,num2)
# logging.debug("Multiplication of {} and {} is {}".format(num1,num2,mul_res))
# div_res=divide(num1,num2)
# logging.debug("Division of {} and {} is {}".format(num1,num2,div_res))


# # 1. So after running the Above code we can see that the only emp.log file is gererated not the sample.log 
# # 2. We have Set the Severity level to Info of the Defualt logger root which is Singleton and cant be changed
# # 3. But if we convert the logging.debug to logging.issue the emp.log file will Log the Operarions Snippet

# add_res=addition(num1,num2)
# logging.info("Addition of {} and {} is {}".format(num1,num2,add_res))
# sub_res=subtraction(num1,num2)
# logging.info("Subtraction of {} and {} is {}".format(num1,num2,sub_res))
# mul_res=multiplication(num1,num2)
# logging.info("Multiplication of {} and {} is {}".format(num1,num2,mul_res))
# div_res=divide(num1,num2)
# logging.info("Division of {} and {} is {}".format(num1,num2,div_res))

# So to overcome this we use the concept of Logger, Handler and Formatters
# So how we create a Custom logger first wee need to go thought the employee.py file

logger=logging.getLogger('__name__')
# 1. Created a Logger

logger.setLevel(logging.DEBUG)
# 2. Set its Level

operation_handler=logging.FileHandler('sample.log')
# 3. Created a file Handler

operation_formatter=logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
# 4. Created a Formatter for the Log

operation_handler.setFormatter(operation_formatter)
# 5. Set the Formatter to the Handler

logger.addHandler(operation_handler)
# 6. Added the file Handler to the Logger

stream_handler=logging.StreamHandler()
# => When we want to Display the content which we store in our Log file in our Terminal we could use stream_handler
stream_handler.setFormatter(operation_formatter)
# => When have also set the format for the Terminal Display
logger.addHandler(stream_handler)
# => When have add the Handler to the logger

# And all is same as :
# logging.basicConfig(filename='sample.log',level=logging.DEBUG,format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')



def addition(x:int,y:int):
    return x+y
def subtraction(x:int,y:int):
    return x-y
def multiplication(x:int,y:int):
    return x*y
def divide(x:int,y:int):
    try:
        result=x/y
    except ZeroDivisionError:
        logger.error('Divison by Zero')
        # We can also print the Traceback Error
        logger.exception('Division by Zero')
    else:
        return result

num1=10
num2=0

add_res=addition(num1,num2)
logger.debug("Addition of {} and {} is {}".format(num1,num2,add_res))

sub_res=subtraction(num1,num2)
logger.debug("Subtraction of {} and {} is {}".format(num1,num2,sub_res))

mul_res=multiplication(num1,num2)
logger.debug("Multiplication of {} and {} is {}".format(num1,num2,mul_res))

div_res=divide(num1,num2)
logger.debug("Division of {} and {} is {}".format(num1,num2,div_res))


