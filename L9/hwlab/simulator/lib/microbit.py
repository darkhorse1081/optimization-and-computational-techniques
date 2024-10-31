from js import document
from pyodide import create_proxy
import asyncio, time

def _block_sleep(milliseconds):
    start = time.monotonic()
    while time.monotonic() < (start + milliseconds/1000):
        if document.getElementById("flag").innerHTML == "STOP":
            raise KeyboardInterrupt

class Button():
    def __init__(self, parent=None):
        self.pressed = False
        self.press_history = False
        self.presses = 0
        
    def press(self, *args):
        self.pressed = True
        self.press_history = True
        self.presses += 1
        
    def unpress(self, *args):
        self.pressed = False

    def is_pressed(self):
        state = self.pressed
        return state

    def was_pressed(self):
        state = self.press_history
        self.press_history = False
        return state

    def get_presses(self):
        state = self.presses
        self.presses = 0
        return state

button_a = Button()
button_b = Button()
proxy_btn_a_dn = create_proxy(button_a.press)
proxy_btn_a_up = create_proxy(button_a.unpress)
proxy_btn_b_dn = create_proxy(button_b.press)
proxy_btn_b_up = create_proxy(button_b.unpress)
document.getElementById("mb_btn_A").addEventListener('mousedown', proxy_btn_a_dn)
document.getElementById("mb_btn_A").addEventListener('mouseup', proxy_btn_a_up)
document.getElementById("mb_btn_B").addEventListener('mousedown', proxy_btn_b_dn)
document.getElementById("mb_btn_B").addEventListener('mouseup', proxy_btn_b_up)

async def sleep(milliseconds):
    await asyncio.sleep(milliseconds/1000)
    if document.getElementById("flag").innerHTML == "STOP":
        raise KeyboardInterrupt
        
