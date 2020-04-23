import os
import zipfile
import datetime

'''
File for main code
'''

class Core:

    def __init__(self, configObject):
        
        self.config = configObject

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
                    if '/Users/rafael/Documents/3D printing/' not in currentPath:
                        if os.path.islink(currentPath):
                            print(f'skipping : {currentPath}')
                        else:
                            if currentPath != '/Users/rafael/Documents/Programming/notebooks/testing/item.zip':
                                print(f'zipping : {currentPath}')
                                zipper.write(currentPath)

        zipper.close()

        endZip = datetime.datetime.now()
        print(end - start)
    