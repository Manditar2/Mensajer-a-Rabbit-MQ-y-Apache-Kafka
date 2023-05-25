#!/usr/bin/env python
import pika, sys, os, threading, time, datetime, random

m_consumidores = 10
actual_time = time.time()

#Conexiones
conexiones = []
canales = []
lock_canales = []

for i in range(5):
    conexiones.append(pika.BlockingConnection(pika.ConnectionParameters('localhost')))
    canales.append(conexiones[i].channel())
    canales[i].queue_declare(queue="queue "+str(i))
    canales[i].queue_declare(queue="hello")
    lock_canales.append(threading.Lock())

def consumidor():
    eleccion_canal = random.randint(0,4)

    while True:
        lock_canales[eleccion_canal].acquire()
        tiempo_inicio = time.time()
        for method_frame, properties, body in canales[eleccion_canal].consume(queue="queue", auto_ack=True):
            tiempo_fin = time.time()
            # print(threading.current_thread().name + " Received")
            print(threading.current_thread().name +" Received %r" % body)
            lock_canales[eleccion_canal].release()
            lock.acquire()
            try:
                with open("tiempos_consumo.txt", "a") as f:
                    f.write(str(tiempo_fin - tiempo_inicio) + "\n")
            finally:
                lock.release()
            
            break

def consumidor_premium():
    conexion_premium = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    canal_premium = conexion_premium.channel()
    canal_premium.queue_declare(queue="queue")
    while True:
        tiempo_inicio = time.time()
        for method_frame, properties, body in canal_premium.consume(queue="queue", auto_ack=True):
            tiempo_fin = time.time()
            print(threading.current_thread().name +" Received %r" % body)
            lock.acquire()
            try:
                with open("tiempos_consum2.txt", "a") as f:
                    f.write(str(tiempo_fin - tiempo_inicio) + "\n")
            finally:
                lock.release()
            break
    
    
    


    


def main():
    for i in range(m_consumidores):
        t = threading.Thread(target=consumidor)
        t.start()
    ## mejora en escalabilidad
    # for i in range(m_consumidores):
    #     t = threading.Thread(target=consumidor_premium)
    #     t.start()


lock = threading.Lock()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
