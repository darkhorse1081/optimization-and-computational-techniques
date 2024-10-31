'''
Hardware Lab device driver exercise.

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

def main():
    '''
    Standalone test of device driver.
    '''
    
    display_pixel(2,2)
    microbit.sleep(1000)
    display_pixel(1,1)
    
    '''
    TODO: clear display, wait 1 second, display centre pixel, wait 1 second,
          turn on all pixels, wait 1 second, clear display
    '''

if __name__ == "__main__":
    main()
