import main
import config

'''
Run file
'''

# Create config object
configurations = config.Config()

# Create the run object
runObject = main.Core(configurations)

runObject.zipArchive()