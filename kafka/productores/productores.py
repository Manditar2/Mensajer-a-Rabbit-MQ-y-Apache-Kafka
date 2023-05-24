from time import sleep
from json import dumps
from kafka import KafkaProducer
import random
import threading
import time

mensajesEnviar = ['Sistemas distribuidos', 'Quiero salir','Solemne2','Aguante','Otro mensaje',
                  'Carrera','Manuel Rodriguez','Hola','Cómo estás','Mira, te explico', 'tienes q']

bootstrapServer =  '172.19.0.3:9093'
topicos = ['topic0','topic1','topic2','topic3','topic4']
particiones_topico = [1,3,3,4,5]

def Produciendo(bootstrapServer,topico):
    delta = random.randint(1,5)
    producer = KafkaProducer(
        bootstrap_servers=[bootstrapServer],
        value_serializer=lambda x: dumps(x).encode('utf-8'),
    )
    for _ in range(10):
        deviceId = threading.current_thread().name
        idMensaje = random.randint(0,len(mensajesEnviar)-1)
        mensaje = mensajesEnviar[idMensaje]
        timestamp = time.time()
        data = { "data": mensaje }
        envioDevice = {'timestamp': timestamp, 'value': data}

        print('deviceID : ' + str(deviceId) + ' enviando : ' + str(envioDevice) + ' topico : ' + topico)

        inicio = time.time()
        producer.send(topico, value=envioDevice)
        final = time.time()
        tiempo = final-inicio

        lock.acquire()

        try:
            
            with open('tiempos_produccion.txt', 'a') as file:
                file.write('\n' + f"{tiempo}")
        finally:
            lock.release()

        time.sleep(delta*0.75)

    producer.close()

def ProduciendoParticiones_mismoTopico(nParticiones,bootstrapServer, topico):
    delta = random.randint(1,5)
    producer = KafkaProducer(
        bootstrap_servers = [bootstrapServer],
        value_serializer=lambda x: dumps(x).encode('utf-8'),
    )
    for _ in range(10):
        deviceId = threading.current_thread().name
        idMensaje = random.randint(0,len(mensajesEnviar)-1)
        mensaje = mensajesEnviar[idMensaje]
        timestamp = time.time()
        data = { "data": mensaje }
        envioDevice = {'timestamp': timestamp, 'value': data}
        particion=random.randint(0,nParticiones-1)

        print('deviceID : ' + str(deviceId) + ' enviando : ' + str(envioDevice) + ' particion' +  str(particion))

        inicio = time.time()
        producer.send(topico, value=envioDevice, partition=particion)
        final = time.time()
        tiempo = final-inicio

        lock.acquire()

        try:
            
            with open('tiempos_produccion_pregunta5.txt', 'a') as file:
                file.write('\n' + f"{tiempo}")
        finally:
            lock.release()

        time.sleep(delta*0.75)


lock = threading.Lock()
hilos = []


############################################ Pregunta 5 #####################################################################
# n = 5

# for i in range(n):
#     productores_canal = random.randint(1,3)
#     for j in range(productores_canal):
#         hilo = threading.Thread(target = Produciendo, args=(bootstrapServer, topicos[i]))
#         hilo.start()
#         hilos.append(hilo)


# for hilo in hilos:
#     hilo.join()

# while(1):
#     print('termino')
#     sleep(60)


############################################ Escalabilidad con particiones ###########################################

# n = 3

# for i in range(n):
#     hilo = threading.Thread(target = ProduciendoParticiones_mismoTopico, args=(particiones_topico[2],bootstrapServer, 'topic2',))
#     hilo.start()
#     hilos.append(hilo)

# for hilo in hilos:
#     hilo.join()

# while(1):
#     print('termino')
#     sleep(120)

###########################################################################################################################
