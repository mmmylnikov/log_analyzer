import unittest
from datetime import datetime

from log_analyzer.log import LogLevel, LogLevelMessagesAggregated, LogMessage


class TestLogLevel(unittest.TestCase):
    def test__name(self):
        level = LogLevel('INFO')
        self.assertEqual(level.name, 'INFO')


class TestLogMessage(unittest.TestCase):
    log_message: LogMessage

    def setUp(self):
        self.log_message = LogMessage(
            '2025-01-26 14:04 INFO Application started'
        )

    def test__timestamp(self):
        self.assertEqual(
            self.log_message.timestamp,
            datetime(2025, 1, 26, 14, 4).astimezone(),
        )

    def test__level(self):
        self.assertEqual(self.log_message.level, LogLevel('INFO'))

    def test__message(self):
        self.assertEqual(self.log_message.message, 'Application started')


class TestLogLevelMessagesAggregated(unittest.TestCase):
    log_level_stat_inital: LogLevelMessagesAggregated
    log_level_stat_aggregated: LogLevelMessagesAggregated

    def setUp(self):
        self.log_level_stat_inital = LogLevelMessagesAggregated(
            level=LogLevel('INFO')
        )
        self.log_level_stat_aggregated = LogLevelMessagesAggregated(
            level=LogLevel('DEBUG')
        )
        self.log_level_stat_aggregated['count'] = 123
        self.log_level_stat_aggregated['longest_message'] = 'test'

    def test__inital__name(self):
        self.assertEqual(self.log_level_stat_inital['level'].name, 'INFO')

    def test__aggregated__name(self):
        self.assertEqual(self.log_level_stat_aggregated['level'].name, 'DEBUG')

    def test__inital__count(self):
        self.assertRaises(KeyError, lambda: self.log_level_stat_inital['count'])

    def test__inital__longest_message(self):
        self.assertRaises(
            KeyError, lambda: self.log_level_stat_inital['longest_message']
        )

    def test__aggregated__count(self):
        self.assertEqual(self.log_level_stat_aggregated['count'], 123)

    def test__aggregated__longest_message(self):
        self.assertEqual(
            self.log_level_stat_aggregated['longest_message'], 'test'
        )
