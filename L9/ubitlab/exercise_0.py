"""Exercise 0 - Hello, World!"""

# An import statement - we are adding logic from the display module of the microbit library to this code
from microbit import display

# Our function that is called
def main():
    # See https://microbit-micropython.readthedocs.io/en/v1.0.1/display.html
    display.scroll("Hello, World!")

# This is a standard Python construction, and states that if this script is being called as the
# primary script then execute the following commands
if __name__ == "__main__":
    # Call the above function
    main()
