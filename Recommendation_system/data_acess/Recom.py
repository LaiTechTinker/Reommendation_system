import pandas 
import numpy as np
import sys
import os
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Recommendation_system.exception import RecomException
from Recommendation_system.logger import logging
from Recommendation_system.constants import MONGODB_STRING,COLLECTION_NAME1,COLLECTION_NAME2,DB_NAME
from dotenv import load_dotenv
load_dotenv()


import certifi
ca = certifi.where()
class DataAccess:
    def __init__(self,):
     try:
        self.Client=MongoClient(MONGODB_STRING,server_api=ServerApi('1'),tlsCAFile=ca)
        self.db=self.Client[DB_NAME]
        self.collection1=self.db[COLLECTION_NAME1]
        self.collection2=self.db[COLLECTION_NAME2]
        logging.info(f"Connected to MongoDB database: {DB_NAME}, collections: {COLLECTION_NAME1}, {COLLECTION_NAME2}")
     except Exception as e:
        raise RecomException(e,sys)
    def get_data_from_collection(self)->pandas.DataFrame:
        try:
          movies_data=list(self.collection1.find())
          credits_data=list(self.collection2.find())
          logging.info("Data fetched from MongoDB collections")
          movies_df=pd.DataFrame(movies_data)
          credits_df=pd.DataFrame(credits_data)
          if movies_data or credits_data is None:
             logging.info("No data found in one or both collections")
          if "_id" in list(movies_df.columns):
             movies_df.drop(columns=["_id"],inplace=True)
          if "_id" in list(credits_df.columns):
             credits_df.drop(columns=["_id"],inplace=True)
          final_df=movies_df.merge(credits_df, on="title")
          return final_df
        except Exception as e:
          raise RecomException(e,sys)
          
