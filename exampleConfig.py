import os
import datetime

'''
Config for backer

create empty lists for things you don't need or want

Always use absolute paths within this configuration file
'''

class Config:
    
    # Folder to store backups
    BACKUP_FOLDER = os.path.join('Backup')

    # Backup filename
    BACKUP_NAME = 'backup'

    # Folders to zip
    FOLDERS_TO_ZIP = [os.path.join('Users', 'jimdoe', 'Documents')]

    # Folders to not zip
    FOLDERS_TO_NOT_ZIP = [os.path.join('Users', 'jimdoe', 'Documents', 'thing')]

    # Files to not zip
    FILES_TO_NOT_ZIP = [os.path.join('Users', 'jimdoe', 'Documents', 'file.txt')]

    # Time to zip
    # NOTE: Might slow computer/use up read and write of your storage system.
    # Example 7:30PM local time \/
    TIME_TO_ZIP = datetime.time(hour=12 + 7, minute=30, second=20)

    # How many daily zips to store. 1 - 6 days
    DAYS_TO_STORE = 3

    # How many weekly zips to store 1 - 3 weeks
    WEEKS_TO_STORE = 2

    # How many monthly zips to store 1 - 12 months
    MONTHS_TO_STORE = 6