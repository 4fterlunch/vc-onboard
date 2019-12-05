import random, time, json
import obd

class vobd:
    def __init__(self,port="auto",mode=1,simulator_port=2):
        self._port = port
        self._mode = mode
        self._simulator_port = simulator_port
        self._connection = ""
        self._available_commands = ""
        self.run()

    def query(self,command):
        r = self._connection.query(obd.commands.RPM)
        if not r.is_null():
            return r.value
        else:
            return False

    def run(self):
        if (self._port == "auto"):
            print("Scanning ports")
            ports = obd.scan_serial()

            print("Found: {0}".format(ports))
            if len(ports) <= 0:
                print("trying simulator on /dev/pts/{0}".format(self._simulator_port))
                self._connection = obd.OBD("/dev/pts/{0}".format(self._simulator_port))
                if self._connection == "":
                    print("failed to find a connection")

                for port in ports:
                    self._connection = obd.OBD(port)
                    if self._connection.status == obd.OBDStatus.NOT_CONNECTED:
                        continue
                    else:
                        break
                if self._connection.status == obd.OBDStatus.NOT_CONNECTED:
                    print("no serial detected.")
                    exit()
                self._available_commands = self._connection.supported_commands
                for command in self._available_commands:
                    print(command)
        else:
            self._connection = obd.OBD(self._port)



# while True:
    
#     if mode == 1:
        

#         rpm = connection.query(obd.commands.RPM)
#         env_air_temp = connection.query(obd.commands.AMBIANT_AIR_TEMP)
#         print("{0}, {0}".format(rpm,env_air_temp))