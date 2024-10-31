"""
Hardware Lab Testing

This function implements a pytest testing suite for the hardware lab in ENGSCI 233. Its main 
purpose is so you can execute unit tests on your code to ensure you meet the marking requirements.

It comes with a set of mocking modules for the micro:bit that substitute for the functionality 
you would experience on the real hardware device, but work without having one available. Please 
ensure this folder is copied as a subdirectory of your main working directory for the lab.
"""
import sys
from testing_modules import machine, microbit

"""
Here we are setting up the mock libraries so that when we do import our code that would be flashed,
it can actually find and use these modules. We have to make sure Python uses our mock libraries 
instead of looking for official ones with these names.
"""
sys.modules['machine'] = machine
sys.modules['microbit'] = microbit

import hwlab_driver
"""
Note: We need to heed the scope of the modules - we must call prototype.machine, instead of just
machine, even though they point to the same module, because there is a prototype scope that contains
its own machine module.

Also note we have only tested happy paths (ideal/standard inputs) here.
"""

OUT_address = 0x50000504

def test_clear():
    hwlab_driver.machine.mem16[OUT_address] = 0xBEAD
    hwlab_driver.clear_display()
    result = hwlab_driver.machine.mem16[OUT_address]
    assert not hwlab_driver.microbit.display.is_on(), 'Normal display enabled'
    assert result & 0xE000 == 0 or result & 0x1FF0 == 0x1FF0, 'Not turned off'
    assert result & 0x000D == 0x000D, 'Interfered with lowest bits'

def test_illuminate():
    hwlab_driver.machine.mem16[OUT_address] = 0xBEAD
    hwlab_driver.illuminate_display()
    result = hwlab_driver.machine.mem16[OUT_address]
    assert not hwlab_driver.microbit.display.is_on(), 'Normal display enabled'
    assert result & 0xE000 == 0xE000 and result & 0x1FF0 == 0, 'Not turned on'
    assert result & 0x000D == 0x000D, 'Interfered with lowest bits'
    
def test_display():
    correct_table = ['㿠彰㿐廰㾰',
                     '齰黱鷲鯳韴',
                     '忐⿲徴迶忨',
                     '㟰㯳㷶㻹㽼',
                     '龰寴鿨巼鿠']
    for row in range(5):
        for col in range(5):
            hwlab_driver.machine.mem16[OUT_address] = 0xBEAD
            hwlab_driver.display_pixel(row, col)
            result = hwlab_driver.machine.mem16[OUT_address]
            test1 = ord(correct_table[row][col]) - row*col
            test2 = ~(test1 | 0x000F)
            assert not hwlab_driver.microbit.display.is_on(), 'Normal display enabled'
            assert result & test1 == test1 and result & test2 == 0, (row,col)
            assert result & 0x000D == 0x000D, 'Interfered with lowest bits'
