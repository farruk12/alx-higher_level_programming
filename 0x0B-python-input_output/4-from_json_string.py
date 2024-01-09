#!/usr/bin/python3
"""Module: my_module"""

import json

def from_json_string(my_str):
    """Converts a JSON string to a Python data structure.

    Args:
        my_str (str): A JSON-formatted string.

    Returns:
        object: A Python data structure representing the JSON string.

    Raises:
        ValueError: If the input string is not a valid JSON.
    """
    return json.loads(my_str)
