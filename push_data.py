from pymongo.mongo_client import MongoClient
import certifi
import dotenv
import os

dotenv.load_dotenv()
uri = os.getenv("MONGO_DB_URI")

# Pass certifi's CA bundle explicitly
client = MongoClient(uri, tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



ca=certifi.where()



from networksecurity.exeption.costum_expection import CustomException
from networksecurity.logging.loger import get_logger
import sys
import pandas as pd
import json
from push_data import client

logger=get_logger(__name__)

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            logger.error(f"Error in NetworkDataExtract: {e}")
            raise CustomException(f"Error occurred while extracting network data : {e}", sys)
        
    def csv_to_json(self,data_path):
        try:
            if data_path.endswith('.csv'):
                logger.info(f"CSV file found at path: {data_path}")
                data=pd.read_csv(data_path)
                data.reset_index(inplace=True,drop=True)
                records=list(json.loads(data.T.to_json()).values())
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

        
