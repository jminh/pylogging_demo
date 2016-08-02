import logging
import sys

logger = logging.getLogger(__name__)

#logger.addHandler(logging.StreamHandler())
logger.addHandler(logging.StreamHandler(sys.stdout))

logger.setLevel(logging.INFO)

logger.info('hello world')
