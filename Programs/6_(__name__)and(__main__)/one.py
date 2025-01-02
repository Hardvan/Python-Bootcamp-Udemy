
# ? __name__ is a built-in variable which evaluates to the name of the current module.
# * The value is set to "__main__" when the module is run as a script.
# * If the module is imported, the value is set to the name of the module.

def fun():
    print("fun() in one.py")


print("TOP LEVEL in one.py")

if __name__ == "__main__":
    print("one.py is being run directly!")
else:
    print(f"one.py has been imported.\n__name__ = {__name__}")
