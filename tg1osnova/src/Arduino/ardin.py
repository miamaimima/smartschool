import serial
import time


def temperature():

    ser = serial.Serial('COM5', 9600)


    try:
        data = ser.readline().decode().strip()
        print(data)
        returneddata = data.split(" ")
        return returneddata
    except KeyboardInterrupt:
        ser.close()






