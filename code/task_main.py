# task_main.py
#
#   part of USB Charger DIY project
#
#   https://github.com/shaoziyang/USBChargerDIY

import asyncio
from gv import gv
import board
from time import sleep_ms

def selftest():
    
    print('start self testing...')
    result = True

    print('\ncheck I2C')
    r = board.i2c.scan()
    if not ((60 in r) and (64 in r)):
        print('I2C device error', r)
        result = False
    else:
        print('  ok')

    if result:
        print('\nself test ok!')
        board.beep()
    else:
        print('\nself test fail!')
        board.beep(2000,80,3)

    gv.selftest = result

async def main():
    
    print('\System start...')
    
    selftest()
    
    if not gv.selftest:
        while True:
            board.pLEDR.duty(0)
            await asyncio.sleep_ms(200)
            board.pLEDR.duty(1023)
            await asyncio.sleep_ms(500)
    
    # sample
    sec = 100
    
    while True:
        
        gv.sample_power()
        
        d = gv.rtc.datetime()
        if gv.rtc_sec != d[6]:
            gv.rtc_sec = d[6]
            gv.sample()
            gv.calc_power()
            print('{:4.1f}V {:3.1f}A {:4.1f}W {:4.1f}C {:8.2f}ws {}s {}'.format(gv.V, gv.C, gv.P, gv.T, gv.wsec,gv.ch_sec, gv.AL))

        await asyncio.sleep_ms(100)
