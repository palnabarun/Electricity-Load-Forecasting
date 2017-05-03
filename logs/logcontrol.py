import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('info.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def loginfo(text):
    logger.info(text)

def logdebug(text):
    logger.debug(text)

def logwarning(text):
    logger.warn(text)

def logerror(text):
    logger.error(text)
