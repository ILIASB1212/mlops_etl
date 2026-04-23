from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exeption.costum_expection import CustomException
from networksecurity.constant import training_pipeline
from networksecurity.logging.loger import get_logger
from networksecurity.components.data_validation import (DataValidation,
    DataValidationConfig)
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataTransformationConfig
from networksecurity.components.data_transformation import DataTransformationConfig,DataTransformation
from networksecurity.components.model_trainer import (ModelTrainer,
    ModelTrainerConfig)
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
        logger.info("data transformation  initiated ::::")
        data_transformation_config=DataTransformationConfig(data_training_pipeline)
        data_transformation=DataTransformation(data_validation_artifacts,data_transformation_config)
        data_transformation_artifacts=data_transformation.initiate_data_transformation()
        logger.info("data transformation completed ::::")
        print("1)))))data transformation done ")


        logger.info("data training  initiated ::::")
        model_trainner_config=ModelTrainerConfig(data_training_pipeline)
        model_trainner=ModelTrainer(data_transformation_artifacts,model_trainner_config)
        model_trainner_artifacts=data_transformation.initiate_data_transformation()
        logger.info("data training completed ::::")
        print("2)))))data training done ")





    except Exception as e:
            logger.error(f"Error in main file: {e}")
            raise CustomException(f"Error occurred while initializing main files  : {e}", sys)