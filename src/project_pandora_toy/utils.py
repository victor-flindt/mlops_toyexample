
def logger_setup(log_file_name: str, logger_name: str = 'FS_logger') -> None:
    """Sets up the logger for the script to log to a specific file and logger.

    Args:
        log_file_name (str): filename for the instance of the logger
        logger_name (str): Name of the logger to be configured (default: 'FS_logger')
    """

    # Check if the logger already exists
    logger = logging.getLogger(logger_name)

    if logger.hasHandlers():
        # Logger already exists, no need to set it up again
        return

    # If logger doesn't exist, set it up:
    # Load configuration file
    config_file = Path(os.getcwd() + "/logs/loggings_configs/config.json")

    with open(config_file) as f_in:
        config = json.load(f_in)

        # Dynamically set the filename for the file handler in the config
        config['handlers']['file']['filename'] = log_file_name

        # Check if logger_name is in config, and if not, add it
        if logger_name not in config['loggers']:
            config['loggers'][logger_name] = {
                'level': 'DEBUG',
                'handlers': ['stderr', 'file']
            }

    # Apply the logging configuration
    logging.config.dictConfig(config)

    # Create an instance of the filter (if necessary)
    filter = IgnoreRepeatedMessages()

    # Add the filter to the handlers of the specified logger
    for handler in logger.handlers:
        handler.addFilter(filter)

    # Disable propagation to prevent the logs from being forwarded to the root logger
    logger.propagate = False
