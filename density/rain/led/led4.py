import serial

arduinodata=serial.Serial('/dev/ttyACM0',9600)

def green4on():
    arduinodata.write(b'411')
def green4off():
    arduinodata.write(b'410')
def yellow4on():
    arduinodata.write(b'421')
def yellow4off():
    arduinodata.write(b'420')
def red4on():
    arduinodata.write(b'431')
def red4off():
    arduinodata.write(b'430')


