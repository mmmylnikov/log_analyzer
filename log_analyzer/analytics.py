from collections import defaultdict

from log import LogLevel, LogLevelMessagesAggregated
from parser import LogParser


def _add_level_count(
    level_count_dict: dict[LogLevel, int], level: LogLevel
) -> None:
    level_count_dict[level] += 1


def _check_longest_message(
    level_longest_messages_dict: dict[LogLevel, str],
    level: LogLevel,
    message: str,
) -> None:
    if len(message) < len(level_longest_messages_dict[level]):
        return
    level_longest_messages_dict[level] = message


def _log_stat(
    levels: list[LogLevel],
    level_counts: dict[LogLevel, int],
    level_longest_messages: dict[LogLevel, str],
) -> dict[str, LogLevelMessagesAggregated]:
    return {
        level.name: LogLevelMessagesAggregated(
            level=level,
            count=level_counts[level],
            longest_message=level_longest_messages[level],
        )
        for level in levels
    }


def parse_log(log_path: str) -> dict[str, LogLevelMessagesAggregated]:
    """Parse log file.

    Returns dictionary with log statistics.

    Args:
        log_path: Path to log file.

    Returns:
        Dictionary with log statistics.
    """
    level_counts: dict[LogLevel, int] = defaultdict(int)
    level_longest_messages: dict[LogLevel, str] = defaultdict(str)

    with LogParser(file_path=log_path) as parser:
        for message in parser.message_generator():
            _add_level_count(level_counts, message.level)
            _check_longest_message(
                level_longest_messages, message.level, message.message
            )
        levels = list(parser.level_generator())
    return _log_stat(levels, level_counts, level_longest_messages)
