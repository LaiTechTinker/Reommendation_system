from Recommendation_system.constants import DATA_VALIDATION_FOLDER, DATE_VALIDATION_REPORT_FILE
import os
import sys
from Recommendation_system.entity.config_entity import DataValidationConfig
from Recommendation_system.entity.artifact_entity import DataValidationArtifact,DataIngestionArtifact
from Recommendation_system.logger import logging
from Recommendation_system.exception import RecomException


#Now let's initiate the data validation component
class DataValidation:
    def __init__(self, data_validation_config:DataValidationConfig,data_ingestion_artifact:DataIngestionArtifact):
        try:
            logging.info("entering the data validation section")
        except Exception as e:
            raise RecomException(e,sys)