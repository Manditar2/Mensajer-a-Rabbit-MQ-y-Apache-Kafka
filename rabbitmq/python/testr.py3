#!/usr/bin/env python
import pika, sys, os, threading, time, datetime

def consumidor():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    def callback(ch, method, properties, body):
        print(threading.current_thread().name +" Received %r" % body)
        # time.sleep(3)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def main():
    while True:
        t = threading.Thread(target=consumidor)
        input("presione enter para iniciar el consumidor")
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
