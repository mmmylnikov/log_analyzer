import json
import sys
from typing import Any


class NotSerializableEncoder(json.JSONEncoder):
    """JSON encoder for non-serializable objects."""

    def default(self, object_cls: Any) -> str:
        """Default method for JSON encoder."""
        return str(object_cls)


def print_dict_as_json(unformatted_data: dict) -> str:
    """Print dictionary as JSON."""
    formated_data = json.dumps(
        unformatted_data,
        indent=4,
        ensure_ascii=False,
        cls=NotSerializableEncoder,
    )
    sys.stdout.write(f'{formated_data}\n')
    return formated_data
