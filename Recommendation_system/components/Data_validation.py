from Recommendation_system.constants import DATA_VALIDATION_FOLDER, DATE_VALIDATION_REPORT_FILE,SCHEMA_FILE_PATH
import os
from pandas import DataFrame
from evidently import DataDefinition
from evidently import Report
import pandas as pd
import json
from evidently.presets import DataDriftPreset, DataSummaryPreset
import sys
from Recommendation_system.entity.config_entity import DataValidationConfig
from Recommendation_system.entity.artifact_entity import DataValidationArtifact,DataIngestionArtifact
from Recommendation_system.logger import logging
from Recommendation_system.exception import RecomException
from Recommendation_system.utils.main_utils import read_yaml_file,write_yaml_file
#Now let's initiate the data validation component
class DataValidation:
    def __init__(self, data_validation_config:DataValidationConfig,data_ingestion_artifact:DataIngestionArtifact):
        try:
            logging.info("entering the data validation section")
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self.schema_config=read_yaml_file(file_path=SCHEMA_FILE_PATH)
            self.status1=None

        except Exception as e:
            raise RecomException(e,sys)
    def validate_number_of_columns(self,data:DataFrame) -> bool:
        try:
            logging.info("entered the columns validation section")
            status=len(data.columns)==len(self.schema_config["columns"])
            logging.info(f"ingested data contains all columns:{status}")
           
            return status
        except Exception as e:
            raise RecomException(e,sys)
    @staticmethod
    def read_data(file_path) -> DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise RecomException(e, sys)
    def detect_dataset_drift(self, reference_df: DataFrame, current_df: DataFrame, ) -> bool:
        """
        Method Name :   detect_dataset_drift
        Description :   This method validates if drift is detected
        
        Output      :   Returns bool value based on validation results
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            status=None
            report = Report([DataDriftPreset() ])
            my_eval = report.run(reference_data=reference_df, current_data=current_df)
            report=my_eval.json()
            json_report=json.loads(report)
            write_yaml_file(file_path=self.data_validation_config.report_file_path, content=json_report)
            item=json_report["metrics"]
            n_features=len([ite["metric_id"] for ite in item])
            # n_drifted_features=json_report["number_of_drifted_features"]
            n_drifted_features =len([ite for ite in item if isinstance(ite["value"], (float, int)) and ite["value"] < 0.01])
            logging.info(f"{n_drifted_features}/{n_features} drift detected.")
            if n_drifted_features>0:
                status=True
            else:
                status=False
            logging.info(f"Drift detection result: {status}")
            return status

        except Exception as e:
            raise RecomException(e,sys)
    def initiate_data_validation(self,):
     try:
        drift_message=""
        logging.info("entered data validation initation")
        train_file,test_file=(DataValidation.read_data(self.data_ingestion_artifact.training_file_path),
                              DataValidation.read_data(self.data_ingestion_artifact.test_file_path))
        column_status=self.validate_number_of_columns(train_file)
        logging.info(f"The status of all the columns in the training file{column_status}")
        column_status=self.validate_number_of_columns(test_file)
        logging.info(f"The status of all the columns in the testing file is {column_status} ")
        drift_status=self.detect_dataset_drift(reference_df=train_file,current_df=test_file)
        if drift_status:
            logging.info("drift detected in your data trying checking for it")
            drift_message="drift detected in your data"
        else:
            logging.info("no drift detected in the data")
            drift_message="no drift detected in your data"
        data_validation_artifact=DataValidationArtifact(
            report_file_path=self.data_validation_config.report_file_path,
            drift_message=drift_message
        )
        return data_validation_artifact
     except Exception as e:
         raise RecomException(e,sys)
    