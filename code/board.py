from machine import Pin, PWM, ADC, SoftI2C, TouchPad, RTC
import pins, cfg
from time import sleep_ms
import ina219

rtc = RTC()
i2c = SoftI2C(scl=Pin(pins.pin_SCL), sda=Pin(pins.pin_SDA))

aV1 = ADC(Pin(pins.pin_VIN1), atten=ADC.ATTN_11DB)
aT1 = ADC(Pin(pins.pin_T1), atten=ADC.ATTN_11DB)
aAL = ADC(Pin(pins.pin_AL), atten=ADC.ATTN_11DB)

pBEEP = PWM(Pin(pins.pin_BEEP), duty=0)
pLEDR = PWM(Pin(pins.pin_LEDR), duty=1023)
pLEDG = PWM(Pin(pins.pin_LEDG), duty=1023)
pLEDB = PWM(Pin(pins.pin_LEDB), duty=1023)

LED = Pin(pins.pin_LED, Pin.OUT)

tP1 = TouchPad(Pin(pins.pin_TOUCH1))
tP2 = TouchPad(Pin(pins.pin_TOUCH2))

import math

def NTC_GND(adc, max=3300, B=3950):
    t1 = math.log(adc/(max-adc))/B + 1/298.15
    return 1/t1 - 273.15

def V():
    return aV1.read_uv()*11/1000000

def T():
    return NTC_GND(aT1.read_uv()//1000)

def AL():
    return aAL.read_uv()//1000

def beep(freq=4000, delay=50, cnt=2):    
    pBEEP.freq(freq)
    for i in range(cnt):
        pBEEP.duty(500)
        sleep_ms(delay)
        pBEEP.duty(0)
        sleep_ms(delay)

def TP1(th=cfg.TH_TP1):
    return tP1.read() > th

def TP2(th=cfg.TH_TP2):
    return tP2.read() > th

ina = ina219.INA219(i2c)
ina.calreg(cfg.INA219_CAL_REG)