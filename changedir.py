# Python code to change the current working directory
 
import os
 
# Get the current working directory
def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()
 
# Print CWD
current_path()
 
# Changing the current working directory (CWD)
os.chdir('../')
 
# Print CWD
current_path()
