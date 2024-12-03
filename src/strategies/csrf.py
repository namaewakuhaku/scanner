from strategy_stub import ScanStrategy
import requests

class CSRFScanner(ScanStrategy):
    def __init__(self, url):
        self._url = url
        self._reports = list()

    def scan(self):
        try:
            response = requests.get(self._url, timeout=10, verify=False)
            if "csrf_token" not in response.text:
                print(f"Endpoint {self._url} did not have a valid CSRF token")
                self._reports.append(f"Endpoint {self._url} did not have a valid CSRF token")
        except requests.exceptions.RequestException as e:
            print(f"Error testing CSRF on {self._url}: {e}")

    def report(self):
        return self._reports

