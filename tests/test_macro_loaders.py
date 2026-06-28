import unittest

from loaders.macro_loaders import _coerce_int


class MacroLoaderTests(unittest.TestCase):
    def test_coerce_int_supports_scientific_notation(self):
        self.assertEqual(_coerce_int('2.997925e+08'), 299792500)
        self.assertEqual(_coerce_int('42'), 42)


if __name__ == '__main__':
    unittest.main()
