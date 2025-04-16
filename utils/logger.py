import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

from colorlog import ColoredFormatter


class Logger:
    LOG_DIR = "logs"

    @staticmethod
    def create_logger(name: str) -> logging.Logger:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if not os.path.exists(current_dir):
            os.makedirs(current_dir)
        log_filename = os.path.join(current_dir, Logger.LOG_DIR, f"test_log_{timestamp}.log")

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # Prevent adding multiple handlers
        if not logger.handlers:
            # File handler with rotation
            file_handler = RotatingFileHandler(log_filename, maxBytes=5 * 1024 * 1024, backupCount=5)
            file_formatter = logging.Formatter(
                "%(asctime)s | %(name)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

            # Optional: Console handler with color (can enable if needed)
            console_handler = logging.StreamHandler()
            color_formatter = ColoredFormatter(
                "%(log_color)s%(asctime)s | %(name)s | %(levelname)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                log_colors={
                    'DEBUG': 'cyan',
                    'INFO': 'green',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'bold_red',
                }
            )
            console_handler.setFormatter(color_formatter)
            logger.addHandler(console_handler)

            # logger.propagate = False

        return logger
