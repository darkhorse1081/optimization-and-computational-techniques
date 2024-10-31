from pyodide.http import pyfetch
from js import document
import utime, random, uuid, json


# Module constants
RATE_250KBIT = 1
RATE_1MBIT = 2
RATE_2MBIT = 4

# Private state
class _internalStatus():
    def __init__(self):
        self.powered = False
        self.length = 32
        self.identity = str(uuid.uuid4())
_rad = _internalStatus()
_probability = 0.25

# Exported functions

async def on():
    _rad.powered = True
    data = {'command': 'register', 'id':_rad.identity}
    response = await pyfetch('radio.queue', method='POST', body=bytes(json.dumps(data), 'utf-8'))
    if response.status != 201:
        raise RuntimeError('Bad HTTP response')

def off():
    _rad.powered = False

def config(**kwargs):
    if 'length' in kwargs:
        length = kwargs['length']
        if length > 0 and length <= 251:
            _rad.length = length
        else:
            raise ValueError('value out of range for argument "length"')

def reset():
    _rad.length = 32

async def send_bytes(msg):
    if not _rad.powered:
        raise ValueError('radio is not enabled') # Not a great error type, but the micro:bit uses it...
    if type(msg) is not bytes:
        raise TypeError('send_bytes() only sends bytes objects.')
    if document.getElementById("flag1").innerHTML == "NOISE":
        if random.random() < _probability:
            print('Packet dropped due to noise')
            return
    if len(msg) > _rad.length:
        msg = msg[0:_rad.length] # Silent truncation is the behaviour on the micro:bit
        
    data = {'command':'add', 'message':msg.hex()} # Can't actually send bytes object in JSON, so send hex representation
    response = await pyfetch('radio.queue', method='POST', body=bytes(json.dumps(data), 'utf-8'))
    if response.status != 201:
        raise RuntimeError('Bad HTTP response')

async def send(message):
    await send_bytes(b'\x01\x00\x01' + bytes(message, 'UTF-8'))

async def receive_bytes():
    if not _rad.powered:
        raise ValueError('radio is not enabled') # Not a great error type, but the micro:bit uses it...
    data = {'command': 'read', 'id':_rad.identity}
    response = await pyfetch('radio.queue', method='POST', body=bytes(json.dumps(data), 'utf-8'))
    if response.status != 200:
        raise RuntimeError('Bad HTTP response')
    data = await response.json()
    message = data['result']
    if not message:
        return None
    msg = bytes.fromhex(message)
    if len(msg) > _rad.length:
        msg = msg[0:rad.length] # Hardware buffer overrun should discard extra
    if document.getElementById("flag1").innerHTML == "NOISE":
        if random.random() < _probability:
            print('Packet lost due to noise')
            return None
    return msg

async def receive():
    msg = await receive_bytes()
    if not msg:
        return None
    if len(msg) < 4:
        return None 
    if msg[0] == 1 and msg[1] == 0 and msg[2] == 1:
        return str(msg[3:], 'UTF-8')
    else:
        raise ValueError('received packet is not a string') # Odd behaviour, but it's what the hardware does

async def receive_bytes_into(buffer):
    raise NotImplementedError

async def receive_full():
    raise NotImplementedError


