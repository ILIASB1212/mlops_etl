from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exeption.costum_expection import CustomException
from networksecurity.constant import training_pipeline
from networksecurity.logging.loger import get_logger
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
import sys
from networksecurity.entity.config_entity import(DataIngestionConfig,
                                                 TrainingPipelineConfig,
                                                 DataValidationConfig,
                                                 DataTransformationConfig,
                                                 ModelTrainerConfig)

from networksecurity.entity.artifact_entity import (DataIngestionArtifactes,
                                                 DataValidationArtifact,
                                                 DataTransformationArtifact,
                                                 ModelTrainerArtifact)


logger=get_logger(__name__)




class TrainPipeline:
    def __init__(self):
        try:
            self.training_pipeline_config=TrainingPipelineConfig()
        except Exception as e:
            raise CustomException(e,sys)
        
    def start_data_ingestion(self):
            logger.info("Starting data ingestion")
            self.data_ingestion_config=DataIngestionConfig(training_pipelien_onfig=self.training_pipeline_config)
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion() 
            logger.info("Data ingestion completed")
            return data_ingestion_artifact
        

    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifactes):
            try:
                self.data_ingestion_artifact=data_ingestion_artifact
                data_validation_config=DataValidationConfig(self.data_ingestion_artifac)
                data_validation=DataValidation(data_ingestion_artifact,data_validation_config)
                data_validation_artifacts=data_validation.initiate_data_validation()
                logger.info("Data validation completed ::::")
                return data_validation_artifacts
            except Exception as e:
                raise CustomException(e,sys)
            
    def start_data_transformation(self,data_validation_artifact:DataValidationArtifact):
            try:
                self.data_validation_artifact=data_validation_artifact
                logger.info("data transformation  initiated ::::")
                data_transformation_config=DataTransformationConfig(self.data_validation_artifact)
                data_transformation=DataTransformation(data_transformation_config,data_transformation_config)
                data_transformation_artifacts=data_transformation.initiate_data_transformation()
                logger.info("data transformation completed ::::")
                return data_transformation_artifacts
            except Exception as e:
                raise CustomException(e,sys)
            
    def start_model_trainner(self,data_transformation_artifact:DataTransformationArtifact):
            try:
                self.data_transformation_artifact=data_transformation_artifact
                logger.info("data training  initiated ::::")
                model_trainner_config=ModelTrainerConfig(self.data_transformation_artifact)
                # CORRECT - config first, then artifact
                model_trainner = ModelTrainer(model_trainner_config, model_trainner_config)
                model_trainner_artifacts=model_trainner.initiate_model_trainer()
                logger.info("data training completed ::::")
                return model_trainner_artifacts
            except Exception as e:
                raise CustomException(e,sys)
            


    def run_pipeline(self):
            try:
                data_ingestion_artifact=self.start_data_ingestion()
                data_validation_artifact=self.start_data_validation(data_ingestion_artifact)
                data_transformation_artifact=self.start_data_transformation(data_validation_artifact)
                model_trainner_artifacts=self.start_model_trainner(data_transformation_artifact)
                return model_trainner_artifacts
            except Exception as e:
                raise CustomException(e,sys)
