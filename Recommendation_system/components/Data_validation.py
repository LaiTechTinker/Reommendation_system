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
            if status==False:
                raise ValueError("Number of columns are not matching")
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
                self.status1=True
            else:
                self.status1=False
            logging.info(f"Drift detection result: {self.status1}")
            return self.status1

        except Exception as e:
            raise RecomException(e,sys)
