import main
import config
from time import sleep as delay

'''
Run file
'''

# Create config object
configurations = config.Config()

# Create the run object
runObject = main.Core(configurations)

# Main loop
while True:

    now = datetime.datetime.now()
    target = datetime.datetime.combine(datetime.date.today(), configurations.TIME_TO_ZIP)
    
    if target < now:
        target += datetime.timedelta(days=1)

    delay((target - now).total_seconds())
    runObject.zipArchive()