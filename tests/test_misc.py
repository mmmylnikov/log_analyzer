import unittest

from log_analyzer.misc import print_dict_as_json, NotSerializableEncoder


class TestNotSerializableEncoder(unittest.TestCase):
    def test__default(self):
        obj = object()
        self.assertEqual(NotSerializableEncoder().default(obj), str(obj))


class TestPrintDictAsJson(unittest.TestCase):
    class UnserializableObject:
        def __str__(self):
            return 'UnserializableObject'

    def test__print_dict_as_json(self):
        unformatted_data = {'key': self.UnserializableObject()}
        expected_output = '{\n    "key": "UnserializableObject"\n}'
        self.assertEqual(print_dict_as_json(unformatted_data), expected_output)
