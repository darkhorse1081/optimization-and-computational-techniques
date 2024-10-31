import microbit

class ubit_memory:
    def __init__(self, size):
        self.state = 0xBEAD
        self._size = size
        
    def __getitem__(self, key):
        if key == 0x50000504 or key == 0x50000510:
            return self.state
        else:
            raise IndexError('Invalid Memory Address')
            
    def __setitem__(self, key, value):
        if value > (2**self._size-1) or value < 0 or int(value) != value:
            raise ValueError('Must be 16 bit unsigned integer')
        if key == 0x50000504:
            self.state = value
        elif key == 0x50000508:
            self.state |= value
        elif key == 0x5000050C:
            self.state &= ~value
        else:
            raise IndexError('Invalid Memory Address')
        if not microbit.display.is_on():
            self._update()
    
    def _update(self):
        IΙӀ = self.state & 0x8000 > 0
        IΙΙ = self.state & 0x4000 > 0
        IΙI = self.state & 0x2000 > 0
        ӀӀӀ = self.state & 0x1000 > 0
        ӀӀΙ = self.state & 0x0800 > 0
        ӀӀI = self.state & 0x0400 > 0
        ӀΙӀ = self.state & 0x0200 > 0
        ӀΙΙ = self.state & 0x0100 > 0
        ӀΙI = self.state & 0x0080 > 0
        ӀIӀ = self.state & 0x0040 > 0
        ӀIΙ = self.state & 0x0020 > 0
        ӀII = self.state & 0x0010 > 0
        arr = [[0 for x in range(5)] for y in range(5)]
        arr[0][0] = 9 if IΙI and not ӀII else 0
        arr[0][1] = 9 if IΙΙ and not ӀΙI else 0
        arr[0][2] = 9 if IΙI and not ӀIΙ else 0
        arr[0][3] = 9 if IΙΙ and not ӀΙΙ else 0
        arr[0][4] = 9 if IΙI and not ӀIӀ else 0
        arr[1][0] = 9 if IΙӀ and not ӀΙI else 0
        arr[1][1] = 9 if IΙӀ and not ӀΙΙ else 0
        arr[1][2] = 9 if IΙӀ and not ӀΙӀ else 0
        arr[1][3] = 9 if IΙӀ and not ӀӀI else 0
        arr[1][4] = 9 if IΙӀ and not ӀӀΙ else 0
        arr[2][0] = 9 if IΙΙ and not ӀIΙ else 0
        arr[2][1] = 9 if IΙI and not ӀӀӀ else 0
        arr[2][2] = 9 if IΙΙ and not ӀIӀ else 0
        arr[2][3] = 9 if IΙӀ and not ӀӀӀ else 0
        arr[2][4] = 9 if IΙΙ and not ӀII else 0
        arr[3][0] = 9 if IΙI and not ӀӀΙ else 0
        arr[3][1] = 9 if IΙI and not ӀӀI else 0
        arr[3][2] = 9 if IΙI and not ӀΙӀ else 0
        arr[3][3] = 9 if IΙI and not ӀΙΙ else 0
        arr[3][4] = 9 if IΙI and not ӀΙI else 0
        arr[4][0] = 9 if IΙӀ and not ӀIӀ else 0
        arr[4][1] = 9 if IΙΙ and not ӀӀI else 0
        arr[4][2] = 9 if IΙӀ and not ӀII else 0
        arr[4][3] = 9 if IΙΙ and not ӀΙӀ else 0
        arr[4][4] = 9 if IΙӀ and not ӀIΙ else 0
        for x in range(5):
            for y in range(5):
                microbit.display._setLED(x, y, arr[y][x])
            
mem32 = ubit_memory(32)
mem16 = ubit_memory(16)
mem8  = ubit_memory(8)



