from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exeption.costum_expection import CustomException
from networksecurity.constant import training_pipeline
from networksecurity.logging.loger import get_logger
from networksecurity.components.data_validation import (DataIngestionArtifactes, DataValidation,
    DataValidationConfig)
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
import sys



logger=get_logger(__name__)



if __name__=="__main__":
    try:
        data_training_pipeline=TrainingPipelineConfig()
        data_config=DataIngestionConfig(data_training_pipeline)
        data_ingestion=DataIngestion(data_config)
        logger.info("initiations")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)
        logger.info("data_ingestion_completed :::::")
        logger.info("data validation initiated ::::")

        data_validation_config=DataValidationConfig(data_training_pipeline)
        data_validation=DataValidation(data_ingestion_artifact,data_validation_config)
        data_validation_artifacts=data_validation.initiate_data_validation()
        logger.info("data validation completed ::::")
        print(data_validation_artifacts)



    except Exception as e:
            logger.error(f"Error in main file: {e}")
            raise CustomException(f"Error occurred while initializing main files  : {e}", sys)