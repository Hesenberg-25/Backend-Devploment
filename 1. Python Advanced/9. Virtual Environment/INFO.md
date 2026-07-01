So in Backend Development most of the Times it happens like our one Project needs suppose python 3.10 and another needs python 3.13

So if we try to Install them Globally they may somwtimes Conflict with each other

So we create a Virtual Environment where we only install those Lib which we want and this Lib installed in this Virtual Env do not create any Conflict with the File outside this Env

And for Every differnt Project we could create different Virtual Env so that None of the Conflict could arise durig the Development and Deployment

So there are some Steps which we need to Follow Creating a Virtual Env doing Development inside it and Deploying the Project

1. We create a Virtual Env by venv
2. Then we create requirements.txt which contains all the needed Lib and there   Version that we have used so that the other devloper can Install the same
3. We also create .env file which contains all our password  which is hidden and only the devloper knoss the password and stuff and which can only be load later use by other Dev

So how to create a Virtual Env ::

1. Go to your desired Folder and copy its Path and go to Command Prompt to to open that path there

2. After that use :: py -{version} -m venv {your-desired-venv-name}

3. Then type 'dir' to know weather the venv is created or not if this shows the venv name somewhere in terminal then venv is created

4. To activate the venv use the command :: {venv-name}\Scripts\activate.bat if it is Activated it will show {(venv-name) path}

5. Then use "where python" or"python --version" to know the python Version

Now if you want to know the Contents just Subjectedd to this venv then use "pip list"

If we want to create the requirement.txt file so that other might able to use the Project use the command "pip freeze" and the Termianl will give you the Lib and there Version

Now if you want to deactivate the venv judt use the command "deactivate"

And to delete the venv first deactivate it then use rmdir /s /p {venv-name}

You can also first Create the Folder for you Project and then give Virtual venv to it
=> "py -{version} -m venv {folder-name}\{venv-name}

If you want to install the requirement.txt file for the venv ::
=> pip install -r requirement.txt