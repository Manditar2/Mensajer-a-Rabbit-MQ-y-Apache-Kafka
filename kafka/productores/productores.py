from time import sleep
from json import dumps
from kafka import KafkaProducer
import random
import threading
import time
tiemposEnvio = [4,1,2,5,1,3,1,2,4,7,1,2,1,3,1,2,3,1]
n = 5
mensajesEnviar = ['Sistemas distribuidos', 'Quiero salir','Solemne2','Aguante','Otro mensaje',
                  'Carrera','Manuel Rodriguez','Hola','Cómo estás','Mira, te explico', 'tienes q']

def Produciendo(tiemposEnvio):
    delta = tiemposEnvio[random.randint(0,len(tiemposEnvio) - 1)]
    producer = KafkaProducer(
        bootstrap_servers=['172.20.0.3:9093'],
        value_serializer=lambda x: dumps(x).encode('utf-8'),
    )
    for _ in range(100):
        deviceId = threading.get_ident()
        idMensaje = random.randint(0,len(mensajesEnviar)-1)
        mensaje = mensajesEnviar[idMensaje]
        timestamp = time.time()
        data = { "data": mensaje }
        envioDevice = {'timestamp': timestamp, 'value': data}
        print('deviceID : ' + str(deviceId) + ' enviando : ' + str(envioDevice))
        producer.send('topic_test', value=envioDevice)
        producer.flush()
        time.sleep(delta)

hilos = []
for i in range(n):
    hilo = threading.Thread(target = Produciendo, args=(tiemposEnvio,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()
