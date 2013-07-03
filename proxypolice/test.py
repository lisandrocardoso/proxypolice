import sys
import os
import logging
import yaml
import datetime

from lib import utils
from lib import pidmanager

from pprint import pprint

if __name__ == '__main__':
  utils.setup_logging(logging.INFO, stream = True)

  logging.info("INFO CHE")
  logging.debug("DEBUG CHE")
  logging.error("ERROR CHE")
   
  utils.setup_logging(logging.INFO, stream = False, filename = 'log')

  logging.info("INFO2CHE")
  logging.debug("DEBUG2CHE")
  logging.error("ERROR2CHE")
 
