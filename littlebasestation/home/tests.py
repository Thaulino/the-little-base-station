from django.test import TestCase
from django.conf import settings
from io import StringIO
from django.core.management import call_command
from .hwaccess import Barometer
from .views import home_periodic_ajax_view

from .management.commands import triggermeasure

# Create your tests here.
# To run tests : python manage.py test home.tests

class BaroMeterTestCase(TestCase):

    def setUp(self) -> None:
        super().setUpClass()

    def tearDown(self) -> None:
        super().tearDownClass()

    # NOTE run with
    def testBarometer(self):

        self.assertEqual(Barometer.alive(), True, "The barometer is not alive")
        try:
            p = Barometer.pressure()
            t = Barometer.temperature()
        except:
            self.assertEqual(True, False, "The barometer throws an error while reading pressure and temperature")

    def testBarometerError(self):
        Barometer.raise_error_on_next_hw_access()
        ep = Barometer.pressure()
        p = Barometer.pressure()

        Barometer.raise_error_on_next_hw_access()
        et = Barometer.temperature()
        t = Barometer.temperature()

        self.assertEqual(ep, -1.0, "error behavior of barometer was not as expected")
        self.assertNotEqual(p, -1.0, "error behavior of barometer was not as expected")

        self.assertEqual(et, -1.0, "error behavior of barometer was not as expected")
        self.assertNotEqual(t, -1.0, "error behavior of barometer was not as expected")

# python manage.py test home.tests.CommandTestCase.test_command_with_faulty_barometer
class CommandTestCase(TestCase):
    def setUp(self) -> None:
        super().setUpClass()

    def tearDown(self) -> None:
        super().tearDownClass()

    def testCommand(self):
        out = StringIO()
        call_command('triggermeasure', stdout=out)

        if out.readable():
            self.assertTrue("Successfully" in out.getvalue())
        else:
            self.assertTrue(False, "command does not output a string")

    def test_command_with_faulty_barometer(self):
        out = StringIO()
        Barometer.raise_error_on_next_hw_access()
        call_command('triggermeasure', stdout=out)

        if out.readable():
            self.assertTrue("Successfully" in out.getvalue())
        else:
            self.assertTrue(False, "command does not output a string")


# More tests, related to db