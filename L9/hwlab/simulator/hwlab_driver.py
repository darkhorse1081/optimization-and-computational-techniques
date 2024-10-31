'''
Hardware Lab device driver exercise.
Use this version with the simulator only.

Please note that this simulator requires use of asynchronous
programming - microbit.sleep(), microbit.dislay.show(), and 
microbit.display.scroll() must be called with the "await"
keyword, any functions calling these must be declared with the
"async" keyword, and any time you call your own async functions
you also need to use await.

For this assignment, please do not use microbit.sleep() except
within the main() function.

TODO: PLEASE ADD AN APPROPRIATE DESCRIPTION HERE
'''
import machine, microbit

OUT_address = 0x50000504
OUT_SET_address = 0x50000508
OUT_CLEAR_address = 0x5000050C

microbit.display.off()

def clear_display():
    '''
    Turn off all pixels.
    
    TODO: Implement function.
    '''

def illuminate_display():
    '''
    Turn on all pixels.
    
    TODO: Implement function
    '''
    
def display_pixel(row, column):
    '''
    Turn on one specific pixel.
    
    TODO: Implement function
    '''

async def main():
    '''
    Standalone test of device driver.
    '''
    
    display_pixel(2,2)
    await microbit.sleep(1000)
    display_pixel(1,1)
    
    '''
    TODO: clear display, wait 1 second, display centre pixel, wait 1 second,
          turn on all pixels, wait 1 second, clear display
    '''

if __name__ == "__main__":
    await main()
