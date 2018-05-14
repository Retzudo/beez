from django.test import TestCase


class UtilTest(TestCase):
    def test_color_for_year(self):
        from core.utils import color_for_year

        self.assertEqual(color_for_year(2016), 'white')
        self.assertEqual(color_for_year(2017), 'yellow')
        self.assertEqual(color_for_year(2018), 'red')
        self.assertEqual(color_for_year(2019), 'green')
        self.assertEqual(color_for_year(2020), 'blue')