from RPLCD.i2c import CharLCD
from time import sleep
from math import floor



class vlcd:
    TEXT_FIELD = 0
    DATA_FIELD = 1
    LOADING_CHAR = '.'

    def __init__(self,chip_set='PCF8574',max_rows=2,max_cols=16,ic2Address=0x27):
        self._chip_set = chip_set
        self._address = ic2Address
        self._max_rows = max_rows
        self._max_cols = max_cols
        self._data_bar = 0
        
        self._lcd = CharLCD(self._chip_set, self._address)

        self.play_searching("VCOMPY v1.0",char='+')
        sleep(0.1)
    
    def clear():
        self._lcd.clear()


    def write_centred(self,text):
        length = len(text)
        cur_pos = 0

        if length > self._max_cols or length < 0:
            return False
        delta = self._max_cols - length
        if delta != 0:
            cur_pos = int(floor(delta / 2))

        self._lcd.cursor_pos = (self.TEXT_FIELD,cur_pos)
        self._lcd.write_string(text)
        self._lcd.crlf()

        return True

    def write_left(self,text):
        length = len(text)
        cur_pos = 0

        if length > self._max_cols or length < 0:
            return False
        self._lcd.cursor_pos = (self.TEXT_FIELD,cur_pos)
        self._lcd.write_string(text)
        self._lcd.crlf()

        return True
    def play_searching(self, msg, delay=0.1,char='.'):
        i = 7
        j = 8
        self.write_centred(msg)
        sleep(0.5)
        while i >= 0:
           self._lcd.cursor_pos = (1,i)
           self._lcd.write_string(char)
           self._lcd.cursor_pos = (1,j)
           self._lcd.write_string(char)
           i -= 1
           j += 1
           sleep(delay)
        self._lcd.clear()
        
        

    def print_loading_bar(self, percent,char='.'):
        if percent >= 100:
            return True
        if percent <= 0:
            return False
        p = int(percent * self._max_cols / 100)
        prev = self._data_bar
        self._data_bar = p
        if p - prev < 0:
            print(p)
            self._lcd.home()
            self._lcd.cur_pos = (1,p-1)
            self._lcd.write_string("-")
        s = ""
        i = 0
        
        self._lcd.cur_pos = (1, 0)
        
        while i < p:
            s = s + char
            i += 1
        self._lcd.write_string(s)
        return False






# i = 0
# while i < 16:
#     lcd.cursor_pos = (1,i)
#     lcd.write_string('*')
#     sleep(0.2)
#     i += 1
