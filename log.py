import logging
import logging.handlers

log_file='tst.log'
handler= logging.handlers.RotatingFileHandler(log_file,maxBytes=1024*1024,backupCount=5)
fmt='%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter=Logging.Formatter(fmt)
handler.setFormatter(formatter)

logging = logging.getLogger('tst')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info('first info message')
logger.debug('first debug message')
