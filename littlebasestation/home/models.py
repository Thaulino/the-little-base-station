import os

from django.db import models

# Create your models here.


class Datapoint(models.Model):
    """ Only model for a little base station
        general_json scheme

        {
            "version " : 0,
            "data":
            [
                {
                    "name" : "temperature",
                    "value": 234.432,
                    "unit": "°C"
                },
                ...
                {
                    "name" : "pressure",
                    "value": 23423,
                    "unit": "hP"

                }
            ]

            refer:
                NAME_JSON_TEMPERATURE
                NAME_JSON_PRESSURE
        }
    """
    creation_timestamp = models.DateTimeField(auto_now_add=True)

    NAME_JSON_TEMPERATURE = "temperature"
    NAME_JSON_PRESSURE = "pressure"

    data_json = models.JSONField()

    def __str__(self):
        return f"{os.linesep}creation time{os.linesep}{self.creation_timestamp}{os.linesep}" \
               f"data_json{os.linesep}{self.data_json}{os.linesep}"


