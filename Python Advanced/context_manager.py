# Context Manger handles the Tear Down of Code in program
# So that there is no need to do it Manually by us

# This can used to many Cases :
# 1. Close the opened Databases Automatically
# 2. Connect Databases

# In this example we are closing the Database Manually 
f=open('sample.txt','w')
f.write("Hi there")
# f.closed tells us if the file is closed or not
print(f.closed) # -> False
f.close()
print(f.closed) # -> True


# But in this method we are using context manager 'with'
# Which automatically closes the Database after it's work is done
with open('sample.txt','w') as f:
    f.write("Hi") 
print(f.closed)


# Creating own Context Manager using Class

class object_class:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode

    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file
    
    # Returning the self.file ensures that we are pointing to a Object created during the class
    # Here it the keyword 'f'
    
    def __exit__(self, exc_type, exc, tb):
        self.file.close()

with object_class('sample.txt','w') as f:
    f.write("Hello World")

print(f.closed)

# Creating own Context Manager using Function, Decorator, Generator
from contextlib import contextmanager

@contextmanager
def open_file(filename,mode):
    try:
        f=open(filename,mode)
        yield f
    finally:
        f.close()

# Here everything before f.close() is working as the __enter__ dunder
# f.close() is like the __exit__ dunder

# Using the try and finally block we are trying close the Program if there is any Error
# This is same as the work of Context Manager trying to close the file if there is an Error

with open_file('sample.txt','w') as f:
    f.write("What to write")
    print(f.closed)
    
print(f.closed)

import os
from contextlib import contextmanager

cwd=os.getcwd()
os.chdir('Sample-1')
print(os.listdir())
os.chdir(cwd)

cwd=os.getcwd()
os.chdir('Sample-2')
print(os.listdir())
os.chdir(cwd)

# So what we are doing here is from the Current directory we are moving to another one
# Then printing the Databases inside it and again shifting to the previous cureent Directory
# To perform the same Functinality

# Here it is Isuue to Switch between Back and Forth
# Instend of that we can create Function who cna performs the same
@contextmanager
def changedir(destination):
    try:
        cwd=os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with changedir('Sample-1'):
    print(os.listdir())

with changedir('Sample-2'):
    print(os.listdir())