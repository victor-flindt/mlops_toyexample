from utils import inference, logger_setup
from datetime import datetime
from logging import getLogger
from random import random
def main() -> None:
    """ Inference loop to run in prod for model x,y,z

    Returns:
        _type_: _description_
    """
    LOGGER_FILE_PATH = f"logs/prod_logger/prod_logger_{datetime.now()}.log"
    LOGGER_NAME = "prod_logger"
    logger_setup(log_file_name=LOGGER_FILE_PATH,
                 logger_name=LOGGER_NAME)
    prod_logger = getLogger(LOGGER_NAME)    

    for i in range(10):

        if i != 5:
            prod_logger.debug(f"Inference ran successfully with prediction {i}, with confidence: {round(random(),3)}")

        else: 
            prod_logger.critical(f"Critical error, inference script encountered x,y,z error. Sending email to victor_flindt@pandora.com")

if __name__ == "__main__":
    main()