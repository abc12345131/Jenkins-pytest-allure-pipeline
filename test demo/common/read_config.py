import configparser
from config.conf import cm

HOST='HOST'

class ReadConfig(object):
    """settings"""

    def __init__(self):
        self.config = configparser.RawConfigParser()  # contain %, use RawConfigParser
        self.config.read(cm.ini_file, encoding='utf-8')

    def _get(self, section, option):
        """read"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """update"""
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)