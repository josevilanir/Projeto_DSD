# client.py
from Pyro4 import Proxy

with open("lamp_uri.txt", "r") as file:
    uri = file.read()

lamp = Proxy(uri)

# Agora você pode usar lamp para ligar e desligar a lâmpada remotamente
lamp.ligar()
lamp.desligar()
lamp.desligar()
