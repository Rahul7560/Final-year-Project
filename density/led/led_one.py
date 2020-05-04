import serial
import time

arduinodata=serial.Serial('/dev/ttyACM0',9600)
time.sleep(2)


def green1on():
    arduinodata.write(b'A')
def green1off():
    arduinodata.write(b'B')
def yellow1on():
    arduinodata.write(b'C')
def yellow1off():
    arduinodata.write(b'D')
def red1on():
    arduinodata.write(b'E')
def red1off():
    arduinodata.write(b'F')


def green2on():
    arduinodata.write(b'G')
def green2off():
    arduinodata.write(b'H')
def yellow2on():
    arduinodata.write(b'I')
def yellow2off():
    arduinodata.write(b'J')
def red2on():
    arduinodata.write(b'K')
def red2off():
    arduinodata.write(b'L')


def green3on():
    arduinodata.write(b'M')
def green3off():
    arduinodata.write(b'N')
def yellow3on():
    arduinodata.write(b'O')
def yellow3off():
    arduinodata.write(b'P')
def red3on():
    arduinodata.write(b'Q')
def red3off():
    arduinodata.write(b'R')


def green4on():
    arduinodata.write(b'S')
def green4off():
    arduinodata.write(b'T')
def yellow4on():
    arduinodata.write(b'U')
def yellow4off():
    arduinodata.write(b'V')
def red4on():
    arduinodata.write(b'W')
def red4off():
    arduinodata.write(b'X')
