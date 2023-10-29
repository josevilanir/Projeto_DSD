# server.py
from Pyro4 import Daemon
from device_interface import Device
from lamp import Lamp

daemon = Daemon()

lamp = Lamp()

uri = daemon.register(lamp)
print("URI do objeto Lamp:", uri)

with open("lamp_uri.txt", "w") as file:
    file.write(str(uri))

daemon.requestLoop()
