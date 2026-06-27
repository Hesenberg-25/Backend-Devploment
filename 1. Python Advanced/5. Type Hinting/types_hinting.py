# Before starting the Concept of Type Hinting we need to Understand the some other Concept along with it
# 1. Type Hinting
# 2. Type Checking
# 3. Data Validation

# Type Hinting :
# In this we Add types to Variables, Function Parameters and Return Values
# This increaes Code Readability and Maintainblity
# But the Main part is even if you give the Wrong Datatype fo the Function Paramater it do not throw any Error
# Because the only part of Type Hinting is to Hint towards the Type

def create_user(firstname : str, lastname : str, age : int)->dict:
    email=f"{firstname.lower()}{lastname.lower()}@gmail.com"

    return{
        "First Name" : firstname,
        "Last Name" : lastname,
        "Email" : email,
        "Age" : age,
    }

user1:dict=create_user("Test","User",18)
print(user1)

#Type Checking : (Extensioin : Mypy (MicroSoft))
# Now the work of Type Checking is showing us Error before the Runtime
# If there are any Mismatch is the Type of Enter Data and Type of Function Parameter
# But this do not stops us from displaying the Data
# And also cant point out any Type mismatch from API, Files so we need to use Data-Validation

def create_user1(firstname : str, lastname : str, age : int)->dict:
    email=f"{firstname.lower()}{lastname.lower()}@gmail.com"

    return{
        "First Name" : firstname,
        "Last Name" : lastname,
        "Email" : email,
        "Age" : age,
    }

# user2:dict=create_user2("Test","User","eighteen")
# print(user2)

# Data Validation :
# Data Validation work at Runtime for Verification to check that they meet Requirements
# Pydantic help us Validate the Data but there is a catch it will show Error only if you pass "eighteen" as string and not as "18"
# Because Pydantic can Handle this Error

from pydantic import validate_call

@validate_call
def create_user2(firstname : str, lastname : str, age : int)->dict:
    email=f"{firstname.lower()}{lastname.lower()}@gmail.com"

    return{
        "First Name" : firstname,
        "Last Name" : lastname,
        "Email" : email,
        "Age" : age,
    }

# user3:dict=create_user3("Test","User","eighteen")
# print(user3)