class Display():
    _power = True
    _leds = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    _letters = {
        'A': [" 99  ",
            "9  9 ",
            "9999 ",
            "9  9 ",
            "9  9 "],

        'B': ["999  ",
            "9  9 ",
            "999  ",
            "9  9 ",
            "999  "],

        'C': [" 9999",
            "9    ",
            "9    ",
            "9    ",
            " 9999"],

        'D': ["9999 ",
            "9   9",
            "9   9",
            "9   9",
            "9999 "],

        'E': ["99999",
            "9    ",
            "99999",
            "9    ",
            "99999"],

        'F': ["99999",
            "9    ",
            "9999 ",
            "9    ",
            "9    "],

        'G': [" 9999",
            "9    ",
            "9  99",
            "9   9",
            " 9999"],

        'H': ["9   9",
            "9   9",
            "99999",
            "9   9",
            "9   9"],

        'I': [" 999 ",
            "  9  ",
            "  9  ",
            "  9  ",
            " 999 "],

        'J': ["99999",
            "  9  ",
            "  9  ",
            "  9  ",
            "99   "],

        'K': ["9  9 ",
            "9 9  ",
            "99   ",
            "9 9  ",
            "9  9 "],

        'L': ["9    ",
            "9    ",
            "9    ",
            "9    ",
            "99999"],

        'M': [" 9 9 ",
            "9 9 9",
            "9   9",
            "9   9",
            "9   9"],

        'N': ["9   9",
            "99  9",
            "9 9 9",
            "9  99",
            "9   9"],

        'O': [" 999 ",
            "9   9",
            "9   9",
            "9   9",
            " 999 "],

        'P': ["9999 ",
            "9   9",
            "9999 ",
            "9    ",
            "9    "],

        'Q': [" 999 ",
            "9   9",
            "9 9 9",
            "9  9 ",
            " 99 9"],

        'R': ["9999 ",
            "9   9",
            "9999 ",
            "9 9  ",
            "9  9 "],

        'S': ["99999",
            "9    ",
            "99999",
            "    9",
            "99999"],

        'T': ["99999",
            "  9  ",
            "  9  ",
            "  9  ",
            "  9  "],

        'U': ["9   9",
            "9   9",
            "9   9",
            "9   9",
            " 999 "],

        'V': ["9   9",
            "9   9",
            " 9 9 ",
            " 9 9 ",
            "  9  "],

        'W': ["9   9",
            "9   9",
            "9   9",
            "9 9 9",
            " 9 9 "],

        'X': ["9   9",
            " 9 9 ",
            "  9  ",
            " 9 9 ",
            "9   9"],

        'Y': ["9   9",
            " 9 9 ",
            "  9  ",
            " 9   ",
            "9    "],

        'Z': ["99999",
            "   9 ",
            "  9  ",
            " 9   ",
            "99999"],



        'a':	[" 999 ",
             "    9",
             " 9999",
             "9   9",
             " 9999"],

        'b': [" 9   ",
            " 9   ",
            " 999 ",
            " 9  9",
            " 999 "],

        'c': ["     ",
            "     ",
            " 9999",
            "9    ",
            " 9999"],

        'd': ["    9",
            "    9",
            " 9999",
            "9   9",
            " 999 "],

        'e': [" 99  ",
            "9  9 ",
            "9999 ",
            "9    ",
            " 999 "],

        'f': ["  99 ",
            " 9   ",
            " 999 ",
            " 9   ",
            " 9   "],

        'g': [" 999 ",
            "9   9",
            " 999 ",
            "   9 ",
            " 99  "],

        'h': ["9    ",
            "9    ",
            "9999 ",
            "9   9",
            "9   9"],

        'i': [" 9   ",
            "     ",
            " 9   ",
            " 9   ",
            " 9   "],

        'j': ["   9 ",
            "     ",
            "   9 ",
            "   9 ",
            "  9  "],

        'k': ["9    ",
            "9    ",
            "9 9  ",
            "99   ",
            "9 9  "],

        'l': ["  9  ",
            "  9  ",
            "  9  ",
            "  9  ",
            "  9  "],

        'm': ["     ",
            "99 9 ",
            "9 9 9",
            "9   9",
            "9   9"],

        'n': ["     ",
            " 99  ",
            "9  9 ",
            "9  9 ",
            "9  9 "],

        'o': ["     ",
            " 999 ",
            "9   9",
            "9   9",
            " 999 "],

        'p': ["     ",
            "999  ",
            "9  9 ",
            "999  ",
            "9    "],

        'q': ["     ",
            " 9999",
            "9   9",
            " 9999",
            "    9"],

        'r': ["     ",
            " 999 ",
            "9    ",
            "9    ",
            "9    "],

        's': [" 999 ",
            "9    ",
            " 999 ",
            "    9",
            "9999 "],

        't': [" 9   ",
            "999  ",
            " 9   ",
            " 9   ",
            "  99 "],

        'u': ["     ",
            "9   9",
            "9   9",
            "9   9",
            " 999 "],

        'v': ["     ",
            "     ",
            "9   9",
            " 9 9 ",
            "  9  "],

        'w': ["     ",
            "     ",
            "9 9 9",
            " 9 9 ",
            " 9 9 "],

        'x': ["     ",
            "9  9 ",
            " 99  ",
            " 99  ",
            "9  9 "],

        'y': ["     ",
            "9  9 ",
            " 99  ",
            "  9  ",
            "99   "],

        'z': ["     ",
            "9999 ",
            "  9  ",
            " 9   ",
            "9999 "],

        "0": [" 999 ",
              "99  9",
              "9 9 9",
              "9  99",
              " 999 "],

        "1": [" 9   ",
              "99   ",
              " 9   ",
              " 9   ",
              "999  "],

        "2": [" 999 ",
              "9   9",
              "   9 ",
              "  9  ",
              " 9999"],

        "3": [" 999 ",
              "9   9",
              "   9 ",
              "9   9",
              " 999 "],

        "4": ["   9 ",
              "  99 ",
              " 9 9 ",
              "99999",
              "   9 "],

        "5": ["99999",
              "9    ",
              "9999 ",
              "    9",
              "9999 "],

        "6": [" 999 ",
              "9    ",
              "9999 ",
              "9   9",
              " 999 "],

        "7": ["99999",
              "   9 ",
              "  9  ",
              " 9   ",
              "9    "],

        "8": [" 999 ",
              "9   9",
              " 999 ",
              "9   9",
              " 999 "],

        "9": [" 999 ",
              "9  9 ",
              " 999 ",
              "   9 ",
              "  9  "],

        '!':	["  9  ",
                 "  9  ",
                 "  9  ",
                 "     ",
                 "  9  "],
        '"':	[" 9 9 ",
                 " 9 9 ",
                 "     ",
                 "     ",
                 "     "],

        '£':	["   99",
                 "  9  ",
                 " 9999",
                 " 9   ",
                 "9 999"],

        '$':	[" 9999",
                 "9 9  ",
                 " 999 ",
                 "  9 9",
                 "9999 "],

        '%':	["99  9",
                 "99 9 ",
                 "  9  ",
                 " 9 99",
                 "9  99"],

        '^':	["  9  ",
                 " 9 9 ",
                 "     ",
                 "     ",
                 "     "],

        '&':	[" 999 ",
                 " 9 9 ",
                 " 99  ",
                 "9  9 ",
                 " 99 9"],

        '*':	["9 9 9",
                 " 999 ",
                 "9 9 9",
                 " 999 ",
                 "9 9 9"],
        '(':	["  9  ",
                 " 9   ",
                 " 9   ",
                 " 9   ",
                 "  9  "],

        ')':	["  9  ",
                 "   9 ",
                 "   9 ",
                 "   9 ",
                 "  9  "],

        '[':	[" 999 ",
                 " 9   ",
                 " 9   ",
                 " 9   ",
                 " 999 "],

        ']':	[" 999 ",
                 "   9 ",
                 "   9 ",
                 "   9 ",
                 " 999 "],

        '{':	["  99 ",
                 " 9   ",
                 "  9  ",
                 " 9   ",
                 "  99 "],

        '}':	[" 99  ",
                 "   9 ",
                 "  9  ",
                 "   9 ",
                 " 99  "],

        '@':	[" 999 ",
                 "9   9",
                 "9 999",
                 "9 9 9",
                 "99999"],

        "'":	["  9  ",
                 "     ",
                 "     ",
                 "     ",
                 "     "],

        '~':	["     ",
                 " 99 9",
                 "   9 ",
                 "     ",
                 "     "],

        ':':	["     ",
                 "  9  ",
                 "     ",
                 "  9  ",
                 "     "],

        '#':	[" 9 9 ",
                 "99999",
                 " 9 9 ",
                 "99999",
                 " 9 9 "],

        '/':	["    9",
                 "   9 ",
                 "  9  ",
                 " 9   ",
                 "9    "],

        '\\':	["9    ",
                 " 9   ",
                 "  9  ",
                 "   9 ",
                 "    9"],

        '?':	["9999 ",
                 "   9 ",
                 "  99 ",
                 "     ",
                 "  9  "],

        '.':	["     ",
                 "     ",
                 "     ",
                 "     ",
                 "  9  "],

        ',':	["     ",
                 "     ",
                 "     ",
                 "   9 ",
                 "  9  "],

        '<':	["   9 ",
                 "  9  ",
                 " 9   ",
                 "  9  ",
                 "   9 "],

        '>':	[" 9   ",
                 "  9  ",
                 "   9 ",
                 "  9  ",
                 " 9   "],

        ' ':	["     ",
                 "     ",
                 "     ",
                 "     ",
                 "     "],

        '-':	["     ",
                 "     ",
                 "99999",
                 "     ",
                 "     "],

        '+':	["  9  ",
                 "  9  ",
                 "99999",
                 "  9  ",
                 "  9  "],

        '_':	["     ",
                 "     ",
                 "     ",
                 "     ",
                 "99999"],


        '=':	["     ",
                 "99999",
                 "     ",
                 "99999",
                 "     "],
    }
    
    def _setLED(self, x, y, brightness):
        led_name = 'mb_led_row_' + str(y) + '.mb_led_col_' + str(x)
        if isinstance(brightness, str):
            if brightness.isnumeric():
                brightness = int(brightness)
            else:
                brightness = 0
        elif isinstance(brightness, float):
            brightness = int(brightness)
        elif isinstance(brightness, int):
            pass
        else:
            raise TypeError
        if brightness > 9:
            brightness = 9
        elif brightness < 0:
            brightness = 0
        brightness_list = ['mb_led_brightness_0',
                           'mb_led_brightness_1',
                           'mb_led_brightness_2',
                           'mb_led_brightness_3',
                           'mb_led_brightness_4',
                           'mb_led_brightness_5',
                           'mb_led_brightness_6',
                           'mb_led_brightness_7',
                           'mb_led_brightness_8',
                           'mb_led_brightness_9']
        brightness_class = 'mb_led_brightness_' + str(brightness)
        active_led = document.getElementById(led_name).classList
        for z in brightness_list:
            active_led.remove(z)
        active_led.add(brightness_class)
        self._leds[y][x] = brightness
        
    def _showCharacter(self, c):
        if c not in self._letters:
            letter = self._letters['?']
        else:
            letter = self._letters[c]
        for x in range(5):
            for y in range(5):
                bright = letter[y][x]
                self._setLED(x, y, bright)
                
    def __init__(self, parent = None):
        self.on()
        self.clear()
        
    def get_pixel(self, x, y):
        return self._leds[y][x]
        
    def set_pixel(self, x, y, brightness):
        self._setLED(x, y, brightness)
        
    def clear(self):
        for x in range(5):
            for y in range(5):
                self._setLED(x, y, 0)
                
    def on(self):
        self._power = True
        
    def off(self):
        self.clear()
        self._power = False
        
    def is_on(self):
        return self._power
        
    def read_light_level(self):
        raise NotImplementedError
                
    async def show(self, image, delay=400, wait=True, loop=False, clear=False):
        if not wait:
            print("Asynchronous mode not supported.")
            wait = True
        if loop:
            print("Looping not supported.")
            loop = False
        if isinstance(image, (list, tuple)):
            for x in image:
                await self.show(x, delay, wait=wait, loop=False, clear=clear)
                if len(image)>1:
                    await sleep(delay)
        elif isinstance(image, int):
            await self.show(str(image), delay=delay, wait=wait, loop=loop, clear=clear)
        elif isinstance(image, str):
            if len(image) == 1:
                self._showCharacter(image)
            else:
                img = list(image)
                await self.show(img, delay=delay, wait=wait, loop=loop, clear=clear)
        elif isinstance(image, Image):
            for x in range(5):
                for y in range(5):
                    self._setLED(x, y, image.lines[y][x])
        else:
            raise TypeError
        if clear:
            self.clear()
    
    async def scroll(self, value, delay=150, wait=True, loop=False, monospace=False):
        if not wait:
            print("Asynchronous mode not supported.")
            wait = True
        if loop:
            print("Looping not supported.")
            loop = False
        if not monospace:
            spacer = ' '
        else:
            spacer = ''
        if isinstance(value, (int, float)):
            msg = str(value)
        elif isinstance(value, str):
            msg = value
        else:
            raise TypeError
        # Build main data
        rows = ['', '', '', '', '']
        for x in msg:
            try:
                letter = self._letters[x]
            except:
                letter = self._letters['?']
            for y in range(5):
                rows[y] += letter[y] + spacer
        # Display
        for offset in range(len(rows[0])-5):
            for y in range(5):
                for x in range(5):
                    self._setLED(x,y,rows[y][x+offset])
            await sleep(delay)
                
