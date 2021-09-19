import os

from src.helpers.singleton import SingletonPerThread
import datetime


class Logger(metaclass=SingletonPerThread):
    LEVEL_DEBUG = 'DEBUG'
    LEVEL_INFO = 'INFO'
    LEVEL_WARN = 'WARN'
    LEVEL_ERROR = 'ERROR'
    LEVEL_ORDER = [LEVEL_DEBUG, LEVEL_INFO, LEVEL_WARN, LEVEL_ERROR]
    FULL_TIME_FORMAT = '%m/%d/%Y %H:%M:%S'

    def __init__(self, filename=None):
        self.filename = filename
        if self.filename:
            with open(filename, 'w') as f:
                f.write('')

    def write(self, message, loglevel=LEVEL_INFO):
        timestamp = datetime.datetime.now().strftime(self.FULL_TIME_FORMAT)
        new_message = f'{timestamp}: [{loglevel}] {message}\n'
        print(new_message)
        if self.filename:
            with open(self.filename, 'a') as f:
                f.write(new_message)

    def debug(self, message):
        if os.environ.get('LOG_LEVEL') in self.LEVEL_ORDER:
            self.write(message, loglevel=self.LEVEL_DEBUG)

    def info(self, message):
        if os.environ.get('LOG_LEVEL') in self.LEVEL_ORDER[:1]:
            self.write(message, loglevel=self.LEVEL_INFO)

    def warn(self, message):
        if os.environ.get('LOG_LEVEL') in self.LEVEL_ORDER[:2]:
            self.write(message, loglevel=self.LEVEL_WARN)

    def error(self, message):
        if os.environ.get('LOG_LEVEL') in self.LEVEL_ORDER[:3]:
            self.write(message, loglevel=self.LEVEL_ERROR)
