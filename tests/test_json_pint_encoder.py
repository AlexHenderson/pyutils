import json
from unittest import TestCase

from pint import Quantity, Unit, UnitRegistry

from src.pyutils.pint_utils.json_pint_encoder import JsonPintEncoder


class TestJsonPintEncoder(TestCase):

    def test_default1(self):
        ureg = UnitRegistry()
        duration = Quantity(5.6, ureg.sec)

        encoder = JsonPintEncoder
        jsonoutput = json.dumps(duration, indent=4, cls=encoder)

        self.assertEqual(jsonoutput, '"5.6 second"')

    def test_default2(self):
        ureg = UnitRegistry()
        sec = Unit(ureg.sec)

        encoder = JsonPintEncoder
        jsonoutput = json.dumps(sec, indent=4, cls=encoder)

        self.assertEqual(jsonoutput, '"second"')

    def test_default3(self):
        ureg = UnitRegistry()
        nm = Unit(ureg.nanometer)

        encoder = JsonPintEncoder
        jsonoutput = json.dumps(nm, indent=4, cls=encoder)

        self.assertEqual(jsonoutput, '"nanometer"')

    def test_default4(self):
        ureg = UnitRegistry()
        nm = Unit(ureg.nm)

        encoder = JsonPintEncoder
        jsonoutput = json.dumps(nm, indent=4, cls=encoder)

        self.assertEqual(jsonoutput, '"nanometer"')
