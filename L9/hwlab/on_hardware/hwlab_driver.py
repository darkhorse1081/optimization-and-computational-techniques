import machine, microbit

OUT_address = 0x50000504
OUT_SET_address = 0x50000508
OUT_CLEAR_address = 0x5000050C

grid = [[(1,1),(2,4),(1,2),(2,5),(1,3)],
[(3,4),(3,5),(3,6),(3,7),(3,8)],
[(2,2),(1,9),(2,3),(3,9),(2,1)],
[(1,8),(1,7),(1,6),(1,5),(1,4)],
[(3,3),(2,7),(3,1),(2,6),(3,2)]]

microbit.display.off()

def bits_to_hex_string(bit_list):
  """
  Converts a list of bits (0s and 1s) into a hexadecimal string.

  Args:
    bit_list: A list of integers, where each is either 0 or 1.

  Returns:
    A string representing the hexadecimal value, e.g., "0x1e0f".
  """
  binary_string = "".join(str(bit) for bit in bit_list)
  integer_value = int(binary_string, 2)
  hex_value = hex(integer_value)

  return hex_value

def clear_display():
    '''
    Turn off all pixels.
    '''
    machine.mem16[OUT_address] = 0x1FF0
    return

def illuminate_display():
    '''
    Turn on all pixels.
    '''
    machine.mem16[OUT_address] = 0xE000
    return
    
def display_pixel(row, column):
    '''
    Turn on one specific pixel.
    '''
    Bit_PowerPins = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # MSB extreme right + LSB extreme left 
    Bit_GNDPins = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # identification of power/gnd pins
    led_val = grid[row][column]

    # power pin rewrite bit_default
    pw_index = 3
    for i in range(0,3):
        if led_val[0] == pw_index:
            Bit_PowerPins[i] = 1
            # eg -> 2[p] -> active high
            hex_pw = bits_to_hex_string(Bit_PowerPins)
            machine.mem16[OUT_SET_address] = int(hex_pw, 16) # OUT_SET_address -> 1 in P pin 2
            break
        else:
            pw_index = pw_index - 1
        
    gnd_index = 9
    for j in range(0,10):  
        if led_val[-1] == gnd_index:
            Bit_GNDPins[j+3] = 1
            # 2[gnd] -> active low
            hex_gnd = bits_to_hex_string(Bit_GNDPins)
            machine.mem16[OUT_CLEAR_address] = int(hex_gnd, 16) # OUT_CLEAR_address -> 1 in G pin 2
            break
        else:
            gnd_index = gnd_index - 1

    return
            
def main():
    '''
    Standalone test of device driver.
    '''
    display_pixel(2,2)
    microbit.sleep(1000)
    display_pixel(1,1)
    microbit.sleep(1000)
    clear_display()
    microbit.sleep(1000)
    display_pixel(2,2)
    microbit.sleep(1000)
    illuminate_display()
    microbit.sleep(1000)
    clear_display()

if __name__ == "__main__":
    main()
