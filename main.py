from vlcd import vlcd
from vobd import vobd
from time import sleep
from threading import Thread

isRunning = False
lcd = ""
obd = ""
gps = ""

def start_lcd():
    global lcd
    global isRunning
    lcd = vlcd()
    while isRunning == False:
        lcd.play_searching("Initialising")

        

def start_obd():
    global isRunning
    global lcd
    obd = vobd()
    isRunning = True
    sleep(2)
    idle = 900
    warning = 4500
    red = 6500
    maxrpm = 7500
    nil = 0
    while isRunning:
        rpm = obd.query("rpm")
        lcd.write_left("RPM -> {0}".format(str(rpm.magnitude)))
        p = int((rpm.magnitude / maxrpm) * 100)
        lcd.print_loading_bar(p,char='#')
        print(p)
        sleep(0.5)

def start_gps():
    gps = ""

x = Thread(target=start_obd,args=())
y = Thread(target=start_lcd)
x.start()
y.start()

# while True:

#     rpm = obd.query("rpm")
#     lcd.write_left(str(rpm))
#     print(str(rpm))
#     sleep(0.5)



