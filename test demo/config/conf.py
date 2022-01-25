import os
from selenium.webdriver.common.by import By
from utils.time import dt_strftime


class ConfigManager(object):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # page elements 
    DATA_PATH = os.path.join(BASE_DIR, "data")
    REPORTS_PATH = os.path.join(BASE_DIR, "reports")
    REPORT_FILE = os.path.join(REPORTS_PATH, "allure_data")
    #screenshots
    IMAGE_PATH = os.path.join(REPORTS_PATH, "screeshots")
    #downloaded chromedriver, should be same version with chrome
    CHROMEDRIVER_PATH = os.path.join(BASE_DIR, "chromedriver.exe")

    #page element locate method
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
    }

    #email info
    EMAIL_INFO = {
        'username': 'abc12345131@gmail.com',
        'authcode': '',
        'smtp_host': 'smtp.gmail.com',
        'smtp_port': 465
    }

    #receiver
    ADDRESSEE = [
        'abc12345131@gmail.com',
    ]

    @property
    def log_file(self):
        """LOG_PATH"""
        LOG_PATH = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)
        return os.path.join(LOG_PATH, '{}.log'.format(dt_strftime()))

    @property
    def ini_file(self):
        """config.ini"""
        ini_file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("Setting file %s does not exist!" % ini_file)
        return ini_file


cm = ConfigManager()
if __name__ == '__main__':
    print(cm.BASE_DIR)