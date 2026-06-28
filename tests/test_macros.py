import io
import unittest

from macros import MacroDB


class FakeFileLoader:
    def __init__(self):
        self._extensions = ['missing_ext']

    def get_extensions(self):
        return self._extensions

    def open_file(self, path):
        if path in {
            '/extensions/missing_ext/index/macros.xml',
            '/extensions/missing_ext/index/components.xml',
        }:
            raise ValueError("Path {} isn't a file".format(path))

        if path in {'index/macros.xml', 'index/components.xml'}:
            return io.BytesIO(b'<index/>')

        raise AssertionError('Unexpected path requested: {}'.format(path))


class MacroDBTests(unittest.TestCase):
    def test_missing_extension_indexes_are_skipped(self):
        macro_db = MacroDB(FakeFileLoader())

        self.assertEqual(macro_db.macro_index, {})
        self.assertEqual(
            macro_db.component_index['cockpit_invisible_escapepod'],
            'assets/units/size_s/cockpit_invisible_escapepod.xml'
        )


if __name__ == '__main__':
    unittest.main()
