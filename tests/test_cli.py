import unittest
import subprocess


class TestEntryPoint(unittest.TestCase):
    def test__main__without_argument(self):
        output = subprocess.run(
            ['python', 'log_analyzer'],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(output.returncode, 1)
        self.assertIn('AttributeError', output.stderr)

    def test__main__with_argument(self):
        output = subprocess.run(
            ['python', 'log_analyzer', './tests/fixtures/test_log.txt'],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(output.returncode, 0)
        self.assertEqual(23, len(output.stdout.split('\n')))
