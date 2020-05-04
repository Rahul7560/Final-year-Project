import serial

arduinodata=serial.Serial('/dev/ttyACM0',9600)

def green2on():
    arduinodata.write(b'211')
def green2off():
    arduinodata.write(b'210')
def yellow2on():
    arduinodata.write(b'221')
def yellow2off():
    arduinodata.write(b'220')
def red2on():
    arduinodata.write(b'2')
def red2off():
    arduinodata.write(b'230')


