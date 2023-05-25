import pika
import threading
import time
import datetime
import random
import json

#variables
actual_time = time.time()
n_productores = 50
stop = False

## Alternar
data = open("small_array.txt", "r").read()
# data = open("big_array.txt", "r").read()
data = data.replace("[", "").replace("]", "").replace("'", "").split(", ")


# ejemplo
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# channel.queue_declare(queue='test1')


#Conexiones
conexiones = []
canales = []
lock_canales = []


for i in range(5):
    conexiones.append(pika.BlockingConnection(pika.ConnectionParameters('localhost')))
    canales.append(conexiones[i].channel())
    canales[i].queue_declare(queue="queue")
    # canales[i].queue_declare(queue="queue "+str(i))
    lock_canales.append(threading.Lock())


def productor():
    # deltaT = random.randint(1,2)
    deltaT = 1
    eleccion_canal = random.randint(0,4)
    # while stop != True:
    for i in range(500):
        time.sleep(deltaT)
        inicio = time.time()
        lock_canales[eleccion_canal].acquire()
        datas = data[random.randint(0,99)]
        canales[eleccion_canal].basic_publish(exchange='',
                            routing_key="queue",
                            body=json.dumps({"value": datas, "timestamp": inicio}).encode('utf-8'))
        fin = time.time()
        tiempo = fin - inicio
        lock.acquire()
        try:
            with open("tiempos_produccion.txt", "a") as f:
                f.write(str(tiempo) + "\n")
        finally:
            lock.release()
            lock_canales[eleccion_canal].release()

        print("Sent from " + threading.current_thread().name + " "+ json.dumps({"value": datas, "timestamp": inicio}))    
    print("Productor teriminado")
    # conexiones[eleccion_canal].close()

    


lock = threading.Lock()

for i in range(n_productores):
    t = threading.Thread(target=productor)
    t.start()


while True:
    input("presione enter para detener el envio")
    for i in range(5):
        conexiones[i].close()
    # stop = True
    break
