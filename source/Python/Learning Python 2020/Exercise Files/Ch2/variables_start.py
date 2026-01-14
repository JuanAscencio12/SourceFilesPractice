# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)


# re-declaring the variable works

f="ABC"
print(f)

# ERROR: variables of different types cannot be combined
try:
    print(str(123) + "ads")
except TypeError as e:
    print(e)



# Global vs. local variables in functions
def someFunction():
    global f    
    f="With global you can change a global variable"
    print(f)

someFunction()
print(f)

del f
f = "With del you can delete a definition for a variable that was previously defined"
print(f)