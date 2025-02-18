import os
import sys
from src.exception import Custom_Exception    # my custom exception class
from src.logger import logging                # my custom logger class 
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass       # note this new library

# importing data transformation class and its config class
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


# This class is responsible for reading the data from the source
# I am defining all the inputs in the dataclass
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifects',"train.csv")
    test_data_path: str = os.path.join('artifects',"test.csv")
    raw_data_path: str = os.path.join('artifects',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()   # calling the dataclass constructor to get the default values

    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion process")
        try:
            df=pd.read_csv('notebook\data\stud.csv')    # Reading data from csv file. # data source can be anything here#
            logging.info("Data set is imported in the panadas dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header= True)  # saving the raw data in the artifects folder

            logging.info("Train Test Split is Initialized")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)  # splitting the data into train and test        

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header= True)  # saving the train data in the artifects folder

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header= True)  # saving the test data in the artifects folder

            logging.info("Data Ingestion Process Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
    
        except Exception as e:
            raise Custom_Exception(e, sys)
        
        
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    # initiating the data transformation process
    data_transformation_obj = DataTransformation()
    data_transformation_obj.initiate_data_transformation(train_data, test_data)
    




