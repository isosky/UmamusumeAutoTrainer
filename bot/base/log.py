import logging
import sys
from logging import Logger, Formatter, FileHandler
from logging.handlers import TimedRotatingFileHandler
from config import CONFIG
import time
import colorlog

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

LOG_FILE = 'logs/' + str(CONFIG.logs_name) + '.log'
LOG_TURN_FLIE = 'logs/trace_' + str(CONFIG.role_name) + '_' + str(int(time.time())) + '.log'


def get_logger(name) -> Logger:
    logger = logging.getLogger(name)
    logger.propagate = False
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        fmt = colorlog.ColoredFormatter(
            fmt='%(log_color)s%(asctime)s  %(levelname)-8s [%(funcName)34s] %(filename)-20s: %(message)s',
            log_colors=log_colors_config
        )
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(fmt)
        console_handler.setLevel(logging.DEBUG)
        logger.addHandler(console_handler)

        file_handler = FileHandler(LOG_FILE)
        file_handler.setLevel('ERROR')
        file_handler.setFormatter(Formatter(
            ' %(asctime)s  %(levelname)-8s [%(funcName)34s] %(filename)-20s: %(message)s'))
        logger.addHandler(file_handler)
        # file_handler = FileHandler(LOG_TURN_FLIE)
        # file_handler.setLevel('INFO')
        # file_handler.setFormatter(Formatter(
        #     ' %(asctime)s  %(levelname)-8s [%(funcName)34s] %(filename)-20s: %(message)s'))
        # logger.addHandler(file_handler)

    return logger
