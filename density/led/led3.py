import serial

arduinodata=serial.Serial('/dev/ttyACM0',9600)

def green3on():
    arduinodata.write(b'311')
def green3off():
    arduinodata.write(b'310')
def yellow3on():
    arduinodata.write(b'321')
def yellow3off():
    arduinodata.write(b'320')
def red3on():
    arduinodata.write(b'331')
def red3off():
    arduinodata.write(b'330')


