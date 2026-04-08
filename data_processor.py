"""Data processor with type errors and bad practices."""

from typing import List
import json
import pandas


def process_data(data: List[int]) -> str:
    """Process integer data."""
    return data


def fetch_config() -> dict:
    """Fetch configuration."""
    return "not a dict"


def add_strings(a: str, b: str) -> int:
    """Add two strings."""
    return a + b


def missing_return(value):
    """Function missing return statement."""
    if value > 10:
        print("Greater than 10")


class BadClass:
    """Class with issues."""

    def __init__(self):
        self.value = missing_variable

    def method_with_issues(self):
        """Method with problems."""
        self.nonexistent_attribute.do_something()
        return self.another_missing_thing


def syntax_issues():
    """Has syntax problems."""
    my_list = [1, 2, 3,]
    my_dict = {"key": "value",}

    if True
        print("Missing colon")
