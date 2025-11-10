from Recommendation_system.logger import logging
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import sklearn
from Recommendation_system.utils.main_utils import save_object
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from pandas import DataFrame
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from Recommendation_system.constants import *
from Recommendation_system.entity.artifact_entity import Embedding_Artifact,DataTransformationArtifact
from Recommendation_system.entity.config_entity import Embedding_Config
from Recommendation_system.exception import RecomException

class EmbeddingTrainer:
    def __init__(self,datatransformation_artifact:DataTransformationArtifact,embedding_artifact:Embedding_Artifact,embedding_config:Embedding_Config):
        self.datatransformation=datatransformation_artifact
        self.embedding_artifact=embedding_artifact
        self.embedding_config=embedding_config
        self.cv=CountVectorizer(max_features=5000,stop_words='english')
        
    def stemmer(self,text):
         ps=PorterStemmer()
         y=[]
         for i in text.split():
          y.append(ps.stem(i))
         return " ".join(y)
    def initiate_count_vectorizer(self,df:DataFrame):
     try:
        logging.info("entered initiate_count_vactorizer")
        df["combined_features"]=df["combined_features"].apply(self.stemmer)
        vectors=self.cv.fit_transform(df['combined_features']).toarray()
        similarity_scores=cosine_similarity(vectors)
        return similarity_scores
     except Exception as e:
        raise RecomException(e)
    def  final_op(self,):
     try:
        logging.info("entered embedding final ops")
        train_df=pd.read_csv(self.datatransformation.trasformed_trained_file)
        scores=self.initiate_count_vectorizer(train_df)
        save_object(self.embedding_config.vector_file,scores)
        embdding_artifact=Embedding_Artifact(
           vector_embdedding_file_path=self.embedding_config.vector_file
        )
        return embdding_artifact
     except Exception as e:
        raise RecomException(e)




        
