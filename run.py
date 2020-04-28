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
logger.info('Start main loop')

#while True:
if True:

    '''
    now = datetime.datetime.now()
    logger.debug(f'Current datetime: {now}')
    logger.info('Setting start time')

    target = datetime.datetime.combine(datetime.date.today(), configurations.TIME_TO_ZIP)
    logger.debug(f'Target datetime: {target}')
    logger.info('Set target time')
    
    if target < now:
        logger.debug(f'Target before adding a day via time delta: {target}')
        target += datetime.timedelta(days=1)
        logger.debug(f'Target after adding a via time delta: {target}')
        logger.info('Adding 1 day to timedelta to delay loop until target time the next day')

    timeToDelay = (target - now).total_seconds()
    logger.info('Being delay')
    logger.debug(f'Delay: {timeToDelay}')
    delay(timeToDelay)

    logger.info('Complete delay and begin zip archive')
    runObject.zipArchive()
    logger.info('Complete archive')
    '''