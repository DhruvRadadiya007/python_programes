# create a virtual python

# create a folder in any drive
# open the folder in cmd
# step 1---> enter the command python -m venv myenv (myenv=name canbe customised)
# step2---> to actiate the virtual python enter the command myenv\Scripts\activate.bat in cmd and .ps1 in powershell
# now you can install modules as per your choice and it will not be installedin the default computer
# any version of module can be installed by givving the version of module at the endfor example:-PIP3 Install pandas==1.4.4
# you can give a custom name to the module while importing the module for example:- import pandas as "name"
# deactivate keyword to disable it

# get all  the papckages and export
# 1->pip freeze to get info of all packages installed
# 2->pip freeze > requirements .txt to make a file of all modules
# 3->pip install -r requirements .txt to import all the modules from the file