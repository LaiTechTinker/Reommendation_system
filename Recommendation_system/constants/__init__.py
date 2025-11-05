import os
from datetime import date
from dotenv import load_dotenv
load_dotenv()
DB_NAME=os.getenv("DB_NAME")
COLLECTION_NAME1=os.getenv("COLLECTION_NAME1")
COLLECTION_NAME2=os.getenv("COLLECTION_NAME2")
PIPELINE_NAME=os.getenv("PIPELINE_NAME")
ARTIFACT_DIR=os.getenv("ARTIFACT_DIR")
MONGODB_STRING=os.getenv("MONGODB_STRING")


print(MONGODB_STRING)
print(DB_NAME)
"""
Data Ingestion related constants are defined here
"""
DATA_INGESTION_COLLECTION_NAME: str = "Itel_Data"
DATA_INGESTION_DIR_NAME: str = "Data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "raw_data"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
FILE_NAME:str="data.csv"
TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"

"""
The constants for data validation are defined here 
"""
DATA_VALIDATION_FOLDER:str="Data_validation"
DATE_VALIDATION_REPORT_FILE:str="report.yaml"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

"""
data transformation related constants are stored here 
"""
DATA_TRANSFORMATION_DIR:str="Data_transformation"
DATA_TRANSFORMATION_TRAIN="transformed_train.csv"
DATA_TRANSFORMATION_TEST="transformed_test.csv"
