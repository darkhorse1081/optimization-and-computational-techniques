'''
Hardware Lab device driver exercise 4.

Moves a pixel around the display on a micro:bit.
'''

import microbit
#TODO: import device driver

while True:
    for n in range(25):
        x = int(n/5)
        y = n % 5
        #TODO: call function in device driver to light pixel in row x, column y
        microbit.sleep(500)
    