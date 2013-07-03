import sys
import os
import threading
import urllib2
import time
import Queue
import logging
# time.time()

class Poller():
  def __init__(self, config, daemon = True):
    self.config = config
    self.daemon = daemon
    self.q = Queue.Queue()

    self.logger = logging.getLogger('PP')
    self.logger.info("Polled URLs:")
    for url in self.config.get('poller_urls', []):
      self.logger.info("   " + url)
      self.q.put(url)
    self.logger.info("Polling interval: " + str(self.config.get('poller_interval', 0)))
    self.logger.info("Proxy settings : " + self.config.get('poller_proxy_url') + ", " +
                     str(self.config.get('poller_proxy_port')))

  def start_poller(self):
    if self.daemon:
      self.logger.info("Running in daemon mode.")
      pinterval = self.config.get('poller_interval', 0)
      while True:
        url = self.q.get(block = True)
        #logging.getLogger('PP').debug('Polling: ' + url)
        t = threading.Thread(target = self.do_poll, args = (self.q, url, pinterval))
        t.daemon = True
        t.start()
    else:
      self.logger.info("Running in single-run mode.")
      pinterval = 0
      for url in self.config.get('poller_urls', []):
        t = threading.Thread(target = self.do_poll, args = (self.q, url, pinterval))
        t.daemon = True
        t.start()

      while threading.active_count() != 1:
        # We wait for our threads to finish
        pass

  def do_poll(self, q, url, interval):
    #print "Thread Start " + url + " " + str(interval)
    tname = threading.current_thread().name
    logging.getLogger('PP').debug('Thread ' + tname + ' started, polling ' + url)
    start_time = time.time()
    time.sleep(interval)
    q.put(url)
    end_time = time.time()
    diff_time = end_time - start_time
    logging.getLogger('PP').debug('Thread ' + tname + ' execution time: ' + str(diff_time))
    #print "Thread Done " + url

