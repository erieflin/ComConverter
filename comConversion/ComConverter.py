import serial
from config import *
# inValue = b'<<357'
startInLineByte = bytes([2])
endInLineByte = bytes([3])
inCommPort = ports[0]['comPort']
outComPort = ports[1]['comPort']
inSer = serial.Serial(inCommPort)
outSer = serial.Serial(outComPort)

line = ''


def getOuputFromInput(checkValue):
    for valuePair in intercomList:
        if valuePair['inVal'] == checkValue:
            return valuePair['outVal']


print("waiting For Input")
while True:
    try:
        inValue = inSer.read()
        if inValue == startInLineByte:
            line = ''
        elif inValue == endInLineByte:
            outValue = getOuputFromInput(line)
            line1 = 'ATZ\r\n'
            line2 = 'ATX0\r\n'
            line3 = outValue + '\r\n'
            print('outputting values:')
            print(line1)
            print(line2)
            print(line3)
            outSer.write(line1.encode())
            outSer.write(line2.encode())
            outSer.write(line3.encode())
            line = ''
        else:
            line = line + (inValue.decode())
    except KeyboardInterrupt:
        print("exiting....")
        raise

inSer.close()




# old b'<<357'
# new ATDT *51
# B"OLD" ->

# b'ATZ\r\n'
# b'ATX0\r\n'
# b'NEW\r\n'
