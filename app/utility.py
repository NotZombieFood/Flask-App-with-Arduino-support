import serial, time


def checkVal(port="COM3", baud_rate = 9600):
    arduino = serial.Serial(port,baud_rate,timeout = 2)
    rawString = arduino.readline()
    value = rawString.decode("utf-8").replace("\r","").replace("\n","")
    arduino.close()
    return value

