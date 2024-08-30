import serial

port = "COM3"

baudrate = 9600

ser = serial.Serial(port=port, baudrate=baudrate, timeout=1,)
print("Connected to the port: ", ser.name)

# while True:
#     x = ser.read()  # returns 1 byte at a time
#     print(x)

ser.close()
