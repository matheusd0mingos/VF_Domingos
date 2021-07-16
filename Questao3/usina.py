import random

class Usina:
    def __init__(self, nivel=239):
        self._nivel= nivel
        self._actuator = False
    def get_sensor(self):
        if self._actuator == True:
            self._nivel = self._nivel-(random.random()+1);
        return self._nivel
    def set_actuator(self, actuator):
        """actuator é booleano"""
        self._actuator = actuator
    def get_actuator(self):
        return self._actuator
