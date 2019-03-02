import os, sys
import ConfigParser

# copy and pasting from stackoverflow !
def load_env_configuration():
    config = ConfigParser.RawConfigParser()
    config.read((os.path.join(os.getcwd(), 'configs/config.cfg')))
    return config

global configp

configp = load_env_configuration()