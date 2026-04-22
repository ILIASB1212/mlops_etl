import os 
import pdb
import sys
import numpy as np
import pandas as pd


DATA_INGESTION_COLLECTION_NAME:str="security_data"
DATA_INGESTION_DATABASE_NAME:str="ilias_database"
DATA_INGESTION_DIR_NAME:str="data_ingestion_dir"
DATA_INGESTION_FEATURE_STORE_NAME:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested" 
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2


TARGET_COLUMN:str="result"
PIPELINE_NAME:str="networksecurity"
ARTIFACTS_DIR:str="artifacts"
DATA_FILENAME:str="phisingData.csv"
TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"