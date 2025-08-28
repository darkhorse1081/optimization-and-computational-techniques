'''
Moves a pixel around the display on a micro:bit.
'''
import microbit
import hwlab_driver


while True:
    for n in range(25):
        x = int(n/5)
        y = n % 5
        hwlab_driver.display_pixel(x,y)
        microbit.sleep(500)
        hwlab_driver.clear_display()


    