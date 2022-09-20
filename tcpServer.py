from socket import *
import serial


serverName = "127.0.0.1"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)


def SerialWrite(msg):
    arduino.write(bytes(msg, 'utf-8'))


while True:
    print("[SERVER READY]")

    connectionSocket, clientAddress = serverSocket.accept()
    print("[NEW CONNECTION]", clientAddress)

    while True:
        sentence = connectionSocket.recv(1024)
        sentence = sentence.decode('utf-8')

        if sentence == '.':
            break

        print("[NEW COMAND]", sentence)

        SerialWrite(sentence)

        connectionSocket.send("ok".encode('utf-8'))

    print("[CONNECTION ENDED]", clientAddress)
    connectionSocket.close()
