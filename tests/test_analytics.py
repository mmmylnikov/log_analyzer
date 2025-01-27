import unittest

from log_analyzer.log import LogLevel, LogLevelMessagesAggregated
from log_analyzer.analytics import (
    _add_level_count,
    _check_longest_message,
    _log_stat,
    parse_log,
)


class TestAddLevelCount(unittest.TestCase):
    log_level_stat: dict[LogLevel, int]

    def setUp(self):
        self.log_level_stat = {
            LogLevel('INFO'): 25,
        }

    def test__add_level_count(self):
        _add_level_count(self.log_level_stat, LogLevel('INFO'))
        self.assertEqual(self.log_level_stat[LogLevel('INFO')], 26)


class TestCheckLongestMessage(unittest.TestCase):
    log_level_stat: dict[LogLevel, str]

    def setUp(self):
        self.log_level_stat = {
            LogLevel('INFO'): 'another text',
        }

    def test__check_longest_message__shorter(self):
        _check_longest_message(self.log_level_stat, LogLevel('INFO'), 'text')
        self.assertEqual(self.log_level_stat[LogLevel('INFO')], 'another text')

    def test__check_longest_message__longer(self):
        _check_longest_message(
            self.log_level_stat, LogLevel('INFO'), 'another longer text'
        )
        self.assertEqual(
            self.log_level_stat[LogLevel('INFO')], 'another longer text'
        )


class TestLogStat(unittest.TestCase):
    levels: list[LogLevel]
    level_counts: dict[LogLevel, int]
    level_longest_messages: dict[LogLevel, str]
    expected_log_stat: dict[str, LogLevelMessagesAggregated]

    def setUp(self):
        self.levels = [
            LogLevel('INFO'),
            LogLevel('DEBUG'),
            LogLevel('WARNING'),
            LogLevel('ERROR'),
        ]
        self.level_counts = {
            LogLevel('INFO'): 25,
            LogLevel('DEBUG'): 14,
            LogLevel('WARNING'): 7,
            LogLevel('ERROR'): 6,
        }
        self.level_longest_messages = {
            LogLevel('INFO'): 'Error successfully handled and logged',
            LogLevel('DEBUG'): 'Query executed: SELECT * FROM users',
            LogLevel('WARNING'): 'Error in query execution',
            LogLevel('ERROR'): 'Error in query execution',
        }
        self.expected_log_stat = {
            'INFO': LogLevelMessagesAggregated(
                level=LogLevel('INFO'),
                count=25,
                longest_message='Error successfully handled and logged',
            ),
            'DEBUG': LogLevelMessagesAggregated(
                level=LogLevel('DEBUG'),
                count=14,
                longest_message='Query executed: SELECT * FROM users',
            ),
            'WARNING': LogLevelMessagesAggregated(
                level=LogLevel('WARNING'),
                count=7,
                longest_message='Error in query execution',
            ),
            'ERROR': LogLevelMessagesAggregated(
                level=LogLevel('ERROR'),
                count=6,
                longest_message='Error in query execution',
            ),
        }

    def test__log_stat(self):
        log_stat = _log_stat(
            self.levels, self.level_counts, self.level_longest_messages
        )
        self.assertDictEqual(log_stat, self.expected_log_stat)


class TestParseLog(unittest.TestCase):
    log_file_test_path: str
    log_stat: dict[str, LogLevelMessagesAggregated]

    def setUp(self):
        self.log_file_test_path = './tests/fixtures/test_log.txt'
        self.log_stat = parse_log(self.log_file_test_path)

    def test__parse_log__count(self):
        self.assertEqual(self.log_stat['INFO']['count'], 25)
        self.assertEqual(self.log_stat['DEBUG']['count'], 14)
        self.assertEqual(self.log_stat['WARNING']['count'], 7)
        self.assertEqual(self.log_stat['ERROR']['count'], 6)

    def test__parse_log__longest_message(self):
        self.assertEqual(
            self.log_stat['INFO']['longest_message'],
            'Error successfully handled and logged',
        )
        self.assertEqual(
            self.log_stat['DEBUG']['longest_message'],
            'Query executed: SELECT * FROM users',
        )
        self.assertEqual(
            self.log_stat['WARNING']['longest_message'],
            'Deprecated function called: oldFunction()',
        )
        self.assertEqual(
            self.log_stat['ERROR']['longest_message'],
            'Failed to connect to external API',
        )
