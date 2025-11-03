import os
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(levelname)s : %(message)s')

filename="Recommendation_system"
list_files=[
    f"{filename}/components/__init__.py",
    f"{filename}/components/Data_ingestion.py",
    f"{filename}/components/Data_validation.py",
    f"{filename}/components/Data_manipulation.py",
    f"{filename}/components/model_training.py",
    f"{filename}/components/model_evaluation.py",
    f"{filename}/components/model_pusher.py",
    f"{filename}/configuration/__init__.py",
    f"{filename}/constants/__init__.py",
    f"{filename}/components/__init__.py",
    f"{filename}/entity/__init__.py",
    f"{filename}/exception/__init__.py",
    f"{filename}/entity/config_entity.py",
    f"{filename}/entity/artifact_entity.py",
    f"{filename}/utils/__init__.py",
    f"{filename}/logger/__init__.py",
    f"{filename}/utils/main_utils.py",
    f"{filename}/pipline/__init__.py",
    f"{filename}/pipline/training_pipeline.py",
    f"{filename}/pipline/prediction_pipeline.py",
    "requirements.txt",
    "setup.py",
    "demo.py",
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "config/model.yaml",
    "config/schema.yaml"
]
for filepath in list_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for file :{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file:{filename}")
    else:
        logging.info(f"file with name:{filename} already exists")