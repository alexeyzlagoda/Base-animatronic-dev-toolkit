import serial

def SearchPorts():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(port.device)
def SW(port,baud,Data):
    #port = "COM1"  # Replace with the appropriate COM port name
    baudrate = baud  # Replace with the desired baud rate
    ser = serial.Serial(port, baudrate=baudrate)
    # Perform operations on the COM port
    # Writing data
    message = Data  # Data to be sent, should be in bytes
    ser.write(message.encode())
    ser.close()  # Remember to close the connection when done
def MoveServ(port,baud,ID,val):
    Command = "moveserv " + ID + " " + val
    SW(port,baud,Command)
