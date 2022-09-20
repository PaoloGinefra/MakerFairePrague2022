from socket import *

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

fig = plt.figure()
fig.patch.set_facecolor('white')


plt.figtext(0.5, 0.9, "CONTROLS", fontsize=30, color='black').set_ha("center")

names = ["Leg 1: 1", "2", "3", "Leg 2: 1", "2", "3", "Leg 3: 1", "2", "3"]

figs = [plt.axes([0.1, 0.7 - 0.05 * i - 0.05*(i // 3), 0.8, 0.03])
        for i in range(9)]
sliders = [Slider(figs[i], names[i], 0.0, 1.0, 0.5, valstep=0.05, color='#0b9e21')
           for i in range(9)]

preVal = [0 for _ in range(9)]

serverName = '10.0.237.206'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

clientSocket.settimeout(2)


def update(val):
    for i, s in enumerate(sliders):
        if(s.val != preVal[i]):
            sentence = f'{i},{round(s.val, 3)}'
            print('[SENDING]', sentence)
            sentence = sentence.encode('utf-8')
            clientSocket.send(sentence)
            exitStatus = clientSocket.recv(1024).decode('utf-8')
            print("[EXIT STATUS]", exitStatus)
        preVal[i] = s.val


for s in sliders:
    s.on_changed(update)

print("[CLIENT READY]")

plt.show()

clientSocket.send(".".encode("utf-8"))

print("[CONNECTION ENDED]")
clientSocket.close()
