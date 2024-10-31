class ubit_memory:
    def __init__(self):
        self.state = 0xBEAD
        
    def __getitem__(self, key):
        if key == 0x50000504 or key == 0x50000510:
            return self.state
        else:
            raise IndexError('Invalid Memory Address')
            
    def __setitem__(self, key, value):
        if value > 0xFFFF or value < 0 or int(value) != value:
            raise ValueError('Must be 16 bit unsigned integer')
        if key == 0x50000504:
            self.state = value
        elif key == 0x50000508:
            self.state |= value
        elif key == 0x5000050C:
            self.state &= ~value
        else:
            raise IndexError('Invalid Memory Address')
            
mem16 = ubit_memory()


