# T2-Distribuido
Kafka y rabbit MQ

# Kafka

Se accede a la carpeta brokers y se ejecuta el docker-compose up -d

Si se quiere dockerizar, se debe hacer lo mismo con los docker-compose en prodoctores y consumidores. Una vez dentro ejecutar:

 - sudo docker inspect network brokers_default

y seleccionar copiar la ip de kafka-1, para posteriormente usarla en consumidores y productores, en la variable bootstrapServer.

Si se trabaja en Linux, no es necesario dockerizar productores y consumidores, basta con montar el compose con kafka y zookeeper, se 
repite el paso anterior para seleccionar las boostrapServer.



