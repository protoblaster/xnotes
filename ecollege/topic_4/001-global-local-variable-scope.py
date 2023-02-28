spam = 42           # global variable

def eggs():
    spam = 42       # local variable

print('Some code here')
print('Some code here')

# to modify a global variable within a local scope 
# do the following

def func():
    global variableName         # allows us to modify global variable
    variableName = "Hekki"
    print(variableName)

variableName = "Hello"
func()
print(variableName)

# Recap
# - A scope is an area of source code and a container for variables
# - The global scope is code outside a function. Variables stored here are global variables
# - Each funcs code is it's own local scope
# - code in a global scope cannot use local variables
# - If assignment for var in func, that is a local variable
