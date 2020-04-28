import os
import zipfile
import logging
import datetime

'''
File for main code
'''


class Core:

    def __init__(self, configObject):
        
        # create logger
        self.logger = logging.getLogger(__name__)

        # create console and file handler
        term = logging.StreamHandler()
        logfile = logging.FileHandler('/' + os.path.join(self.config.BACKUP_FOLDER, 'logs', 'backer.log'))

        # create formatter and add to term and logfile
        formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        term.setFormatter(formatter)
        logfile.setFormatter(formatter)

        # add term and logfile to logger
        self.logger.addHandler(term)
        self.logger.addHandler(logfile)

        self.logger.setLevel(logging.INFO)

        self.config = configObject
        self.config.FOLDERS_TO_NOT_ZIP.append(self.config.BACKUP_FOLDER)

        self.logger.debug('Configuration loaded into class variable config')

    def zipArchive(self):

        self.logger.info('Being zipping archive')
        startZip = datetime.datetime.now()
        self.logger.debug(f'Start zip: {startZip}')

        folders = []

        self.logger.info('Being compiling list of folders to zip')
        for pathItems in self.config.FOLDERS_TO_ZIP:
            folders.append(f'/{pathItems}/')
            self.logger.debug(f'Folder added: /{pathItems}/')

        self.logger.info('Format and create path to new file')

        todayFormatted = repr(startZip.month) + '-' + repr(startZip.day) + '-' + repr(startZip.year)
        self.logger.debug(f'Format date: {todayFormatted}')

        archiveName = '/' + os.path.join(self.config.BACKUP_FOLDER, 'day', self.config.BACKUP_NAME + '_' + todayFormatted + '.zip')
        self.logger.debug(f'Archive path and name set: {archiveName}')

        with zipfile.ZipFile(archiveName, 'w', compression=zipfile.ZIP_DEFLATED) as zipper:

            self.logger.info('Create file and being zip proccess')

            for pathThing in folders:

                self.logger.debug(f'Starting folder: {pathThing}')

                for root, dirs, files in os.walk(pathThing):

                    self.logger.debug(f'Current root: {root}')

                    for things in files:

                        currentPath = os.path.join(root, things)
                        self.logger.debug(f'Path to check: {currentPath}')

                        folderCheck = True

                        for notDirectory in self.config.FOLDERS_TO_NOT_ZIP:
                            if notDirectory in currentPath:
                                folderCheck = False
                                self.logger.debug(f'File: {currentPath} : in blocked directory: {notDirectory}')
                                break

                        if folderCheck:

                            if os.path.islink(currentPath):
                                self.logger.debug(f'Symlink found and not zipping: {currentPath}')

                            else:
                                fileCheck = True

                                for notFile in self.config.FILES_TO_NOT_ZIP:
                                    if notfile == currentPath:
                                        fileCheck = False
                                        self.logger.debug(f'File: {currentPath} blocked from being zipped')
                                        break

                                if fileCheck:
                                    self.logger.debug(f'Zipping: {currentPath}')
                                    zipper.write(currentPath)
                                    self.logger.debug(f'Zipped: {currentPath}')

        endZip = datetime.datetime.now()
        self.logger.info('Complete zip archive')
        self.logger.debug(f'Zip completed at {endZip}')

        self.logger.info(f'Operation took {(endZip - startZip).seconds()}')
        self.logger.debug(f'Operation began at {startZip}')
        self.logger.debug(f'Operation ended at {endZip}')


    