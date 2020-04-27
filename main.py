import os
import zipfile
import datetime

'''
File for main code
'''

class Core:

    def __init__(self, configObject):
        
        self.config = configObject
        self.config.FOLDERS_TO_NOT_ZIP.append(self.config.BACKUP_FOLDER)

    def zipArchive(self):

        startZip = datetime.datetime.now()

        folders = []

        for pathItems in self.config.FOLDERS_TO_ZIP:
            folders.append('/' + pathItems + '/')

        todayFormatted = repr(startZip.month) + '-' + repr(startZip.day) + '-' + repr(startZip.year)

        archiveName = os.path.join(self.config.BACKUP_FOLDER, 'day', self.config.BACKUP_NAME + '_' + todayFormatted + '.zip')

        zipper = zipfile.ZipFile(archiveName, 'w', compression=zipfile.ZIP_DEFLATED)

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

        zipper.close()

        endZip = datetime.datetime.now()
        print(end - start)
    