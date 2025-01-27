from typing import Any
from unittest.mock import patch, mock_open
import unittest

from log_analyzer.parser import LogParser


class TestLogParser(unittest.TestCase):
    test_log_content: str
    mock_open: Any

    def setUp(self):
        self.test_log_content = (
            '2025-01-26 14:04 INFO Application started\n'
            '2025-01-26 14:04 DEBUG Initializing database connection\n'
            '2025-01-26 14:05 INFO User login: john_doe\n'
            '2025-01-26 14:05 DEBUG Query executed: SELECT * FROM users\n'
            '2025-01-26 14:06 WARNING Slow query detected\n'
            '2025-01-26 14:07 INFO New user registered: jane_smith\n'
            '2025-01-26 14:08 ERROR Error in query execution\n'
            '2025-01-26 14:09 INFO Processing daily report\n'
            '2025-01-26 14:10 DEBUG Cache cleared\n'
        )
        self.mock_open = mock_open(read_data=self.test_log_content)

    @patch('pathlib.Path.open')
    def test__message_generator(self, mock_path_open):
        mock_path_open.return_value = self.mock_open.return_value

        with LogParser('test.log') as parser:
            messages = list(parser.message_generator())

        self.assertEqual(len(messages), 9)
        self.assertEqual(messages[0].level.name, 'INFO')
        self.assertEqual(messages[1].level.name, 'DEBUG')

    @patch('pathlib.Path.open')
    def test__level_generator(self, mock_path_open):
        mock_path_open.return_value = self.mock_open.return_value

        with LogParser('test.log') as parser:
            messages = list(parser.message_generator())
            levels = set(parser.level_generator())

        self.assertEqual(len(levels), 4)

    def test__context_manager(self):
        with patch('pathlib.Path.open', self.mock_open):
            with LogParser('test.log') as parser:
                self.assertIsNotNone(parser.log_file)
            self.assertTrue(parser.log_file.closed)
