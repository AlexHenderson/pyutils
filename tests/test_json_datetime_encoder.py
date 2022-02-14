import datetime
import json
from unittest import TestCase

from src.pyutils.datetime_utils.json_datetime_encoder import JsonDatetimeEncoder


class TestJsonDatetimeEncoder(TestCase):

    def test_default1(self):
        """ Test date """
        date = datetime.date(2000, 12, 25)

        encoder = JsonDatetimeEncoder
        jsonoutput = json.dumps(date, indent=4, cls=encoder)

        self.assertEqual(jsonoutput, '"2000-12-25"')

    def test_default2(self):
        """ Test time, with and without seconds """
        time = datetime.time(13, 23)

        encoder = JsonDatetimeEncoder
        jsonoutput = json.dumps(time, indent=4, cls=encoder)

        self.assertEqual(jsonoutput, '"13:23:00"')

        time = datetime.time(13, 23, 33)

        encoder = JsonDatetimeEncoder
        jsonoutput = json.dumps(time, indent=4, cls=encoder)

        self.assertEqual(jsonoutput, '"13:23:33"')

    def test_default3(self):
        """ Test date/time """
        christmas_time = datetime.datetime(2000, 12, 25, 13, 23)

        encoder = JsonDatetimeEncoder
        jsonoutput = json.dumps(christmas_time, indent=4, cls=encoder)

        self.assertEqual(jsonoutput, '"2000-12-25T13:23:00"')
