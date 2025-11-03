from datetime import datetime
import logging
from from_root import from_root
import os
file_name = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_folder="logs"
file_path=os.path.join(from_root(),log_folder,file_name)
os.makedirs(os.path.dirname(file_path),exist_ok=True)
logging.basicConfig(
    filename=file_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
