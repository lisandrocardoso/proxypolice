import sys
import os
import logging
import yaml
import datetime

from lib import utils
from lib import pidmanager

from pprint import pprint

if __name__ == '__main__':
  options = utils.parse_cmd_line()
  config = yaml.load(options.config_file)

  logformat = "%(asctime)s %(levelname)s %(message)s"

  if options.debug:
    logging.basicConfig(level=logging.DEBUG, format=logformat)
  else:
    logging.basicConfig(level=logging.INFO, format=logformat)


  if not options.single_run:
    pid = os.fork()
    if pid:
      sys.exit(0)
    logging.info("Running in background")
    pid = os.getpid()
  else:
    pid = os.getpid()
    logging.info("Single run mode")

  log_file_name = config.get('log_file').format(datetime.datetime.now())
  logging.basicConfig(filename=log_file_name)

  pm = pidmanager.PidMgr(config.get('pid_file'), pid)


  logging.info("ProxyPolice 0.1 - PID " + str(pid))
  logging.info("INFO CHE")
  logging.debug("DEBUG CHE")
   

    




  pm.clear_pidfile()

