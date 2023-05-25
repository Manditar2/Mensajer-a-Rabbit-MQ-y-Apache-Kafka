# T2-Distribuido
Kafka y rabbit MQ
# Link Video
https://drive.google.com/file/d/1aZfZGYBgET35-Kf8QDdI_y95lhuZF2BH/view?usp=sharing
# Kafka

Se accede a la carpeta brokers y se ejecuta el docker-compose up -d

Si se quiere dockerizar, se debe hacer lo mismo con los docker-compose en prodoctores y consumidores. Una vez dentro ejecutar:

 - sudo docker inspect network brokers_default

y seleccionar la ip de kafka-1, para posteriormente usarla en consumidores y productores, en la variable bootstrapServer.

Si se trabaja en Linux, no es necesario dockerizar productores y consumidores, basta con montar el compose con kafka y zookeeper, se 
repite el paso anterior para seleccionar el boostrapServer corresponde.

Para lo anterior, es necesario primero utilizar los compose ubicados en las carpetas consumidores y productores, y luego se utiliza el compose de la carpeta brokers

RabittMQ solo necesita montar el servicio con el compose



