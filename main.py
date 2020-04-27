import os
import zipfile
import logging
import datetime

'''
File for main code
'''


class Core:

    def __init__(self, configObject):
        
        self.config = configObject
        self.config.FOLDERS_TO_NOT_ZIP.append(self.config.BACKUP_FOLDER)

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

    def zipArchive(self):

        startZip = datetime.datetime.now()

        folders = []

        for pathItems in self.config.FOLDERS_TO_ZIP:
            folders.append('/' + pathItems + '/')

        todayFormatted = repr(startZip.month) + '-' + repr(startZip.day) + '-' + repr(startZip.year)

        archiveName = '/' + os.path.join(self.config.BACKUP_FOLDER, 'day', self.config.BACKUP_NAME + '_' + todayFormatted + '.zip')

        with zipfile.ZipFile(archiveName, 'w', compression=zipfile.ZIP_DEFLATED) as zipper:

            for pathThing in folders:

                for root, dirs, files in os.walk(pathThing):

                    for things in files:

                        currentPath = os.path.join(root, things)
                        folderCheck = True

                        for notDirectory in self.config.FOLDERS_TO_NOT_ZIP:
                            if notDirectory in currentPath:
                                folderCheck = False
                                break

                        if folderCheck:

                            if os.path.islink(currentPath):
                                print(f'skipping : {currentPath}')

                            else:
                                fileCheck = True

                                for notFile in self.config.FILES_TO_NOT_ZIP:
                                    if notfile == currentPath:
                                        fileCheck = False

                                if fileCheck:
                                    print(f'zipping : {currentPath}')
                                    zipper.write(currentPath)
                                    

        endZip = datetime.datetime.now()
        print(endZip - startZip)
    