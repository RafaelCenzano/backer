#from setuptools import setup, find_packages
#from os import getcwd, path
import os
import sys
import json
import config

#currentDir = getcwd()

'''
# Get Readme text
with open(path.join(currentDir, 'README.md'), encoding='utf-8') as fR:
    readme = fR.read()
'''

# Run setup
'''
setup(

    # Project's name
    name='Backer',

    # Project's version number
    # Major.Moderate.Minor values
    version='1.0.0',

    # Project's description
    description='Backup software for maintaining a backup of files and zip and archive at set times',

    # Project's long description
    # Readme can't have links to external pages but 
    # external badges and images are permitted
    long_description=readme,

    # Define markdown long description type
    long_description_content_type='text/markdown'

    # Author's name
    author='Rafael Cenzano',

    # Author's contact
    author_email='savagecoder77@gmail.com',

    # Maintainer's name
    maintainer='Rafael Cenzano',

    # Maintainer's email
    maintainer_email='savagecoder77@gmail.com',

    # Project's home page
    url='https://github.com/RafaelCenzano/backer',

    # Classifiers help users find your project by categorizing it.
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        #'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # Python 2 loses support as of 2020
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # Keywords/Tags
    keywords='backup backer',

    # Finds project files
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Needed installs
    #install_requires=[],

    # Data files
    # package_data={
    #    'sample': ['package_data.dat'],
    # },

    # Python requirement
    #python_requires='>=3.4',

    # Adds CLI
    #entry_points={
    #    'console_scripts': [
    #        'sample cli command = projectName.FileName:FunctionName',
    #    ],
    #},

    # Additional links
    #project_urls={
    #    'Bug Reports': '',
    #    'Source': '',
    #},
)

# setup.py generated using PyStarter
# https://pypi.org/project/PyStarter/
# pip3 install pystarter
# The above message can be deleted, it does not effect the python code.
'''

# Create config object
configurations = config.Config()

# Check for backup folder
if os.path.isdir(f'/{configurations.BACKUP_FOLDER}/') == False:
    sys.exit('Backup folder not found')

# check that folders to zip exsist, exit and alert user if folder not found
for folders in configurations.FOLDERS_TO_ZIP:
    if os.path.isdir(f'/{folders}/') == False:
        sys.exit(f'Folder: {folders} not found')

# Check days to store count is valid
if isinstance(configurations.DAYS_TO_STORE, int) == False or configurations.DAYS_TO_STORE <= 0 or configurations.DAYS_TO_STORE > 6:
    sys.exit('DAYS_TO_STORE is too large or small or not an integer')

# Check weeks to store count is valid
if isinstance(configurations.WEEKS_TO_STORE, int) == False or configurations.WEEKS_TO_STORE <= 0 or configurations.WEEKS_TO_STORE > 3:
    sys.exit('WEEKS_TO_STORE is too large or small or not an integer')

# Check months to store count is valid
if isinstance(configurations.MONTHS_TO_STORE, int) == False or configurations.MONTHS_TO_STORE <= 0 or configurations.MONTHS_TO_STORE > 12:
    sys.exit('MONTHS_TO_STORE is too large or small or not an integer')

# Create day folder to store daily backups, if folder doesn't exsist already
if os.path.isdir(f'/{configurations.BACKUP_FOLDER}/day/') == False:
    os.mkdir(f'/{configurations.BACKUP_FOLDER}/day/')

# Create week folder to store weekly backups, if folder doesn't exsist already
if os.path.isdir(f'/{configurations.BACKUP_FOLDER}/week/') == False:
    os.mkdir(f'/{configurations.BACKUP_FOLDER}/week/')

# Create month folder to store monthly backups, if folder doesn't exsist already
if os.path.isdir(f'/{configurations.BACKUP_FOLDER}/month/') == False:
    os.mkdir(f'/{configurations.BACKUP_FOLDER}/month/')

# Create data folder to store data on backups, if folder doesn't exsist already
if os.path.isdir(f'/{configurations.BACKUP_FOLDER}/data/') == False:
    os.mkdir(f'/{configurations.BACKUP_FOLDER}/data/')

# Create json data file to store backup data, if folder doesn't exsist already
if os.path.isfile(f'/{configurations.BACKUP_FOLDER}/data/data.json') == False:

    jsonData = {
        'month': {},
        'week': {},
        'day': {}
    }
    
    with open(f'/{configurations.BACKUP_FOLDER}/data/data.json', 'w') as jsonFile:
        json.dump(jsonData, jsonFile)

print('Follow instructions in README on how to set up cron jobs')
