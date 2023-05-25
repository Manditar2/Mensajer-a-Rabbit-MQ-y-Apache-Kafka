import matplotlib.pyplot as plt

import seaborn as sns
import numpy as np
import math
import threading

sns.set_style('darkgrid')


# respuesta kafka prod, kafka con, rabbit prod, rabbit con, implementacion canal
datatxt =["./reskprod.txt", "./reskcon.txt", "./resrprod.txt","./resrcon.txt","./ru.txt"]
# datatxt =["./ru.txt"]


def calcular_desviacion_standar(nombre_archivo):
    with open(nombre_archivo,"r") as archivo:
        valores = [float(linea.strip()) for linea in archivo.readlines()]
        media = sum(valores)/len(valores)
        suma_cuadrados = sum((valor - media)**2 for valor in valores)
        desviacion_standar = round(math.sqrt(suma_cuadrados/len(valores)),2)
        return desviacion_standar

def calcular_media_txt(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        total = 0
        count = 0
        for line in lines:
            total +=float(line.strip())
            count += 1
        media = total/count
        return media
# print (calcular_media_txt("./probando_cache22.txt"))
# print (calcular_desviacion_standar("./probando_cache22.txt"))

def graficar(archivo):
    with open(archivo, 'r') as f:
        tiempos = [float(line.strip()) for line in f]

    tiempos_api = np.array(tiempos)
    tiempos_grafica = tiempos_api.astype('float')
    cantidad_consultas = np.arange(0, len(tiempos_grafica),1)

    plt.plot(cantidad_consultas, tiempos_api)
    plt.ylabel('Tiempo (s)')
    plt.xlabel('N° de consultas')
    # plt.title('Tiempo Productor RabbitMQ')
    plt.show()

# graficar('probando_cache22.txt')
for i in datatxt:
    graficar(i)
    print(i)
    print("Media: ",calcular_media_txt(i))
    print("Desviacion estandar: ",calcular_desviacion_standar(i))
    print("-----------------------------------------------------------")
