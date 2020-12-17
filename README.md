# Practica Unidad 1 Timeouts & Retries

Esta practica consiste en simular un servicio bancario y un generador qr/pdf, en los cuales pueden presentarse fallos como Timeout o Latencia, el objetivo es crear un API que sea capaz de conectarse a estos servicios simulados de tal forma que pueda manejar los problemas, y si se comporta como se espera, se obtendra un Flag por cada problema.

## Prerequisitos

Tener instalados _Docker_ y _docker-compose_, de preferencia ejecutar sobre un sistema operativo _Linux / Mac OS_ para poder ejecutar los archivos _.sh_

## Ejecución

```
docker-compose up -d
```

### Activación de problemas
```
. problemaX.sh
```
donde _X_ es un numero: 1 para activar el timeout en el servicio de banco
                        2 para activar la latencia en el servicio de generador qr

Ejecutar el siguiente comando para desactivar alguno de los problemas
```
. eliminarProblemas.sh
```

## Ejecución del test

El script testeara el API en un ambiente normal y en los dos problemas planteados, si todo esta bien se obtendras los Flag. El script se ejecuta de la siguiente manera:
```
Manera magica y super divertida de testear el api....
```