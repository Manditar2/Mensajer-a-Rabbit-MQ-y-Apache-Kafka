import random
import threading
from kafka import KafkaConsumer
from json import loads
from time import sleep

consumer = KafkaConsumer(
    'topic_test',
    bootstrap_servers='172.20.0.3:9093',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='nuego_grupo',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

for event in consumer:
    event_data = event.value
    print(event_data)
    sleep(2)