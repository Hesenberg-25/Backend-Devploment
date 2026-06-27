# In higher other function Free Variable is defined as the Variable
# Which is not defined in the Function but can be Assced

# A Closure is a Inner Function of a Higher order Function
# Which has Asscees to the Local Variable even if the Outer Function Excution is Done

def outer_func(msg):
    message=msg
    def inner_func():
        print(message)

    return inner_func

hi_func=outer_func('Hi')
hello_func=outer_func('Hello')

hi_func()
hello_func()

# So we can say that Closure closes the Free Variable present in there Env