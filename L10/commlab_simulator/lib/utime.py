import time
import microbit

async def sleep(seconds):
    await microbit.sleep(seconds*1000)

async def sleep_ms(ms):
    await microbit.sleep(ms)

async def sleep_us(us):
    await microbit.sleep(us/1000)

def ticks_ms():
    return int(time.monotonic() * 1000)

def ticks_us():
    return int(time.monotonic() * 1e6)

def ticks_diff(time1, time2):
    return time1 - time2

def ticks_add(time1, time2):
    return time1 + time2
