# the-little-base-station
A django application which monitors temperature, pressure and fairy dust.  

First thing to do is login in as user, after that the 
user data, live data and cyclic data are shown.  
The server can run in Django debug mode and without external hardware (mocking).  


![Walkthrough_Video](https://github.com/Thaulino/the-little-base-station/media/the-little-base-station.webm)


## some details

The hardware mocking can be enabled/ disabled by setting the MOCK_HARDWARE variable to true/false (refer littlebasestation/settings.py)  
  
The little-base-station ships with a custom command to trigger a measurement of pressure,temperature and fairy dust:

```
    >> python manage.py triggermeasure
```
It is used as a cron job to trigger a periodic measurement, for example every 8 hours.



## hardware setup and testing 

I deployed and tested a setup consisting of a [raspberry pi 3B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/) and a [bmp280 sensor module](https://www.az-delivery.de/en/products/azdelivery-bmp280-barometrischer-sensor-luftdruck-modul-fur-arduino-und-raspberry-pi)


