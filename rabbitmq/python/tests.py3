import pika
import threading
import time
import datetime

actual_time = time.time()

deltaT=0
stop = False

def productor():
    if deltaT == 0:
        print("sin tiempo seleccionado")
    else:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        while stop != True:
            time.sleep(deltaT)
            channel.basic_publish(exchange='',
                                routing_key='hello',
                                body=str(threading.current_thread().name) + " " + str(datetime.datetime.now()))
            print(" [x] Sent 'Hello World!'")   
        print("Productor teriminado")
        connection.close()

while True:
    t = threading.Thread(target=productor)
    a=input("seleccionar tiempo de envio: ")
    if a == "q":
        break
    elif a == "s":
        stop = True
        # t.join()
        # stop = False
    else:
        deltaT = float(a)
        t.start()



