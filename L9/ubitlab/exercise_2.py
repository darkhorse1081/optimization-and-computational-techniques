"""Exercise 2: Displaying Characters on the micro:bit"""

from microbit import display, button_a, button_b, sleep

def signal_to_ascii(input_signal):
    """Translates the inputs from the buttons to an ascii character"""
    decimal_value = 0
    # TODO: Loop through the list of signals to generate a decimal value

    # Return the ASCII interpretation of that decimal number
    # See https://docs.python.org/3/library/functions.html for 
    # direction
    return chr(decimal_value)


def main():
    """Main control loop of the program"""

    # Initialise the display
    display.clear()

    # Use a list to contain the input signals
    batch_list = [0, 0, 0, 0, 0, 0, 0, 0]
    # Create a counter for the list index
    counter = 0

    # Continuous loop
    while True:

        # Display ASCII character once we have collected enough button inputs
        if counter == 8:
            display_character = signal_to_ascii(batch_list)
            # Signal that we are displaying the result
            display.scroll('=')
            display.show(display_character)
            # Reset the counter
            counter = 0

        # Logic for storing the button presses
        # See https://microbit-micropython.readthedocs.io/en/latest/button.html for direction
        if button_a.was_pressed():
            # The input value at the counter position is zero
            batch_list[counter] = 0
            # Increment the counter
            counter += 1
            # Briefly flash the input to display
            display.clear()
            sleep(150)
            display.show("0")
        # TODO: Implement logic for button_b
        
        # Important - in the simulator, omitting this delay will make your browser tab crash!
        # This delay is not required on the physical micro:bit, since it has nothing better to
        # do than run your code in an infinite loop.
        sleep(100)

if __name__ == "__main__":
    main()
