import logging
from config.conf import cm

class Log:
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            # create handler to write file
            fh = logging.FileHandler(cm.log_file, encoding='utf-8')
            fh.setLevel(logging.INFO)

            # create handler to console
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # format 
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # add handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'

log = Log().logger

if __name__ == '__main__':
    log.info('Pytest Log')