import logging
from enum import Enum

from . import config

class status(Enum):
    OK = 0
    URL_VALIDATION_FAILED = 1
    FETCHING_OR_DECODING_ERROR = 2
    UNEXPECTED_SERVER_RESPONSE = 3
    HTML_DOM_PARSING_ERROR = 4
    URL_NOT_FOUND = 5


def configure_loggers():
    default_format = '%(asctime)s %(levelname)s\t%(name)s:\t%(message)s'
    default_date_format = '%H:%M:%S'
    default_formatter = logging.Formatter(default_format, default_date_format)

    logging.basicConfig(
        level=logging.INFO,
        format=default_format,
        datefmt=default_date_format
    )

    mainLoggerFileHandler = logging.FileHandler(config.APP_LOG_FILE)
    mainLoggerFileHandler.setFormatter(default_formatter)
    mainLoggerFileHandler.setLevel(logging.DEBUG)
    mainLogger = logging.getLogger('main')
    mainLogger.setLevel(logging.DEBUG)

    logging.getLogger().addHandler(mainLoggerFileHandler)
    mainLogger.addHandler(mainLoggerFileHandler)
