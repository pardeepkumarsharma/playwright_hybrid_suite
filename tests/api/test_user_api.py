from utils.config_reader import Config_Reader
from utils.logger import Logger

logger = Logger.create_logger(__name__)


def test_run():
    c = Config_Reader()
    print(c.get("url"))
    logger.info("This is an info log")
    logger.error("Something went wrong")
    logger.warning("This is a warning message")
    logger.debug("This is a debug message")
    logger.critical("This is a critical message")
