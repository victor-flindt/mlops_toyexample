import logging
from logging import config
from configs.filter_classes import *
from pathlib import Path
import json
from os import getcwd
from random import random
from datetime import datetime


def inference(model, inference_data: str, input_number: int) -> int:
    """ Following function returns a str given a certain input to a given model

    Args:
        mode (torch.model): pytorch.model.model object
        inference_data (str): string data.

    Returns:
        str: returns the output string generated from inference from the model.
    """

    return input_number


def calculate_metrics(model, validataion_data: list[dict]) -> dict:
    """ The following function calculates the params; f1, recall, precision etc.
        given a validation data set

    Args:
        model (torch.model): model to be tested
        validataion_data (list[dict]): data to be tested against

    Returns:
        dict: paramters dict.
    """

    params = {'accuracy':1*random(),
              'f1':1*random(),
              'recall':1*random()}


    return params

def get_parameters() -> dict:
    """ Following function collecst parameters regarding experiment

    Returns:
        dict: Parameter dictionary.
    """

    params = {'Learning rate': 0.01,
              'Experiment start time': datetime.now(),
              'Dataset name': 'dataset A',
              'Compute resource': 'EC2 gndr4xLarge'
              }
    return params


def logger_setup(log_file_name: str, logger_name: str) -> None:
    """Sets up the logger for the script to log to a specific file and logger.
    Args:
        log_file_name (str): filename for the instance of the logger
        logger_name (str): Name of the logger to be configured
    """
    # Check if the logger already exists
    logger = logging.getLogger(logger_name)
    root_logger = logging.getLogger('root')
    
    # If logger doesn't exist, set it up:
    # Load configuration file
    config_file = Path(getcwd() + "/src/project_pandora_toy/configs/log_configs.json")
    with open(config_file) as f_in:
        config = json.load(f_in)
    
    config['handlers']['file']['filename'] = log_file_name
    
    # Check if the logger_name exists in the config
    if logger_name not in config['loggers']:
        # Raise an AssertionError if the logger is not in the config
        raise AssertionError(f"Logger '{logger_name}' is not set up in the config file.")
    
    # Apply the logging configuration
    logging.config.dictConfig(config)
    
    # Get the configured logger
    logger = logging.getLogger(logger_name)
    
    
    ignore_repeated_msg_filter = IgnoreRepeatedMessages()
    exclusive_show_below_error = ShowBelowErrorOnly()

    # Add the filter to the handlers of the specified logger
    for handler in logger.handlers:
        handler.addFilter(ignore_repeated_msg_filter)

    for root_handler in root_logger.handlers:
        if root_handler.get_name() == "stdout_info":
            root_handler.addFilter(exclusive_show_below_error)

    logger.propagate = True 