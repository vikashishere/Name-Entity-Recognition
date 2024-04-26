import sys
from ner.components.data_ingestion import DataIngestion
# from ner.components.data_transforamation import DataTransformation
# from ner.components.model_trainer import ModelTraining
# from ner.components.model_evaluation import ModelEvaluation
# from ner.components.model_pusher import ModelPusher
from ner.configuration.gcloud import GCloud
from ner.constants import *

from ner.entity.artifact_entity import (DataIngestionArtifacts)


from ner.entity.config_entity import (DataIngestionConfig)


from ner.exception import NerException
from ner.logger import logging


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        # self.data_transformation_config = DataTransformationConfig()
        # self.model_training_config = ModelTrainingConfig()
        # self.model_evaluation_config = ModelEvalConfig()
        # self.model_pusher_config = ModelPusherConfig()
        self.gcloud = GCloud()


    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from Google cloud storage")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config, gcloud=self.gcloud
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from Google cloud storage")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact

        except Exception as e:
            raise NerException(e, sys) from e
        

    def run_pipeline(self) -> None:
        try:
            logging.info("Started Model training >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise NerException(e, sys) from e