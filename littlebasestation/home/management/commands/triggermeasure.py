from django.core.management.base import BaseCommand, CommandError

from contextlib import suppress

from home.models import Datapoint
from home.hwaccess import Barometer

import time
import random
import json

# TODO trigger this stuff periodic at rbpi
# TODO parameterize via settings of app

class Command(BaseCommand):
    help = 'triggers a measure'
    default_max_data = 24

    def add_arguments(self, parser):
        parser.add_argument(
            '--max-data',
            help="the cyclic buffer size, after which the overwriting starts")

    def handle(self, *args, **options):

        # empty dictionary
        general_json = {"version": "0.1", "data": []}

        temperature = {"name": Datapoint.NAME_JSON_TEMPERATURE, "value": Barometer.temperature(), "unit": "°C"}
        pressure = {"name": Datapoint.NAME_JSON_PRESSURE, "value": Barometer.pressure(), "unit": "hPa"}

        general_json["data"].append(temperature)
        general_json["data"].append(pressure)

        if options['max_data'] is None:
            options['max_data'] = Command.default_max_data

        try:
            int(options['max_data'])
        except Exception as e:
            raise RuntimeError(f"max_delta must be an int or a value which can be converted to int given value: "
                               f"{options['max_data']}, detailed error {str(e)}")

        while len(Datapoint.objects.all()) >= int(options['max_data']):
            to_delete = Datapoint.objects.all().order_by('creation_timestamp')[0]
            self.stdout.write(self.style.NOTICE(f'Deleting: {str(to_delete)}'))
            to_delete.delete()

        # make sure to store the entries
        general_json["data"].sort(key=lambda x: x["name"], reverse=True)
        datapoint = Datapoint(data_json=json.dumps(general_json))
        datapoint.save()

        # TODO write django log
        self.stdout.write(self.style.SUCCESS('Successfully triggered measurement'))



