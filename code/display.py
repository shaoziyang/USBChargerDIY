import asyncio
from gv import gv
import oled

def WSecToStr(ws):
    WH = ws/3.6
    if WH<1000:
        return '{:3.0f}mWH'.format(WH)
    elif WH<10000:
        return '{:4.2f}WH'.format(WH/1000)
    elif WH<100000:
        return '{:4.1f}WH'.format(WH/1000)
    else:
        return '{:4.0f}WH'.format(WH/1000)

def SecToStr(sec):
    if sec < 60:
        return ' {:2d} sec'.format(sec)
    elif sec < 3600:
        return '{:2d}M {:2d}S'.format(sec//60, sec%60)
    elif sec < 3600*100:
        return '{:2d}H{}{:02d}M'.format(sec//3600,' ' if sec%2 else ':', (sec%3600)//60)
    else:
        return '100Hour'

# show charge info
async def show_info():

    await asyncio.sleep_ms(100)
    if not gv.selftest:
        return

    print('\nInit OLED I2C 128x32')
    o = oled.OLED_I2C(gv.i2c, 128, 32)
    o.rotate(0)
    o.text_16x32(0,0,'Power ON')
    await asyncio.sleep_ms(2000)
    o.clear()

    gv.DisOn = True
    sec_old = 100

    while True:
        
        if sec_old != gv.rtc_sec:
            sec_old = gv.rtc_sec

            if gv.DisCnt < gv.DISPLAYON_MAX_SEC:
                gv.DisCnt += 1
                
                if not gv.DisOn:
                    gv.DisOn = True
                    o.on()
                    print('Turn on display')

                # show: xx.xV x.xA xx.xC/ -xxC
                if (gv.DisCnt//2)%2:
                    if gv.P > 10:
                        s = '{:4.1f}W'.format(gv.P)
                    else:
                        s = '{:4.2f}W'.format(gv.P)
                else:
                    if gv.T>0:
                        s = '{:4.1f}C'.format(gv.T)
                    else:
                        s = '{:4d}C'.format(gv.T)
                s1 = '{:4.1f}V {:3.1f}A {}'.format(gv.V, gv.C, s)
                o.text_8x16(0, 0, s1)

                # show: xxxxmWH/x.xxWH/xx.xWH xxS/xx
                if gv.DisCnt%2:
                    s2 = WSecToStr(gv.wsec) +' - ' + SecToStr(gv.ch_sec)
                else:
                    s2 = WSecToStr(gv.wsec) +'   ' + SecToStr(gv.ch_sec)
                o.text_8x16(0, 2, s2)

            else:
                if gv.DisOn:
                    gv.DisOn = False
                    o.on(0)
                    print('Turn off display')
             
        await asyncio.sleep_ms(200)


# Using LED colors to represent charging power
async def task_LED():

    LED_color = [[0,1000,0], [500,1000,0], [800,1000,0], [1000,0,0]]
    AL_k = 1
    STEP = 20
    
    await asyncio.sleep_ms(1000)
    
    n = STEP
    while True:
        n = (n+1)%(2*STEP)

        AL_k = min(0.1 + (gv.AL/1500), 1)

        c = LED_color[gv.mc_stat]
        r = round(c[0]*AL_k*abs(n-STEP)/STEP)
        g = round(c[1]*AL_k*abs(n-STEP)/STEP)
        b = round(c[2]*AL_k*abs(n-STEP)/STEP)
        gv.intensity((r,g,b))

        await asyncio.sleep_ms(50)

# touchkey task

async def task_TP():
    
    await asyncio.sleep_ms(1000)
    
    while True:
        
        if gv.TP2():
            gv.LED(1)
            gv.DisCnt = 0
        else:
            gv.LED(0)
            
        await asyncio.sleep_ms(200)