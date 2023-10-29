# lamp.py
from device_interface import Device
from Pyro4 import expose

class Lamp(Device):
    def __init__(self):
        self.is_on = False  # Inicialmente, a lâmpada está desligada

    @expose  # Decorar o método ligar
    def ligar(self):
        if not self.is_on:
            print("A lâmpada está ligada.")
            
            self.is_on = True
        else:
            print("A lâmpada já está ligada.")

    @expose  # Decorar o método desligar
    def desligar(self):
        if self.is_on:
            print("A lâmpada está desligada.")
            
            self.is_on = False
        else:
            print("A lâmpada já está desligada.")

