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

        zipper = zipfile.ZipFile('item.zip', 'w', zipfile.ZIP_DEFLATED)

        zipper.close()
    