import random
import threading
import time
from kafka import KafkaConsumer
from json import loads

hilos = []
bootstrapServer =  '172.19.0.3:9093'
topicos = ['topic0','topic1','topic2','topic3','topic4']
particiones_topico = [1,3,3,4,5]

def consumir(topico,bootstrapServer): 
    consumer = KafkaConsumer(
    topico,
    bootstrap_servers=[bootstrapServer],
    group_id='nuevo',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

    consumer.subscribe(topics=['topic2'])

    for event in consumer:
        inicio = time.time()
        event_data = event.value
        final = time.time()
        tiempo = final - inicio
        print(event_data)
        lock.acquire()

        try:
            with open('tiempos_consumidor.txt', 'a') as file:
                file.write('\n' + f"{tiempo}")
        finally:
            lock.release()
    consumer.close()
    return

def mConsumidores(topico): #Pregunta 5
    consumer = KafkaConsumer(
    topico,
    bootstrap_servers=['172.19.0.3:9093'],
    value_deserializer=lambda x: loads(x.decode('utf-8')))


    for event in consumer:
        inicio = time.time()
        event_data = event.value
        final = time.time()
        tiempo = final - inicio
        print('Estoy en el canal : ' + topico + ' Mensaje : ' + str(event_data) + ' particion : ' str(event.partition))
        lock.acquire()
        try:
            with open('tiempos_consumidor_pregunta5.txt', 'a') as file:
                file.write('\n' + f"{tiempo}")
        finally:
            lock.release()
    consumer.close()
    return



lock = threading.Lock()




########################################################### Pregunta 5 #############################################################
# n = 5


# for i in range(n):
#     consumidores_canal = random.randint(1,2) 
#     for j in range(consumidores_canal):
#         hilo = threading.Thread(target = mConsumidores, args=(topicos[i],))
#         hilo.start()
#         hilos.append(hilo)

# for hilo in hilos:
#     hilo.join()

##################################################### Escalabilidad particiones #################################################

# n = 3 

# for i in range(n):
#     hilo = threading.Thread(target = mConsumidores, args=(topicos[i],))
#     hilo.start()
#     hilos.append(hilo)

# for hilo in hilos:
#     hilo.join()


####################################################################################################################################

