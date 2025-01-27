from dataclasses import dataclass
from datetime import datetime
from typing import TypedDict


@dataclass(frozen=True)
class LogLevel:
    """Log level."""

    name: str


@dataclass
class LogMessage:
    """Message from log file."""

    raw_message: str
    timestamp: datetime
    level: LogLevel
    message: str
    separator: str

    def __init__(self, raw_message: str, separator: str = ' '):
        """Initialize LogMessage."""
        self.raw_message = raw_message.strip()
        self.separator = separator
        self._parse_timestamp()
        self._parse_level()
        self._parse_message()

    def _parse_timestamp(self) -> None:
        raw_timestamp = ' '.join(self.raw_message.split(self.separator)[:2])
        self.timestamp = datetime.strptime(
            raw_timestamp, '%Y-%m-%d %H:%M'
        ).astimezone()

    def _parse_level(self) -> None:
        self.level = LogLevel(self.raw_message.split(self.separator)[2])

    def _parse_message(self) -> None:
        self.message = self.raw_message.split(self.separator, 3)[3]


class LogLevelMessagesAggregated(TypedDict):
    """Aggregated log messages by level."""

    level: LogLevel
    count: int
    longest_message: str
