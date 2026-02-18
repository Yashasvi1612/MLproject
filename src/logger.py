import logging
import os 
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs") # this will give us the path to the logs folder and the log file name
os.makedirs(os.path.dirname(logs_dir), exist_ok=True) # this will create the logs

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE) # this will give us the path to the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started.")
