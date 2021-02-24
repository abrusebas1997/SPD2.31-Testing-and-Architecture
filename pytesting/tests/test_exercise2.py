import unittest
import pytest
import math
from ..exercise2 import get_age_carbon_14_dating

class test_get_age_carbon_14_dating(unittest.TestCase):

    def test_numbers(self):
        assert math.isclose(get_age_carbon_14_dating(0.35), 8680.34, abs_tol=0.01)
        assert get_age_carbon_14_dating(0) == 0
        assert get_age_carbon_14_dating(-10) == 0

    def test_error(self):
        with self.assertRaises(ValueError):
            get_age_carbon_14_dating(10)
        with self.assertRaises(TypeError):
            get_age_carbon_14_dating('boop')

    def test_error_pytest_syntax(self):
        with pytest.raises(ValueError):
            assert get_age_carbon_14_dating(10)
        with pytest.raises(TypeError):
            assert get_age_carbon_14_dating('boop')
