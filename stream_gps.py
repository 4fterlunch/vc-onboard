import serial

# adapted from http://ozzmaker.com/using-python-with-a-gps-receiver-on-a-raspberry-pi/

port = "/dev/ttyS0"
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)

def parseSerial(data):
    if data[0:6] == "$GPRMC":
        sdata = data.split(",")
        if sdata[2] == 'V':
            print "no satellite data available"
            return
        reading = {
            "time": sdata[1][0:2] + ":" + sdata[1][2:4] + ":" + sdata[1][4:6],
            "date": sdata[9][0:2] + "/" + sdata[9][2:4] + "/" + sdata[9][4:6],#date
            "lat": sdata[3], #latitude
            "lon": sdata[5], #longitute
            "dirLat": sdata[4]   ,   #latitude direction N/S
            "dirLon": sdata[6]    ,  #longitude direction E/W
            "knots": sdata[7]    ,   #Speed in knots
            "trCourse": sdata[8]   #True course
  
        }
        return reading

        

        #print "time : %s, latitude : %s(%s), longitude : %s(%s), speed : %s, True Course : %s, Date : %s" %  (time,lat,dirLat,lon,dirLon,speed,trCourse,date)

def decode(coord):
    #Converts DDDMM.MMMMM > DD deg MM.MMMMM min
    x = coord.split(".")
    head = x[0]
    tail = x[1]
    deg = head[0:-2]
    min = head[-2:]
    return deg + min + "." + tail


while True:
    data = ser.readline()
    if parseSerial(data) is not None:
        print(parseSerial(data))

