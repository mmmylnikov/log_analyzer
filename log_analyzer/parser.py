from collections.abc import Generator
from io import TextIOWrapper
from pathlib import Path
from traceback import TracebackException
from typing import Self

from log import LogLevel, LogLevelMessagesAggregated, LogMessage


class LogParser:
    """Class for analyzing log files."""

    file_path: Path
    log_file: TextIOWrapper
    log_stat: dict[LogLevel, LogLevelMessagesAggregated]

    _levels: set[LogLevel]

    def __init__(self, file_path: str):
        """Initialize LogParser."""
        self.file_path = Path(file_path)
        self._levels = set()

    def __enter__(self) -> Self:
        """Open log file."""
        self.log_file = Path.open(self.file_path, 'r')
        return self

    def __exit__(
        self,
        exc_type: type,
        exc_value: BaseException,
        traceback: TracebackException,
    ) -> None:
        """Close log file."""
        self.log_file.close()

    def message_generator(self) -> Generator[LogMessage]:
        """Generate messages from log file."""
        for raw_message in self.log_file:
            message = LogMessage(raw_message)
            self._check_or_add_level(message.level)
            yield message

    def level_generator(self) -> Generator[LogLevel]:
        """Generate levels from log file."""
        yield from self._levels

    def _check_or_add_level(self, level: LogLevel) -> None:
        if level not in self._levels:
            self._levels.add(level)
