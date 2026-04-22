from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.exeption.costum_expection import CustomException
from networksecurity.constant import training_pipeline
from networksecurity.logging.loger import get_logger
from sklearn.model_selection import train_test_split
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from datetime import datetime
from typing import List
import pandas as pd
import numpy as np
import pymongo
import certifi
import json
import sys
import os
from networksecurity.entity.artifact_entity import DataIngestionArtifactes

###################################################"
load_dotenv()
uri = os.getenv("MONGO_DB_URI")
logger=get_logger(__name__)



class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=DataIngestionConfig
            logger.info(f"DataIngestionConfig class initiated")
        except Exception as e:
            logger.error(f"Error in DataIngestion: {e}")
            raise CustomException(f"Error occurred while initializing DataIngestion : {e}", sys)
        

    def load_records_as_dataframe(self):
        self.datbase_name=self.data_ingestion_config.database_name
        self.collection_name=self.data_ingestion_config.collection_name
        self.mongodb_client=MongoClient(uri)
        self.db=self.mongodb_client[self.datbase_name]
        collection=self.db[self.collection_name]
        df=pd.DataFrame(list(collection.find()))
        logger.info(f"Data loaded from MongoDB collection: {self.collection_name} in database: {self.datbase_name}")
        if "_id" in df.columns.to_list():
            df.drop("_id",axis=1,inplace=True)
        df.replace({"na":np.nan},inplace=True)
        return df

        


    def export_to_feature_store(self,record:pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            os.makedirs(os.path.dirname(feature_store_file_path),exist_ok=True)
            df=record.to_csv(feature_store_file_path,index=False,header=True)
            return df
        except Exception as e:
            logger.error(f"Error in DataIngestion: {e}")
            raise CustomException(f"Error occurred while initializing DataIngestion : {e}", sys)
    
    
    def split_data_as_train_test(self,dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logger.info("Performed train test split on the dataframe")
            logger.info("Exited split_data_as_train_test method of Data_Ingestion class")
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            
            os.makedirs(dir_path, exist_ok=True)
            
            logger.info(f"Exporting train and test file path.")
            
            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
            )

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True
            )
            logger.info(f"Exported train and test file path.")

            
        except Exception as e:
            raise CustomException(f"Error occurred while initializing DataIngestion : {e}", sys)



    def initiate_data_ingestion(self):
        try:
            self.database=self.load_records_as_dataframe()
            self.dataframe=self.export_to_feature_store(self.database)
            self.split=self.split_data_as_train_test(self.dataframe)
            data_ingestion_model=DataIngestionArtifactes(train_file_path=self.data_ingestion_config.training_file_path,
                                                         test_file_path=self.data_ingestion_config.testing_file_path)
        except Exception as e:
            logger.error(f"Error in DataIngestion: {e}")
            raise CustomException(f"Error occurred while initializing DataIngestion : {e}", sys)
        



