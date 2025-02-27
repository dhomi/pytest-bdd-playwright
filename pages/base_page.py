from playwright.sync_api import Locator
# from conftest import playwright_page
import requests

class ApiPage:
    def __init__(self, base_url):
        self.base_url = base_url

    def put(self, endpoint, json_data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=json_data)
        return response
