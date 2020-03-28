import os

'''
Config for backer

create empty lists for things you don't need or want
'''

class Config:
    
    # Folder to store backups
    BACKUP_FOLDER = os.path.join('Library', 'Backup')

    # Folders to backup
    FOLDERS_TO_BACKUP = [os.path.join('Users', 'jimdoe', 'Documents'), os.path.join('Users', 'jimdoe', 'Downloads'), os.path.join('Users', 'jimdoe', 'Desktop')]

    # Files to backup
    FILES_TO_BACKUP = []

    # Folders to not zip
    FOLDERS_TO_NOT_ZIP = [os.path.join('Users', 'jimdoe', 'Documents', 'thing')]

    # Files to not zip
    FILES_TO_NOT_ZIP = [os.path.join('Users', 'jimdoe', 'Documents', 'file.txt')]