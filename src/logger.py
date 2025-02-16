# This file contains the code for the logger module
# the module is for logging the information in the log file
# this log file contains the information about the error, warning, and info messages

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)    # path for the log file
os.makedirs(logs_path, exist_ok=True)  # create the directory if it does not exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  # path for the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] - %(lineno)d %(name)s - %(levelname)s - %(message)s"
)


if __name__ == "__main__":
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")