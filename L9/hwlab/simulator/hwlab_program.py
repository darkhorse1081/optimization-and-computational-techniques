'''
Hardware Lab device driver exercise 4.
Use this version with the simulator only.

Please note that the simulator requires use of asynchronous
programming - microbit.sleep(), microbit.dislay.show(), and 
microbit.display.scroll() must be called with the "await"
keyword, any functions calling these must be declared with the
"async" keyword, and any time you call your own async functions
you also need to use await.

Moves a pixel around the display on a micro:bit.
'''

import microbit
#TODO: import device driver

while True:
    for n in range(25):
        x = int(n/5)
        y = n % 5
        #TODO: call function in device driver to light pixel in row x, column y
        await microbit.sleep(500)
    