import serial
from config import *
targetValue = 8
s = serial.Serial('COM1')
responseSer= serial.Serial('COM4')

for valuePair in intercomList:
    outValue = valuePair['inVal'].encode()
    outValue = bytes([2])+outValue+bytes([3])
    print("sending value" + outValue.decode())
    s.write(outValue)
    s.flushOutput()
    responseVal = responseSer.readline()
    responseVal += responseSer.readline()
    responseVal += responseSer.readline()
    print("response " + responseVal.decode() + "\r\n")
s.close()