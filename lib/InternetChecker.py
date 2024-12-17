import socket
import requests
from typing import List

class InternetChecker:
    def __init__(self,
                 testUrls: List[str] = None,
                 dnsAddress: str = "8.8.8.8",
                 port: int = 53,
                 timeout: int = 5):
        """
        The InternetChecker class is designed to check internet connectivity via DNS and HTTP.
        
        :param testUrls: List of URLs to check for accessibility.
        :param dnsAddress: The address used to check DNS connectivity.
        :param port: Port number used for DNS connection.
        :param timeout: Maximum wait time (in seconds) for each connection attempt.
        """
        self.testUrls = testUrls if testUrls else ["http://www.google.com"]
        self.dnsAddress = dnsAddress
        self.port = port
        self.timeout = timeout

    def _checkDNS(self) -> bool:
        """
        Checks connectivity via DNS.
        :return: True (successful) or False (failed)
        """
        try:
            socket.create_connection((socket.gethostbyname(self.dnsAddress), self.port), timeout=self.timeout)
            return True
        except (socket.error, socket.timeout) as e:
            print(f"DNS check failed: {e}")
            return False

    def _checkURL(self, url: str) -> bool:
        """
        Checks accessibility to a specific URL via an HTTP request.
        :param url: The URL to check for accessibility.
        :return: True (successful) or False (failed)
        """
        try:
            response = requests.get(url, timeout=self.timeout)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"URL check failed: {url} -> {e}")
            return False

    def check(self) -> bool:
        """
        Checks internet connectivity via both DNS and HTTP.
        :return: True (internet connection available) or False (no internet connection)
        """
        dnsStatus = self._checkDNS()
        urlStatus = any(self._checkURL(url) for url in self.testUrls) # Returns True if any of the URL connections succeed.
        
        if dnsStatus and urlStatus:
            return True
        return False