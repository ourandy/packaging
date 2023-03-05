# from unittest import TestCase
# from capsphere.common.utils import to_snake_case, dataclass_to_dict
# from capsphere.domain.data import Cf
# from decimal import Decimal
#
#
# class TestUtils(TestCase):
#     camelCase = 'camelCase'
#     PascalCase = 'PascalCase'
#     allLowerCase = 'alllowercase'
#     allCaps = 'ALLCAPS'
#     number = '1'
#     mixedNumber = '1something'
#     cashflow = Cf('Mar 22',
#                   Decimal('1'),
#                   Decimal('2'),
#                   Decimal('3'),
#                   Decimal('4'),
#                   Decimal('5'),
#                   Decimal('6'))
#
#     def test_to_dict(self):
#         self.assertEqual(to_snake_case(self.camelCase), 'camel_case')
#         self.assertEqual(to_snake_case(self.PascalCase), 'pascal_case')
#         self.assertEqual(to_snake_case(self.mixedNumber), '1something')
#         self.assertEqual(to_snake_case(self.allLowerCase), 'alllowercase')
#         self.assertEqual(to_snake_case(self.allCaps), 'ALLCAPS')
#         self.assertEqual(to_snake_case(self.number), '1')
#
#     def test_dataclass_to_dict(self):
#         data_dict = dataclass_to_dict(self.cashflow)
#         self.assertTrue('month' in data_dict)
#         self.assertTrue('start_balance' in data_dict)
#         self.assertTrue('end_balance' in data_dict)
#         self.assertTrue('total_debit' in data_dict)
#         self.assertTrue('total_credit' in data_dict)
#         self.assertTrue('average_debit' in data_dict)
#         self.assertTrue('average_credit' in data_dict)
#         self.assertEqual(data_dict.get('month'), 'Mar 22')
#         self.assertEqual(data_dict.get('start_balance'), Decimal('1'))
#         self.assertEqual(data_dict.get('end_balance'), Decimal('2'))
#         self.assertEqual(data_dict.get('total_debit'), Decimal('3'))
#         self.assertEqual(data_dict.get('total_credit'), Decimal('4'))
#         self.assertEqual(data_dict.get('average_debit'), Decimal('5'))
#         self.assertEqual(data_dict.get('average_credit'), Decimal('6'))
#
