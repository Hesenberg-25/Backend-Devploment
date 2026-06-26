# Decorator are the Higher Functions which which takes paramter input as a Function
# Then wraps some Logic around the Function without altering the Original Source Code
# And Returns the New Modified Function

# In Decorator ::
# Outer Function : decorator-func
# Inner Function : wrapper-func


def decorator_function(msg):
    def wrapper_function():
        print(msg)

    return wrapper_function

hi_decorator=decorator_function('Hi')
hi_decorator()

# The above function is sort of a Decorator
# Just Instead of Some Object we need to pass Function

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper Function was Executed before {}".format(original_function.__name__))
        original_function()

    return wrapper_function

def display():
    print("Decorated Function Passed")

decorated_display=decorator_function(display)
decorated_display()

# Now we have Passed some Function as a Parameter and the Function now has become a Decorator

# As you can see the line : print("Wrapper Function was Executed before {}".format(original_function.__name__))
# This is the change which we are making without altering the Source code i.e the function Display
# So we have kept the Source code Intact but we also added some new Functalities along with it

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper Function was Executed before {}".format(original_function.__name__))
        original_function()

    return wrapper_function

@decorator_function
def display():
    print("Decorated Function Passed")

display()

# Now we have use New Functinality "@decorator_function" => @{outerFunction-name}
# This make sure that the work will be as Follow ::

# display=decorated_function(display)
# display()

# This helps we Minimizing the Variable we need to create it same as ::

# decorated_display=decorator_function(display)
# decorated_display()


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper Function was Executed before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Decorated Function Passed")

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments {} {}'.format(name, age))

display_info('Admin', 25)
display()

# In the same way we can use Classes instead for Function

class decorator_class(object):

    def __init__(self,original_function):
        self.original_function=original_function

    def __call__(self,*args,**kwargs):
        print("__call__ method was Executed before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)
    

@decorator_class
def display():
    print("Decorated Function Passed")

@decorator_class
def display_info(name, age):
    print('display_info ran with arguments {} {}'.format(name, age))

display_info('Admin', 25)
display()