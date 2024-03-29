# Backer

*Note* this was a project to work with paths and zip files. It does zip and store your files but since it stores these backups on your own device it is not a proper backup, it also only saves your files not preferences and other items on your computer. Using software like Time Machine is much better then this repo which was used for learning.

Backup software for maintaining a backup of files in a zip at set times. The program will manage old backups saving backups for a certain amount of days, weeks, and months bases off how the user configures the app. This was created on and for a macbook most items should be avaible on linux.

## Setup

Duplicate `exampleConfig.py` as `config.py` to configure **Absolute paths** to your backup folder and to block any files and folders you don't want to zip or backup.

Go to your terminal.
- Open crontab, you can use your own terminal editor, these instructions will be for vi/vim.
- env EDITOR=vi crontab -e
- Press `i` to change to insert mode
- Next decide the time you want to run the backup. This can be done with [crontab.guru/](https://crontab.guru/) or by editing this line `30 19 * * *`, this line will run at 7:30 pm everyday.
- Lastly add the absolute path to python and the run.py. and add something to create a cron.log file Example: `30 19 * * * /usr/local/bin/python3 /Users/jimdoe/Desktop/backer/run.py >> ~/cron.log 2>&1`
- Save and exit vi/vim by pressing `esc` and `:wq`. This should create a new cronjob that will run at your specified time. This however will not run if you computer is off or sleeping.
- Go to `System Preferences` > `Energy Saver` > `Schedule` and set a startup/wake up time one to two minutes before you want your backup to commence. This way crontab will run the program because your computer is awake.
- Lastly we have to allow cron full disk access to run the program this can be done for Mojave here: [https://blog.bejarano.io/fixing-cron-jobs-in-mojave/](https://blog.bejarano.io/fixing-cron-jobs-in-mojave/).

#### Requirements

[Use a virtualenv to create an isolated enviorment](https://virtualenv.pypa.io/en/latest/)

Run the make command to install requirements

```
make
```

or with pip manually

```
pip3 install -r requirements.txt
```

Edit and setup config.py, then run setup.py

```
python3 setup.py
```

## Running the program

Run description

```
make run
```

or with python manually

```
python3 run.py
```

## Authors

* [**Rafael Cenzano**](https://github.com/RafaelCenzano)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details


This Readme was created with [pystarter](https://github.com/RafaelCenzano/PyStarter)

```
pip3 install pystarter
```