display = Display()

class Image():
    def __init__(self, string=''):
        if string == '':
            string = "00000:00000:00000:00000:00000"
        self.lines = string.split(':')

Image.HEART = Image("09090:99999:99999:09990:00900:")
Image.HEART_SMALL = Image("00000:09090:09990:00900:00000:")
Image.HAPPY = Image("00000:09090:00000:90009:09990:")
Image.SMILE = Image("00000:00000:00000:90009:09990:")
Image.SAD = Image("00000:09090:00000:09990:90009:")
Image.CONFUSED = Image("00000:09090:00000:09090:90909:")
Image.ANGRY = Image("90009:09090:00000:99999:90909:")
Image.ASLEEP = Image("00000:99099:00000:09990:00000:")
Image.SURPRISED = Image("09090:00000:00900:09090:00900:")
Image.SILLY = Image("90009:00000:99999:00909:00999:")
Image.FABULOUS = Image("99999:99099:00000:09090:09990:")
Image.MEH = Image("09090:00000:00090:00900:09000:")
Image.YES = Image("00000:00009:00090:90900:09000:")
Image.NO = Image("90009:09090:00900:09090:90009:")
Image.CLOCK12 = Image("00900:00900:00900:00000:00000:")
Image.CLOCK1 = Image("00090:00090:00900:00000:00000:")
Image.CLOCK2 = Image("00000:00099:00900:00000:00000:")
Image.CLOCK3 = Image("00000:00000:00999:00000:00000:")
Image.CLOCK4 = Image("00000:00000:00900:00099:00000:")
Image.CLOCK5 = Image("00000:00000:00900:00090:00090:")
Image.CLOCK6 = Image("00000:00000:00900:00900:00900:")
Image.CLOCK7 = Image("00000:00000:00900:09000:09000:")
Image.CLOCK8 = Image("00000:00000:00900:99000:00000:")
Image.CLOCK9 = Image("00000:00000:99900:00000:00000:")
Image.CLOCK10 = Image("00000:99000:00900:00000:00000:")
Image.CLOCK11 = Image("09000:09000:00900:00000:00000:")
Image.ARROW_N = Image("00900:09990:90909:00900:00900:")
Image.ARROW_NE = Image("00999:00099:00909:09000:90000:")
Image.ARROW_E = Image("00900:00090:99999:00090:00900:")
Image.ARROW_SE = Image("90000:09000:00909:00099:00999:")
Image.ARROW_S = Image("00900:00900:90909:09990:00900:")
Image.ARROW_SW = Image("00009:00090:90900:99000:99900:")
Image.ARROW_W = Image("00900:09000:99999:09000:00900:")
Image.ARROW_NW = Image("99900:99000:90900:00090:00009:")
Image.TRIANGLE = Image("00000:00900:09090:99999:00000:")
Image.TRIANGLE_LEFT = Image("90000:99000:90900:90090:99999:")
Image.CHESSBOARD = Image("09090:90909:09090:90909:09090:")
Image.DIAMOND = Image("00900:09090:90009:09090:00900:")
Image.DIAMOND_SMALL = Image("00000:00900:09090:00900:00000:")
Image.SQUARE = Image("99999:90009:90009:90009:99999:")
Image.SQUARE_SMALL = Image("00000:09990:09090:09990:00000:")
Image.RABBIT = Image("90900:90900:99990:99090:99990:")
Image.COW = Image("90009:90009:99999:09990:00900:")
Image.MUSIC_CROTCHET = Image("00900:00900:00900:99900:99900:")
Image.MUSIC_QUAVER = Image("00900:00990:00909:99900:99900:")
Image.MUSIC_QUAVERS = Image("09999:09009:09009:99099:99099:")
Image.PITCHFORK = Image("90909:90909:99999:00900:00900:")
Image.XMAS = Image("00900:09990:00900:09990:99999:")
Image.PACMAN = Image("09999:99090:99900:99990:09999:")
Image.TARGET = Image("00900:09990:99099:09990:00900:")
Image.TSHIRT = Image("99099:99999:09990:09990:09990:")
Image.ROLLERSKATE = Image("00099:00099:99999:99999:09090:")
Image.DUCK = Image("09900:99900:09999:09990:00000:")
Image.HOUSE = Image("00900:09990:99999:09990:09090:")
Image.TORTOISE = Image("00000:09990:99999:09090:00000:")
Image.BUTTERFLY = Image("99099:99999:00900:99999:99099:")
Image.STICKFIGURE = Image("00900:99999:00900:09090:90009:")
Image.GHOST = Image("99999:90909:99999:99999:90909:")
Image.SWORD = Image("00900:00900:00900:09990:00900:")
Image.GIRAFFE = Image("99000:09000:09000:09990:09090:")
Image.SKULL = Image("09990:90909:99999:09990:09990:")
Image.UMBRELLA = Image("09990:99999:00900:90900:09900:")
Image.SNAKE = Image("99000:99099:09090:09990:00000:")

Image.ALL_CLOCKS = [Image.CLOCK1, Image.CLOCK2, Image.CLOCK3, Image.CLOCK4,
                    Image.CLOCK5, Image.CLOCK6, Image.CLOCK7, Image.CLOCK8,
                    Image.CLOCK9, Image.CLOCK10, Image.CLOCK11, Image.CLOCK12]
Image.ALL_ARROWS = [Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE,
                    Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW]