# global value
#
#

from micropython import const
import asyncio
import board, cfg

class global_var:
    
    DISPLAYON_MAX_SEC = const(60)
    DisCnt = 0
    DisOn = True
    
    selftest = True
    
    i2c = board.i2c
    rtc = board.rtc
    rtc_sec = 0
    
    T = 0
    V = 0
    C = 0
    P = 0
    _P = 0
    
    wsec = 0     # sum of watt/second
    ch_sec = 0   # charge time / seconds
    ch_n = 0     # charge state change count
    ch_s = 0     # charge state
    AL = 0       # Ambient Light
    
    mc_stat = 0  # charge module state
    
    sample_cnt = 0 # sample count

    # sample power multiple times per second
    def sample_power(self):
        self._P += board.ina.power()
        self.sample_cnt += 1
    
    # sample other parameters
    def sample(self):
        self.T = board.T()
        self.AL = (self.AL*3 + board.AL())//4
        self.V = board.ina.volt()
        self.C = board.ina.current()

    # calc power every second
    def calc_power(self):
        self.P = self._P / self.sample_cnt
        self.sample_cnt = 0
        self._P = 0
        if self.P > 6:                # Set mc_stat based on power size
            self.mc_stat = 3
        elif self.P > 2:
            self.mc_stat = 2
        elif self.P > cfg.TH_POWER:
            self.mc_stat = 1
        else:
            self.mc_stat = 0
        
        if self.ch_s:
            self.ch_sec += 1          # Incremental charge time
            self.wsec += self.P       # Accumulated charging power
            if self.mc_stat == 0:
                self.ch_n += 1
                if self.ch_n > 2:     # change charge state
                    self.ch_s = 0     
                    self.DisCnt = 0   # update display time count
                    print('\nstop charge')
                    board.beep(4000,50,1)
            else:
                self.ch_n = 0         # clear count
        else:
            if self.mc_stat > 0:
                self.ch_n += 1
                if self.ch_n > 2:     # change charge state
                    self.ch_s = 1     
                    self.DisCnt = 0   # update display time count
                    self.wsec = 0     # Restart calculation
                    self.ch_sec = 0
                    print('\nstart charge')
                    board.beep(2000,50,1)
            else:
                self.ch_n = 0         # clear count
        

    def TP1(self, th=cfg.TH_TP1):
        return board.TP1(th)

    def TP2(self, th=cfg.TH_TP2):
        return board.TP2(th)

    def LED(self, on):
        board.LED(on)

    def intensity(self, duty=[0,0,0]):
        board.pLEDR.duty(1023-duty[0])
        board.pLEDG.duty(1023-duty[1])
        board.pLEDB.duty(1023-duty[2])

    def beep(self, f=2000, delay=50, cnt=2):
        board.pBEEP.freq(f)
        for i in range(cnt):
            board.pBEEP.duty(500)
            await asyncio.sleep_ms(delay)
            board.pBEEP.duty(0)
            await asyncio.sleep_ms(delay)

gv = global_var()
