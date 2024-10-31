"""Exercise 1: Button interface and Conditionals"""

# Importing all the necessary functionality from the microbit library
from microbit import button_a, button_b, display, sleep

def main():
    """Main control loop, makes characters display on the microbit"""

    # Initialise the display
    display.clear()

    # A continuous loop
    while True:
        # Slight delay in order to allow the micro:bit to process button presses
        sleep(100)
        # If button A is pressed
        if button_a.was_pressed():
            # Display a corresponding character
            display.show('A')
        # TODO: Otherwise if button B is pressed



if __name__ == "__main__":
    main()
