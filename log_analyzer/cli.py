import sys

from analytics import parse_log
from misc import print_dict_as_json


def entry_point() -> None:
    """Entry point for the CLI."""
    if len(sys.argv) == 2:
        log_path = sys.argv[1]
        print_dict_as_json(parse_log(log_path))
    else:
        raise AttributeError('Log file not found in arguments')
