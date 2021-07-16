from usina import Usina
import numpy as np
from matplotlib import pyplot as plt

class Leitor():
    def __init__(self, usina, control):
        self.usina=usina
        self.control=control

    def level_time(self):
        level=np.array([])
        nivel=self.usina.get_sensor()
        aux=self.usina.get_actuator()
        i=0
        while aux:
                level=np.append(level, nivel)
                nivel=self.usina.get_sensor()
                aux=self.usina.get_actuator()  
                self.control.check()         
        x=np.arange(0, len(level))*0.1

        
        return x, level

class Controlador():
    def __init__(self, usina):
        self.usina=usina

    def abrir(self):
        self.usina.set_actuator(True)
        #print('Comporta aberta com sucesso')
    def fechar(self):
        self.usina.set_actuator(False)
        #print('Comporta fechada com sucesso')

    def check(self):
        if self.usina.get_sensor()>=245*70/90+10:
            self.abrir()
        else:
            self.fechar()


usina1=Usina()
control1=Controlador(usina1)
leitor1=Leitor(usina1, control1)
control1.check()
x, level=leitor1.level_time()
plt.plot(x,level)
plt.show()

