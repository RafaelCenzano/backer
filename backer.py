import os
import json
import shutil
import zipfile
import logging
import datetime


'''
File for main code
'''


class Core:

    def __init__(self, configObject):

        self.configurations = configObject
        self.configurations.FOLDERS_TO_NOT_ZIP.append(self.configurations.BACKUP_FOLDER)

        # create logger
        self.logger = logging.getLogger(__name__)

        # create console and file handler
        term = logging.StreamHandler()
        logfile = logging.FileHandler('/' + os.path.join(self.configurations.BACKUP_FOLDER, 'data', 'backer.log'))

        # create formatter and add to term and logfile
        formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        term.setFormatter(formatter)
        logfile.setFormatter(formatter)

        # add term and logfile to logger
        self.logger.addHandler(term)
        self.logger.addHandler(logfile)

        self.logger.setLevel(logging.INFO)

        self.logger.debug('Created logger')
        self.logger.debug('Configuration loaded into class variable config')


    def zipArchive(self):

        self.logger.info('Begining zipping archive')
        startZip = datetime.datetime.now()
        self.logger.debug(f'Start zip: {startZip}')

        folders = []

        self.logger.info('Compiling list of folders to zip')
        for pathItems in self.configurations.FOLDERS_TO_ZIP:
            folders.append(f'/{pathItems}/')
            self.logger.debug(f'Folder added: /{pathItems}/')

        self.logger.info('Format and create path to new file')

        todayFormatted = repr(startZip.month) + '-' + repr(startZip.day) + '-' + repr(startZip.year)
        self.logger.debug(f'Format date: {todayFormatted}')

        archiveName = '/' + os.path.join(self.configurations.BACKUP_FOLDER, 'day', self.configurations.BACKUP_NAME + '_' + todayFormatted + '.zip')
        self.logger.debug(f'Archive path and name set: {archiveName}')

        with zipfile.ZipFile(archiveName, 'w', compression=zipfile.ZIP_DEFLATED) as zipper:

            self.logger.info('Create file and begin zip proccess')

            for pathThing in folders:

                self.logger.debug(f'Starting folder: {pathThing}')

                for root, dirs, files in os.walk(pathThing):

                    self.logger.debug(f'Current root: {root}')

                    for things in files:

                        currentPath = os.path.join(root, things)
                        self.logger.debug(f'Path to check: {currentPath}')

                        folderCheck = True

                        for notDirectory in self.configurations.FOLDERS_TO_NOT_ZIP:
                            if notDirectory in currentPath:
                                folderCheck = False
                                self.logger.debug(f'File: {currentPath} : in blocked directory: {notDirectory}')
                                break

                        if folderCheck:

                            if os.path.islink(currentPath):
                                self.logger.debug(f'Symlink found and not zipping: {currentPath}')

                            else:
                                fileCheck = True

                                for notFile in self.configurations.FILES_TO_NOT_ZIP:
                                    if '/' + notFile == currentPath:
                                        fileCheck = False
                                        self.logger.debug(f'File: {currentPath} blocked from being zipped')
                                        break

                                if fileCheck:
                                    self.logger.debug(f'Zipping: {currentPath}')
                                    zipper.write(currentPath)
                                    self.logger.debug(f'Zipped: {currentPath}')

        endZip = datetime.datetime.now()
        self.logger.info(f'Zip completed at {endZip}')

        self.logger.info(f'Operation took {endZip - startZip}')
        self.logger.debug(f'Operation began at {startZip}')
        self.logger.debug(f'Operation ended at {endZip}')

        with open(f'/{self.configurations.BACKUP_FOLDER}/data/data.json', 'r') as jsonFile:
            jsonData = json.load(jsonFile)

        now = datetime.datetime.now()
        datetimeFormat = '%m/%d/%Y'

        if not bool(jsonData['month']):

            self.logger.info('new backup system being setup')

            shutil.copyfile(archiveName, '/' + os.path.join(self.configurations.BACKUP_FOLDER, 'month', self.configurations.BACKUP_NAME + '_' + todayFormatted + '.zip'))
            self.logger.debug('Copy file to month folder')
            shutil.copyfile(archiveName, '/' + os.path.join(self.configurations.BACKUP_FOLDER, 'week', self.configurations.BACKUP_NAME + '_' + todayFormatted + '.zip'))
            self.logger.debug('Copy file to week folder')

            jsonData['day'][archiveName] = now.strftime(datetimeFormat)
            jsonData['week']['/' + os.path.join(self.configurations.BACKUP_FOLDER, 'week', self.configurations.BACKUP_NAME + '_' + todayFormatted + '.zip')] = now.strftime(datetimeFormat)
            jsonData['month']['/' + os.path.join(self.configurations.BACKUP_FOLDER, 'month', self.configurations.BACKUP_NAME + '_' + todayFormatted + '.zip')] = now.strftime(datetimeFormat)
            self.logger.debug('Add initial Json data')

        else:

            jsonData['day'][archiveName] = now.strftime(datetimeFormat)
            timeDeltaDays0 = []
            timeDeltaDays1 = []

            for archive in jsonData['week']:
                then = datetime.datetime.strptime(jsonData['week'][archive], datetimeFormat)
                timeDeltaDays0.append((now - then).days)

            minimumDeltaDay = min(timeDeltaDays0)

            if minimumDeltaDay >= 7:
                self.logger.info('Adding new week item')
                shutil.copyfile(archiveName, '/' + os.path.join(self.configurations.BACKUP_FOLDER, 'week', self.configurations.BACKUP_NAME + '_' + todayFormatted + '.zip'))
                jsonData['week']['/' + os.path.join(self.configurations.BACKUP_FOLDER, 'week', self.configurations.BACKUP_NAME + '_' + todayFormatted + '.zip')] = now.strftime(datetimeFormat)

            for archive in jsonData['month']:
                then = datetime.datetime.strptime(jsonData['month'][archive], datetimeFormat)
                timeDeltaDays1.append((now - then).days)

            minimumDeltaDay = min(timeDeltaDays1)

            if minimumDeltaDay >= 30:
                self.logger.info('Adding new month item')
                shutil.copyfile(archiveName, '/' + os.path.join(self.configurations.BACKUP_FOLDER, 'month', self.configurations.BACKUP_NAME + '_' + todayFormatted + '.zip'))
                jsonData['month']['/' + os.path.join(self.configurations.BACKUP_FOLDER, 'month', self.configurations.BACKUP_NAME + '_' + todayFormatted + '.zip')] = now.strftime(datetimeFormat)


            if len(jsonData['day']) > self.configurations.DAYS_TO_STORE:
                self.logger.info('Clearing old days')
                numberOver = len(jsonData['day']) - self.configurations.DAYS_TO_STORE
                self.logger.debug(f'Clearing {numberOver} day items')
                for i in range(numberOver):
                    timeDeltaDays = []

                    for archive in jsonData['day']:
                        then = datetime.datetime.strptime(jsonData['day'][archive], datetimeFormat)
                        timeDeltaDays.append((now - then).days)

                    maximumDeltaDay = max(timeDeltaDays)

                    for archive in jsonData['day']:
                        then = datetime.datetime.strptime(jsonData['day'][archive], datetimeFormat)
                        if (now - then).days == maximumDeltaDay:
                            self.logger.debug(f'Delete {archive}')
                            os.remove(archive)
                            del jsonData['day'][archive]
                            break


            if len(jsonData['week']) > self.configurations.WEEKS_TO_STORE:
                self.logger.info('Clearing old weeks')
                numberOver = len(jsonData['week']) - self.configurations.WEEKS_TO_STORE
                self.logger.debug(f'Clearing {numberOver} week items')
                for i in range(numberOver):
                    timeDeltaDays = []

                    for archive in jsonData['week']:
                        then = datetime.datetime.strptime(jsonData['week'][archive], datetimeFormat)
                        timeDeltaDays.append((now - then).days)

                    maximumDeltaDay = max(timeDeltaDays)

                    for archive in jsonData['week']:
                        then = datetime.datetime.strptime(jsonData['week'][archive], datetimeFormat)
                        if (now - then).days == maximumDeltaDay:
                            self.logger.debug(f'Delete {archive}')
                            os.remove(archive)
                            del jsonData['week'][archive]
                            break


            if len(jsonData['month']) > self.configurations.MONTHS_TO_STORE:
                self.logger.info('Clearing old months')
                numberOver = len(jsonData['month']) - self.configurations.MONTHS_TO_STORE
                self.logger.debug(f'Clearing {numberOver} month items')
                for i in range(numberOver):
                    timeDeltaDays = []

                    for archive in jsonData['month']:
                        then = datetime.datetime.strptime(jsonData['month'][archive], datetimeFormat)
                        timeDeltaDays.append((now - then).days)

                    maximumDeltaDay = max(timeDeltaDays)

                    for archive in jsonData['month']:
                        then = datetime.datetime.strptime(jsonData['month'][archive], datetimeFormat)
                        if (now - then).days == maximumDeltaDay:
                            self.logger.debug(f'Delete {archive}')
                            os.remove(archive)
                            del jsonData['month'][archive]
                            break

        self.logger.info('Complete Json work')

        with open(f'/{self.configurations.BACKUP_FOLDER}/data/data.json', 'w') as jsonFile:
            json.dump(jsonData, jsonFile)

        self.logger.debug('Dump and write to json file')



    