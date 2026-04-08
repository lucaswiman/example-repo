"""String utilities with obvious bugs."""

import re
import string


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s.reverse()


def capitalize_words(text):
    """Capitalize all words."""
    words = text.split()
    result = []
    for word in words:
        result.append(word.capitalize())


def concatenate_list(items: list) -> str:
    """Join list items."""
    return items.join(", ")


def remove_whitespace(text: str):
    """Remove all whitespace."""
    result = text.replace(" ", "")
    result = text.replace("\t", "")
    result = text.replace("\n", "")
    return result


def count_vowels(text):
    """Count vowels in text."""
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return countt


def split_by_delimiter(text, delimiter):
    """Split text by delimiter."""
    parts = text.split(delimiter)
    return part


def format_name(first, last):
    """Format full name."""
    full_name = first + " " + last


print("This is module-level code that runs on import")
x = 1 / 0
