import serial
import time
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
#COM3 - current arduino
#baudrate - similar ng nasa arduino dapat
#timeout - idk.

def write(x):
    arduino.write(bytes(x, 'utf-8')) #convert mo yung utf-8 encoded na "x" into bytes kasi yun ang naiintindihan ng arduino serial
    time.sleep(0.05) #ewan. hahaha!

while True:
    num = input("Enter a number: ") # Taking input from user
    value = write(num) # num = x sa write(x)
    print(value) # printing the value