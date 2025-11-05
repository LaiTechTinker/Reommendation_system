import os
import sys
import ast
import numpy as np
import dill
import yaml
from pandas import DataFrame
from Recommendation_system.exception import RecomException
from Recommendation_system.logger import logging

# from Block_intel_class.exception import visaException
# from Visa_classifier import logging


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise RecomException(e, sys) from e
    


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise RecomException(e, sys) from e
    



def load_object(file_path: str) -> object:
    logging.info("Entered the load_object method of utils")

    try:

        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)

        logging.info("Exited the load_object method of utils")

        return obj

    except Exception as e:
        raise RecomException(e, sys) from e
    


def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise RecomException(e, sys) from e
    

def remove_whitespace(words):
    # If it's a list of strings, remove spaces from each element
    if isinstance(words, list):
        return [i.replace(" ", "") for i in words if isinstance(i, str)]
    
    # If it's a string, just strip internal and external spaces
    elif isinstance(words, str):
        return words.replace(" ", "")
    
    # Otherwise (int, float, NaN, etc.), return it as-is
    else:
        return words
def director_get(text):
    name = []
    
    # If it's a string, safely parse it
    if isinstance(text, str):
        try:
            items = ast.literal_eval(text)
        except Exception:
            # if it's not valid Python syntax, just return the text itself
            return text
    else:
        # Already a list or other type
        items = text
    
    # If it's a list of dicts, extract "name"
    for i in items:
       if i["job"]=="Director":
           name.append(i["name"])
       if len(name)==4:
           break
    
    return name
def convert_to_list(text):
    name = []
    
    # If it's a string, safely parse it
    if isinstance(text, str):
        try:
            items = ast.literal_eval(text)
        except Exception:
            # if it's not valid Python syntax, just return the text itself
            return text
    else:
        # Already a list or other type
        items = text
    
    # If it's a list of dicts, extract "name"
    for i in items:
        if isinstance(i, dict) and "name" in i:
            name.append(i["name"])
        
        elif isinstance(i, str):
            name.append(i)  # already plain string (like 'Action')
    
    return name

def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise RecomException(e, sys) from e




def save_object(file_path: str, obj: object) -> None:
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save_object method of utils")

    except Exception as e:
        raise RecomException(e, sys) from e



def drop_columns(df: DataFrame, cols: list)-> DataFrame:

    """
    drop the columns form a pandas DataFrame
    df: pandas DataFrame
    cols: list of columns to be dropped
    """
    logging.info("Entered drop_columns methon of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")
        
        return df
    except Exception as e:
        raise RecomException(e, sys) from e