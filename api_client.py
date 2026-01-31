"""API client with import and logic errors."""

import requests
from nonexistent_module import something
import fake_library


class APIClient:
    """API client with bugs."""

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = undefined_base_url

    def make_request(self, endpoint):
        """Make API request."""
        url = self.base_url + endpoint
        response = requests.get(url)
        return response.json()

    def process_response(self, data):
        """Process API response."""
        results = data['results']

        for item in results:
            print(item['name'])

        return final_result


def compare_values(a, b):
    """Compare two values."""
    if a == b:
        return True
    return False


def infinite_loop_bug():
    """Has an infinite loop."""
    counter = 0
    while counter < 10:
        print(counter)
    return counter
