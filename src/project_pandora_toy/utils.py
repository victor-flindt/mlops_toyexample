import logging
from configs.filter_classes import *
from pathlib import Path
import json
from os import getcwd

def logger_setup(log_file_name: str, logger_name: str) -> None:
    """Sets up the logger for the script to log to a specific file and logger.

    Args:
        log_file_name (str): filename for the instance of the logger
        logger_name (str): Name of the logger to be configured (default: 'pandora_toylogger')
    """

    # Check if the logger already exists
    logger = logging.getLogger(logger_name)

    if logger.hasHandlers():
        # Logger already exists, no need to set it up again
        return

    # If logger doesn't exist, set it up:
    # Load configuration file
    config_file = Path(getcwd() + "/src/project_pandora_toy/configs/log_configs.json")

    with open(config_file) as f_in:
        config = json.load(f_in)

        # Dynamically set the filename for the file handler in the config
        config['handlers']['file']['filename'] = log_file_name

        # Check if the logger_name exists in the config
        if logger_name not in config['loggers']:
            # Raise an AssertionError if the logger is not in the config
            raise AssertionError(f"Logger '{logger_name}' is not set up in the config file.")

    # Apply the logging configuration
    logging.config.dictConfig(config)

    # Create an instance of the filter (if necessary)
    filter = IgnoreRepeatedMessages()

    # Add the filter to the handlers of the specified logger
    for handler in logger.handlers:
        handler.addFilter(filter)

    # Disable propagation to prevent the logs from being forwarded to the root logger
    logger.propagate = False
