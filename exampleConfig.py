import os

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