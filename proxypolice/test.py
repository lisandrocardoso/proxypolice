import sys
import os
import logging
import yaml
import datetime

from lib import utils
from lib import pidmanager

from pprint import pprint

if __name__ == '__main__':
  utils.setup_logging(logging.DEBUG, stream = True)

  logging.getLogger('PP').debug("DEBUG CHE")
  logging.getLogger('PP').info("INFO CHE")
  logging.getLogger('PP').error("ERROR CHE")
   
  utils.setup_logging(logging.INFO, stream = False, filename = 'log')

  logging.getLogger('PP').info("INFO2CHE")
  logging.getLogger('PP').debug("DEBUG2CHE")
  logging.getLogger('PP').error("ERROR2CHE")
 
