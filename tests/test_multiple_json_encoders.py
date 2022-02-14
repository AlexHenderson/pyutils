import json
from unittest import TestCase

import datetime
from pint import Quantity, Unit, UnitRegistry

from src.pyutils.json_utils.multiple_json_encoders import MultipleJsonEncoders
from src.pyutils.pint_utils.json_pint_encoder import JsonPintEncoder
from src.pyutils.datetime_utils.json_datetime_encoder import JsonDatetimeEncoder


class TestMultipleJsonEncoders(TestCase):

    def test_default1(self):

        ureg = UnitRegistry()
        duration = Quantity(5.6, ureg.sec)

        encoder = MultipleJsonEncoders(JsonPintEncoder, JsonDatetimeEncoder)
        output = json.dumps(duration, indent=4, cls=encoder)

        self.assertEqual(output, '"5.6 second"')

    def test_default2(self):

        time = datetime.time(13, 23)

        encoder = MultipleJsonEncoders(JsonPintEncoder, JsonDatetimeEncoder)

        output = json.dumps(time, indent=4, cls=encoder)

        self.assertEqual(output, '"13:23:00"')

    def test_default3(self):

        christmas_time = datetime.datetime(2000, 12, 25, 13, 23)
        ureg = UnitRegistry()
        duration = Quantity(5.6, ureg.sec)

        encoder = MultipleJsonEncoders(JsonPintEncoder, JsonDatetimeEncoder)

        christmas_time_output = json.dumps(christmas_time, indent=4, cls=encoder)
        self.assertEqual(christmas_time_output, '"2000-12-25T13:23:00"')

        durationoutput = json.dumps(duration, indent=4, cls=encoder)
        self.assertEqual(durationoutput, '"5.6 second"')
