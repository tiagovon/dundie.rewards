
import logging
import os
from logging import handlers

log_level= os.getenv("LOG_LEVEL","WARNING").upper()
log = logging.getLogger("dundie")
fmt = logging.Formatter( '%(asctime)s %(name)s %(levelname)s l:%(lineno)d' 
                            'f:%(filename)s: %(message)s')


def get_logger(logfile='dundie.log'):
    fh = handlers.RotatingFileHandler(
    logfile, 
    maxBytes=300, # 10**6
    backupCount=10,)

    fh.setLevel(log_level)
    fh.setFormatter(fmt)
    log.addHandler(fh)
    return log 