# the-little-base-station
A django application which monitors temperature, pressure and fairy dust.  

First thing to do is login as user, after that the user data, live data and cyclic data are shown.  
The server can run in Django debug mode and without external hardware (mocking enabled).  

<img src="https://github.com/Thaulino/the-little-base-station/blob/main/media/walkthrough.gif" alt="Walkthrough_Video" width="300">

## quickstart

prequisition:  
* python  
* pip 
* terminal
* git  

step by step  
1. clone repository to ${SOME_DIRECTORY}  
2. create and open virtual python environment
3. navigate to ${SOME_DIRECTORY}\littlebasestation
4. install packages via pip from requirements.txt  
```
 >> pip install -r requirements.txt 
```
5. create minimal database
```
python manage.py migrate
```
6. create a super user
```
python manage.py createsuperuser 
```  
7. start server
```
python manage.py runserver
``` 

Open http://127.0.0.1:8000/ in your browser to see the server running.

**Warning: This is a devlopment server, please use a server like apache or nginx in production, 
[a tutorial about deployment of django applications](https://uwsgi.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)**

## some details

The hardware mocking can be enabled/ disabled by setting the MOCK_HARDWARE variable to true/false (refer littlebasestation/settings.py)  
  
The little-base-station ships with a custom command to trigger a measurement of pressure,temperature and fairy dust:

```
    >> python manage.py triggermeasure
```
It is used as a cron job to trigger a periodic measurement, for example every 8 hours.  
  
Python related [dependencies](littlebasestation\\requirements.txt)  

## hardware setup and testing 

A setup consisting of a [raspberry pi 3B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/) and a [bmp280 sensor module](https://www.az-delivery.de/en/products/azdelivery-bmp280-barometrischer-sensor-luftdruck-modul-fur-arduino-und-raspberry-pi) is running in production.

<img src="https://github.com/Thaulino/the-little-base-station/blob/main/media/circuit.JPG" alt="Hardware_Schematic" width="250">

