from unittest import TestCase
from capsphere.domain.data import Cf, MonthlyCf
from decimal import Decimal


class TestExceptions(TestCase):

    def test_cf_validation(self):
        with self.assertRaises(TypeError) as cm:
            Cf('Mar 22',
               2502.23,
               Decimal('25'),
               Decimal('25'),
               Decimal('25'),
               Decimal('25'),
               Decimal('25'))
        self.assertEqual("Field 'start_balance' must be of type 'Decimal'.",
                         str(cm.exception))

    def test_monthly_cf_validation(self):
        with self.assertRaises(TypeError) as cm:
            MonthlyCf('Andy', 'Rhb', 'invalid cf')
        self.assertEqual("Field 'cash_flow' must be a list of type 'Cf'.",
                         str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            MonthlyCf('Andy', 'Rhb', [])
        self.assertEqual("Field 'cash_flow' must have one or more items.",
                         str(cm.exception))
