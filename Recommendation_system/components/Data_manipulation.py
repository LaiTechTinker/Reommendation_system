import pandas as pd
import ast
import sys
from Recommendation_system.logger import logging
from Recommendation_system.constants import *
from pandas import DataFrame
from Recommendation_system.exception import RecomException
from Recommendation_system.entity.artifact_entity import (DataTransformationArtifact,DataIngestionArtifact,DataValidationArtifact)
from Recommendation_system.entity.config_entity import DataTransformationConfig
from Recommendation_system.utils.main_utils import read_yaml_file,write_yaml_file,director_get,convert_to_list,remove_whitespace

class DataTransformation:
  def __init__(self,data_ingest_artifact:DataIngestionArtifact,data_tranformation_config:DataTransformationConfig,data_validation_artifact:DataValidationArtifact):
    self.ingestion_artifact=data_ingest_artifact
    self.transformation_config=data_tranformation_config
    self.validation_artifact=data_validation_artifact
    self.schema_config=read_yaml_file(file_path=SCHEMA_FILE_PATH)

 
  def load_data(self,file_path)->pd.DataFrame:
    df=pd.read_csv(file_path)
    df=df[['id','title','overview','genres','keywords','cast','crew']]
    df=df.dropna(inplace=True)
    for col in self.schema_config["convert_to_list"]:
       df[col]=df[col].apply(self.convert_to_list)
    df["crew"]=df["crew"].apply(self.director_get)
    df["overview"]=df["overview"].apply(lambda x:x.lower().split())
    for col in self.schema_config["remove_whitespace"]:
      df[col]=df[col].apply(remove_whitespace)
    df["combined_features"]=df["overview"]+df["genres"]+df["keywords"]+df["cast"]+df["crew"]
    new_df=df[["id","title","combined_features"]]
    new_df["combined_features"]=new_df["combined_features"].apply(lambda x: ' '.join(x))
    logging.info("load_data_func done")
    return new_df
  def initiate_data_manipulation(self,):
    try:
      data_manipulation_artifact=None
      if self.validation_artifact.drift_message==False:
       logging.info("entered the data_manipulation function")
       train_df=self.load_data(self.ingestion_artifact.training_file_path)
       test_df=self.load_data(self.ingestion_artifact.test_file_path)
       train_df.to_csv(self.transformation_config.train_transformed)
       test_df.to_csv(self.transformation_config.test_transformed)
       data_manipulation_artifact=DataTransformationArtifact(
         transformed_dir=self.transformation_config.data_tranform_dir,
         trasformed_trained_file=self.transformation_config.train_transformed,
         transformed_test_file=self.transformation_config.test_transformed
       )
       
      else: 
        raise ValueError("there is a drift check you data before begining data_manipulation")
      return data_manipulation_artifact
    except Exception as e:
      raise RecomException(e,sys)
      
      
