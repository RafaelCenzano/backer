import os
import main
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
logfile = logging.FileHandler('/' + os.path.join(configurations.BACKUP_FOLDER, 'logs', 'backer.log'))

# create formatter and add to term and logfile
formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
term.setFormatter(formatter)
logfile.setFormatter(formatter)

# add term and logfile to logger
logger.addHandler(term)
logger.addHandler(logfile)

logger.setLevel(logging.INFO)

# Create the run object
runObject = main.Core(configurations)

runObject.zipArchive()

# Main loop
#while True:
if True:

    '''
    now = datetime.datetime.now()
    target = datetime.datetime.combine(datetime.date.today(), configurations.TIME_TO_ZIP)
    
    if target < now:
        target += datetime.timedelta(days=1)

    delay((target - now).total_seconds())
    runObject.zipArchive()
    '''