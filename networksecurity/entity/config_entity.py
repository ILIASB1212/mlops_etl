from datetime import datetime
import json
import os
from networksecurity.constant import training_pipeline
from networksecurity.exeption.costum_expection import CustomException
from networksecurity.logging.loger import get_logger


logger=get_logger(__name__)



print(training_pipeline.DATA_INGESTION_DATABASE_NAME)
print(training_pipeline.DATA_INGESTION_COLLECTION_NAME)
print(training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO)





class TrainingPipelineConfig:
    def __init__(self,time=datetime.now()):
        timestamp=time.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFACTS_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.model_dir=os.path.join("final_model")
        self.timestamp=timestamp
        

class DataIngestionConfig:
    def __init__(self,training_pipelien_onfig:TrainingPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(training_pipelien_onfig.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME
            )
        self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_NAME, training_pipeline.DATA_FILENAME
            )
        self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
            )
        self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
            )
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME