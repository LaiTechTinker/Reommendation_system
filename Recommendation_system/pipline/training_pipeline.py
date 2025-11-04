import sys
from Recommendation_system.exception import RecomException
from Recommendation_system.logger import logging
from Recommendation_system.components.Data_ingestion import DataIngestion
from Recommendation_system.components.Data_validation import DataValidation
from Recommendation_system.entity.config_entity import (DataIngestionConfig,DataValidationConfig)
from Recommendation_system.entity.artifact_entity import (DataIngestionArtifact,DataValidationArtifact)  
                                         


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config=DataValidationConfig() 
    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise RecomException(e, sys) from e
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            logging.info("entered the start_data_validation method")
            datavalidation=DataValidation(data_validation_config=self.data_validation_config,data_ingestion_artifact=data_ingestion_artifact)
        except Exception as e:
            raise RecomException(e,sys)

        
    def run_pipeline(self, ) -> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            logging.info(f"data ingest artifact:{data_ingestion_artifact}")
            logging.info(f"data ingest artifact:{data_validation_artifact}")
        except Exception as e:
            raise RecomException(e, sys)
        