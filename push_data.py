from networksecurity.exeption.costum_expection import CustomException
from networksecurity.logging.loger import get_logger
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import pandas as pd
import certifi
import dotenv
import json
import sys
import os



load_dotenv()
uri = os.getenv("MONGO_DB_URI")
ca=certifi.where()




logger=get_logger(__name__)

class NetworkDataExtract:
    def __init__(self):
        try:
            logger.info("NetworkDataExtract class initiated")
        except Exception as e:
            logger.error(f"Error in NetworkDataExtract: {e}")
            raise CustomException(f"Error occurred while extracting network data : {e}", sys)
        
    def csv_to_json(self,data_path):
        try:
            if data_path.endswith('.csv'):
                logger.info(f"CSV file found at path: {data_path}")
                data=pd.read_csv(data_path) # load data as csv
                data.reset_index(inplace=True,drop=True) #remove index 
                records=list(json.loads(data.T.to_json()).values()) #convert to list of jsons
                logger.info(f"data loaded to mongo db")
                return records
        except Exception as e:
            logger.error(f"Error in csv_tojson: {e}")
            raise CustomException(f"Error occurred while converting csv to json : {e}", sys)
            
    def load_data_to_mongodb(self,db_name,record,collection_name):
        try:
            self.database=db_name
            self.reecord=record
            self.collection=collection_name

            self.mongo_client=MongoClient(uri)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.reecord)
            logger.info(f"Data loaded to MongoDB successfully in database: {self.database}")
            return self.collection
        except Exception as e:
            logger.error(f"Error in load_data_to_mongodb: {e}")
            raise CustomException(f"Error occurred while loading data to MongoDB : {e}", sys)
        



if __name__=="__main__":
    DataPath="security_data\phisingData.csv"
    DataBase="ilias_database"
    Collection="network_security_collection"
    network_data_extract=NetworkDataExtract()
    records=network_data_extract.csv_to_json(DataPath)
    print(f"Records extracted: {records}")
    nor=network_data_extract.load_data_to_mongodb(DataBase,records,Collection)
    print("Data loaded to MongoDB successfully")
    print("Collection Name:", nor.name)
    print(f"numbers of records {nor}")

        
