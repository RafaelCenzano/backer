import os
import datetime

'''
Config for backer

create empty lists for things you don't need or want
'''

class Config:
    
    # Folder to store backups
    BACKUP_FOLDER = os.path.join('Library', 'Backup')

    # Folders to zip
    FOLDERS_TO_ZIP = [os.path.join('Users', 'jimdoe', 'Documents')]

    # Folders to not zip
    FOLDERS_TO_NOT_ZIP = [os.path.join('Users', 'jimdoe', 'Documents', 'thing')]

    # Files to not zip
    FILES_TO_NOT_ZIP = [os.path.join('Users', 'jimdoe', 'Documents', 'file.txt')]

    # Time to zip
    # NOTE: Might slow computer/use up read and write of your storage system.
    # Example 7:30PM local time \/
    TIME_TO_ZIP = datetime.time(hour=19, minute=30, second=20)