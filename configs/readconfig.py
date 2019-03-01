import os, sys
import ConfigParser

# define different level of environments

ENV_CONFIG = {
    'dev': 'dev',
    'prod': 'prod',
    'staging': 'staging'
}

def load_env_configuration():
    config = ConfigParser.RawConfigParser()
    config.read((os.path.join(os.getcwd(), 'configs/dev.cfg')))
    return config

global configp

configp = load_env_configuration()