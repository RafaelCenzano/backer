import os
import backer
import config
import logging
import datetime
from time import sleep as delay

'''
Run file
'''

# Create config object
configurations = config.Config()

# create logger
logger = logging.getLogger(__name__)

# create console and file handler
term = logging.StreamHandler()
logfile = logging.FileHandler('/' + os.path.join(configurations.BACKUP_FOLDER, 'data', 'backer.log'))

# create formatter and add to term and logfile
formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
term.setFormatter(formatter)
logfile.setFormatter(formatter)

# add term and logfile to logger
logger.addHandler(term)
logger.addHandler(logfile)

logger.setLevel(logging.INFO)

# Create the run object
runObject = backer.Core(configurations)


# Create archive
logger.info('Begin zip archive')
runObject.zipArchive()
logger.info('Complete program')