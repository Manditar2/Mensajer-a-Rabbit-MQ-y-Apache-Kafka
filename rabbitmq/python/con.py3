#!/usr/bin/env python
import pika, sys, os, threading, time, datetime, random

m_consumidores = 7

#Conexiones
conexiones = []
canales = []
lock_canales = []

for i in range(5):
    conexiones.append(pika.BlockingConnection(pika.ConnectionParameters('localhost')))
    canales.append(conexiones[i].channel())
    # canales[i].queue_declare(queue="queue "+str(i))
    canales[i].queue_declare(queue="hello")
    lock_canales.append(threading.Lock())

def consumidor():
    eleccion_canal = random.randint(0,4)

    while True:
        lock_canales[eleccion_canal].acquire()
        for method_frame, properties, body in canales[eleccion_canal].consume(queue="hello", auto_ack=True):
            # print(threading.current_thread().name + " Received")
            print(threading.current_thread().name +" Received %r" % body)
            lock_canales[eleccion_canal].release()
            break


def main():
    for i in range(m_consumidores):
        t = threading.Thread(target=consumidor)
        t.start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
