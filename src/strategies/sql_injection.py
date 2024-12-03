from strategy_stub import ScanStrategy
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SqlInjectionScanner(ScanStrategy):
    def __init__(self, url):
        self._url = url
        self._reports = list()
        # change this to chrome before running
        self._driver = webdriver.Firefox()
        self._payloads = list()
        with open("../assets/sql_injection.txt") as payloads:
            for line in payloads.readlines():
                self._payloads.append(line)

    def get_all_formnames(self):
        self._driver.get(self._url)
        contents = self._driver.find_elements(By.TAG_NAME,"input")
        return [content.get_attribute("id") for content in contents]

    def scan(self):
        formnames = self.get_all_formnames()
        for payload in self._payloads:
            try:
                response = requests.post(self._url,{field : payload for field in formnames}, timeout=10, verify=False)
                if response.status_code == 200:
                    self._reports.append(f"SQL Payload got status 200, payload: {payload}, url: {self._url} forms: {formnames}")
                    print(f"SQL Payload got status 200, payload: {payload}, url: {self._url} forms: {formnames}")
            except requests.exceptions.RequestException as e:
                print(f"Error testing SQL Injection on {self._url}: {e}")
    
    def report(self):
        return self._reports
