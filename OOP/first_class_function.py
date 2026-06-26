# First class Functions :
# This means that if there is a variable to which we assign like str, int and float
# And in the same way when we assign a Function to the variable
# Then the Function is called First class Function

def square(x):
    return x*x

# Here we have not defined Function Square to the Variable f but we ahve Equalled them
# f=square(5)

# But if we do like :
# f=square
# This means that we are Assigning the Square to f normally like str, int, float
# This will give the Storage postion of the Function as if it is new type of Datatype
# And this is called First Function

# And due to this Reasons we could pass f as parameters or f can be return as statement

# print(f)


def my_map(func,arr):
    result=[]
    for i in arr:
        result.append(func(i))

    return result

squares=my_map(square,[1,2,3,4,5])

print(squares)

# So as Earlier told when a function becomes a First Class Function 
# 1. It can be passed as the Parameter for other function
# And Internally inside the my_map function we are using the Function to get New Set of Values
# 2. A function can calculate something and pass f back as a return statement.
# In the same we could write the Cube function and pass it as the function parameter

def cube(x):
    return x*x*x

def my_map(func,arr):
    result=[]
    for i in arr:
        result.append(func(i))

    return result

cubes=my_map(cube,[1,2,3,4,5])

print(cubes)

# So in below Function what happens is log_hi is Equated to logger Function withsome Argument inside it
# Then aas the inside Function logger_msg is called to returned
# We can see that it is not passed as a Function and due to this log_hi is Equated to logger_msg
# And when log_hi is converted to Function it is then calling logger_msg in form of Function to Execute

def logger(msg):
    def logger_msg():
        print('Log :',msg)

    return logger_msg

log_hi=logger('Hi')
log_hi()


def html_tag(tag):
    def warp_msg(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))

    return warp_msg

print_h1=html_tag('h1')
print_h1('Text!')
