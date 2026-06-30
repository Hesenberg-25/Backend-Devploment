logging.basicConfig(filename='sample.log',level=logging.DEBUG,format='%(asctime)s:%(filename)s:%(levelname)s:%(message)s')

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