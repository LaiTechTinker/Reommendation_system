import os
from Recommendation_system.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
@dataclass
class ArtifactConfig:
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP
artifactConfig:ArtifactConfig=ArtifactConfig()

class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(artifactConfig.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = DATA_INGESTION_COLLECTION_NAME

@dataclass
class DataValidationConfig:
    dataValidationDir:str=os.path.join(artifactConfig.artifact_dir,DATA_VALIDATION_FOLDER)
    report_file_path:str=os.path.join(dataValidationDir,DATE_VALIDATION_REPORT_FILE)
@dataclass
class DataTransformationConfig:
    data_tranform_dir=os.path.join(artifactConfig.artifact_dir,DATA_TRANSFORMATION_DIR)
    train_transformed=os.path.join(data_tranform_dir,DATA_TRANSFORMATION_TRAIN)
    test_transformed=os.path.join(data_tranform_dir,DATA_TRANSFORMATION_TEST)

