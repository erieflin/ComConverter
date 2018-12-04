import serial
s = serial.Serial('COM4')
while 1==1:
    value = s.readline()
    print(value)


