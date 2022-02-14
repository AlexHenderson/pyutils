from unittest import TestCase

from src.pyutils.pint_utils import unit_manager


class TestUnitManager(TestCase):

    def test_unit_manager1(self):
        """ Example for a wavelength of 280 nm """
        ureg = unit_manager.pint.UnitRegistry()
        output = unit_manager.unit_manager('wavelength', ureg.nanometer, 280)

        self.assertEqual(output['name'], "wavelength")
        self.assertEqual(output['unit'], "nm")
        self.assertEqual(output['label'], "wavelength (nm)")
        self.assertEqual(output['value'], 280)
        self.assertEqual(output['quantity'], "280 nm")

    def test_unit_manager2(self):
        """ Example for unitless absorbance """
        output = unit_manager.unit_manager('absorbance')

        self.assertEqual(output['name'], "absorbance")
        self.assertEqual(output['unit'], "")
        self.assertEqual(output['label'], "absorbance")

        self.assertNotIn('value', 'output')
        self.assertNotIn('quantity', 'output')
