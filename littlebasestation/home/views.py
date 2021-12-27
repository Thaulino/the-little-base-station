from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Datapoint
from .hwaccess import Barometer




import random
import json

# Create your views here.
def home_plain(*args, **kwargs):
    """ """
    # string of HTMl code
    return HttpResponse("<h1> Hello World </h1>")


requests_served = 0


@login_required(login_url='/accounts/login/')
def home_view(request, *args, **kwargs):
    """ """
    global requests_served

    requests_served += 1
    template = loader.get_template('home/home.html')
    dataset = Datapoint.objects.all()

    pressure = []
    temperature = []
    timestamps = []

    # find index for datum
    if len(dataset) > 0:
        for i, datum in enumerate(dataset):
            for obj in json.loads(datum.data_json)["data"]:
                if obj["name"] == Datapoint.NAME_JSON_TEMPERATURE:
                    temperature.append(obj["value"])
                if obj["name"] == Datapoint.NAME_JSON_PRESSURE:
                    pressure.append(obj["value"])
            if (i % 3) == 0:
                timestamps.append(datum.creation_timestamp.strftime("%m.%d, %H:%M"))
            else:
                timestamps.append("")


    context = {
        "requests_served": requests_served,
        "pressure": pressure,
        "temperature": temperature,
        "timestamps": timestamps,
        "barometer_connected": Barometer.hw_connected

    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/accounts/login/')
def home_periodic_ajax_view(request):
    """  This view returns the current measurement values of
            pressure
            temperature
            fairy dust
     """
    # empty dictionary
    general_json = {"version": "0.1", "data": []}

    #temperature = {"name": "temperature", "value": (random.random() * 100) % 50, "unit": "°C"}
    temperature = {"name": Datapoint.NAME_JSON_TEMPERATURE, "value": Barometer.temperature(), "unit": "°C"}
    
    #pressure = {"name": "pressure", "value": ((random.random() - 0.5) * 100 + 1013.25), "unit": "hPa"}
    pressure = {"name": Datapoint.NAME_JSON_PRESSURE, "value": Barometer.pressure(), "unit": "hPa"}
    
    fairy_dust = {"name": "fairy_dust", "value": random.random(), "unit": "unicorn quarks"}

    general_json["data"].append(temperature)
    general_json["data"].append(pressure)
    general_json["data"].append(fairy_dust)

    return JsonResponse(general_json)


