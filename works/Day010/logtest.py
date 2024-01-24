import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def do_something():
    logger.info('info from logtest')
    logger.debug('debug from logtest')