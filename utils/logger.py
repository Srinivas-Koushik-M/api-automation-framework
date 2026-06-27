# Logger Utility
import logging
import os
import sys


class Logger:

    @staticmethod
    def get_logger(name, log_file):

        os.makedirs("logs", exist_ok=True)

        logger = logging.getLogger(name)

        if not logger.handlers:

            logger.setLevel(logging.INFO)
            logger.propagate = False

            console_handler = logging.StreamHandler(sys.stdout)

            file_handler = logging.FileHandler(
                f"logs/{log_file}"
            )

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            console_handler.setFormatter(formatter)
            file_handler.setFormatter(formatter)

            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        return logger
