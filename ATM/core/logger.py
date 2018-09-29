import logging
import sys
import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

from conf import setting


def logger(log_type):
    logger = logging.getLogger(log_type)
    logger.setLevel(setting.LOG_LEVEL)

    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    log_dir = os.path.join(setting.BASE_DIR,'log',setting.LOG_TYPE[log_type])
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)

    fh = logging.FileHandler(log_dir)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

if __name__ == '__main__':
    logger('access').info('helllo+       +___')


