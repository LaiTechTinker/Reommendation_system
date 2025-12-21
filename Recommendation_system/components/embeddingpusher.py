import sys

from Recommendation_system.cloudstorage.awsstorage import SimpleStorageService
from Recommendation_system.exception import RecomException
from Recommendation_system.logger import logging
from Recommendation_system.entity.artifact_entity import ModelPusherArtifact,Embedding_Artifact
from Recommendation_system.entity.config_entity import ModelPusherConfig
from Recommendation_system.entity.s3_estimator import Recomfunc
from Recommendation_system.entity.config_entity import Embedding_Config

class EmbeddingPusher:
    def __init__(self, 
                 model_pusher_config: ModelPusherConfig):
        """
        :param model_evaluation_artifact: Output reference of data evaluation artifact stage
        :param model_pusher_config: Configuration for model pusher
        """
        self.s3 = SimpleStorageService()
        # self.model_evaluation_artifact = model_evaluation_artifact
        self.model_pusher_config = model_pusher_config
        self.Recom_func = Recomfunc(bucket_name=model_pusher_config.bucket_name,
                                model_path=model_pusher_config.s3_model_key_path)
        self.embedding_artifact=Embedding_Artifact

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        """
     this function block will initiate the embedded vector to amazon s3 bucket
        """
        logging.info("Entered initiate_model_pusher method of  embdedding class")

        try:
            logging.info("Uploading artifacts folder to s3 bucket")
            self.Recom_func.save_model(from_file=self.embedding_artifact.vector_embdedding_file_path)
            model_pusher_artifact = ModelPusherArtifact(bucket_name=self.model_pusher_config.bucket_name,
                                                        s3_model_path=self.model_pusher_config.s3_model_key_path)

            logging.info("Uploaded artifacts folder to s3 bucket")
            logging.info(f"Model pusher artifact: [{model_pusher_artifact}]")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")
            
            return model_pusher_artifact
        except Exception as e:
            raise RecomException(e, sys) from e