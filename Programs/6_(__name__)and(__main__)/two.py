import one

print("TOP LEVEL in two.py")

one.fun()

if __name__ == "__main__":
    print("two.py is being run directly!")
else:
    print("two.py has been imported.")
