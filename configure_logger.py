import logging
import sys
print(__name__)
logger = logging.getLogger(__name__)
default_format = "%(asctime)s - %(name)s --- %(pathname)s:[%(lineno)d]--- - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=default_format, stream=sys.stdout)

logger.info("prem")
