import sys
import os

class Poller():
  def __init__(self, proxy_url, proxy_port, url):
    self.proxy_url = proxy_url
    self.proxy_port = proxy_port
    self.url = url

