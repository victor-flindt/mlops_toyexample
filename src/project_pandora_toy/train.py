# from project_pandora_toy.model import Model
# from project_pandora_toy.data import MyDataset

from utils import logger_setup, calculate_metrics, get_parameters
from datetime import datetime
from logging import getLogger
import time
import mlflow
from tqdm import tqdm
from random import random

def train() -> None:
    """ Main training loop for x,y,z model
    """

    ## Variables
    ## Misc
    best_model_score = 0

    ## Experiment
    EXPERIMENT_RUN_NAME = f"viggo_test_{datetime.now()}"
    EXPERIMENT = 'defect_detection_of_jewlerry_Pandora'

    ## MlFlow
    URL = "http://127.0.0.1"
    PORT = "8080"

    ## mlflow server --host 127.0.0.1 --port 8080

    ## Logger setup
    LOGGER_FILE_PATH = f"logs/train_logger/train_logger_{datetime.now()}.log"
    LOGGER_NAME = "train_logger"
    logger_setup(log_file_name=LOGGER_FILE_PATH,
                 logger_name=LOGGER_NAME)
    train_logger = getLogger(LOGGER_NAME)    

    ## Mlflow setup
    mlflow.set_tracking_uri(uri=URL+":"+PORT)
    # Create a new MLflow Experiment    
    mlflow.set_experiment(EXPERIMENT)
    mlflow.start_run(run_name=EXPERIMENT_RUN_NAME)
    mlflow.log_params(get_parameters())

    train_logger.info(f"Starting training of experiment {EXPERIMENT}, Run name: {EXPERIMENT_RUN_NAME}.")

    for i in tqdm(range(0,11),desc = "Epoc"):
        validation_score = random() 

        train_logger.debug(msg=f"Epoch {i} accuracy {validation_score*10}")
        best_model_score = validation_score*10 if (validation_score*10 > best_model_score) else best_model_score

        if i == 3:
            train_logger.warning(msg= f"OOOHH NOOOO something happened, This is so important we should show it in the terminal")
        metrics = calculate_metrics(None, None)
        mlflow.log_metrics(metrics,step=i)
            
        time.sleep(0.4)
        
    train_logger.info(f"model training done saving best model with accruacy {round(best_model_score,3)}")
    train_logger.debug(f"Ending experiment {EXPERIMENT}, Run name: {EXPERIMENT_RUN_NAME}.")
    mlflow.log_artifact(local_path=LOGGER_FILE_PATH)

    mlflow.end_run()


if __name__ == "__main__":
    train()
