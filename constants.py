# reads values from config.ini and returns them
import configparser
import os

if os.path.isfile('config.ini'):
    prefix = ''
elif os.path.isfile('sailbot/config.ini'):
    prefix = 'sailbot/'
elif os.path.isfile('sailbot/sailbot/config.ini'):
    prefix = 'sailbot/sailbot/'
elif os.path.isfile('src/sailbot/sailbot/config.ini'):
    prefix = 'src/sailbot/sailbot/'
else:
    raise Exception(F"cannot find config.ini file in {os.getcwd()}")

config = configparser.ConfigParser()
config.read(F'{prefix}config.ini')
    
def save():
    with open('../config.ini', 'w') as configfile:
        config.write(configfile) 

if __name__ == '__main__':

    print(config.sections())
    print(config['CONSTANTS']['win_title'])
