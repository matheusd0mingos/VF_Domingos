from usina import Usina
import numpy as np
from matplotlib import pyplot as plt

class Leitor():
    def __init__(self, usina):
        self.usina=usina

    def level_time(self):
        level=np.array([])
        nivel=self.usina.get_sensor()
        if self.usina.get_actuator():
            while self.get_actuator():
                level=np.append(level, nivel)
                nivel=self.usina.get_sensor()
                if nivel<=0:
                    break
            x=np.arange(0,len(level))*0.1
        else:
            level=np.append(level, nivel)
            x=0
        return x, level

class Controlador():
    def __init__(self, usina):
        self.usina=usina

    def abrir(self):
        self.usina.set_actuator(True)
        print('Comporta aberta com sucesso')
    def fechar(self):
        self.usina.set_actuator(True)
        print('Comporta fechada com sucesso')

    def check(self):
        if self.usina.get_sensor()>=245*70/90+10:
            self.abrir()
        elif self.usina.get_sensor()<=0:
            self.fechar()


usina1=Usina()
control1=Controlador(usina1)
leitor1=Leitor(usina1)
control1.check()
x, level=leitor1.level_time()
plt.plot(x,level)
plt.show()

