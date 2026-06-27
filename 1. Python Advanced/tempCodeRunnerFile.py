from pydantic import validate_call

@validate_call
def create_user(firstname : str, lastname : str, age : int)->dict:
    email=f"{firstname.lower()}{lastname.lower()}@gmail.com"

    return{
        "First Name" : firstname,
        "Last Name" : lastname,
        "Email" : email,
        "Age" : age,
    }

user1:dict=create_user("Test","User","18")
print(user1)